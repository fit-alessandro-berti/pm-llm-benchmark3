"""Evaluate PM-LLM-Benchmark answers with the xAI Grok CLI.

Run from any directory with::

    python -m utils.grok_evaluate
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    from utils.script_bootstrap import add_repo_root_to_path
except ModuleNotFoundError:
    from script_bootstrap import add_repo_root_to_path

add_repo_root_to_path()

from file_utils import read_file_with_fallback
from utils import forge_eval_prompt
from utils.script_bootstrap import REPO_ROOT
from utils.table_per_model import match_regex


TARGET_MODEL = "grok-4.5"
TARGET_REASONING_EFFORT = "high"
MAX_WORKERS = 80
DEFAULT_RETRY_DELAY_SECONDS = 17.0
EVALUATION_FOLDER = Path("evaluation-grok-4.5")

_print_lock = threading.Lock()


def log(message: str) -> None:
    with _print_lock:
        print(message, flush=True)


def non_negative_float(value: str) -> float:
    parsed = float(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be at least 0")
    return parsed


def resolve_from_repo(path: Path) -> Path:
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate every answer with Grok in non-interactive mode."
    )
    parser.add_argument(
        "--answers-folder",
        type=Path,
        default=Path("answers"),
        help="Answer directory relative to the repository root (default: answers).",
    )
    parser.add_argument(
        "--questions-folder",
        type=Path,
        default=Path("questions"),
        help="Question directory relative to the repository root (default: questions).",
    )
    parser.add_argument(
        "--grok-command",
        default="grok",
        help="Grok CLI executable (default: grok).",
    )
    parser.add_argument(
        "--retry-delay",
        type=non_negative_float,
        default=DEFAULT_RETRY_DELAY_SECONDS,
        help="Seconds to wait after a failed attempt (default: 17).",
    )
    return parser.parse_args(argv)


def collect_tasks(
    answers_folder: Path,
    questions_folder: Path,
    evaluation_folder: Path,
) -> list[tuple[str, Path, Path, Path]]:
    """Return (answering model, question, answer, evaluation) tasks."""
    tasks: list[tuple[str, Path, Path, Path]] = []
    for answer_path in sorted(answers_folder.glob("*.txt")):
        parts = answer_path.name.split("_cat", 1)
        if len(parts) != 2 or not parts[0] or not parts[1]:
            log(f"Ignoring malformed answer filename: {answer_path.name}")
            continue

        answering_model = parts[0]
        question_path = questions_folder / f"cat{parts[1]}"
        if not question_path.is_file():
            log(f"Ignoring answer without matching question: {answer_path.name}")
            continue

        tasks.append(
            (
                answering_model,
                question_path,
                answer_path,
                evaluation_folder / answer_path.name,
            )
        )
    return tasks


def build_evaluation_prompt(
    answering_model: str,
    question_path: Path,
    answer_path: Path,
) -> str:
    answer = read_file_with_fallback(answer_path)
    prompt, _ = forge_eval_prompt.forge(
        str(question_path),
        answer,
        answering_model_name=answering_model,
    )
    return prompt


def validate_evaluation_text(text: str) -> None:
    if not text.strip():
        raise ValueError("evaluation is empty")
    if match_regex(text) is None:
        raise ValueError("evaluation does not contain a score from 1.0 to 10.0")


def has_valid_evaluation(evaluation_path: Path) -> bool:
    if not evaluation_path.is_file():
        return False
    try:
        validate_evaluation_text(read_file_with_fallback(evaluation_path))
    except Exception as exc:
        log(f"Invalid existing evaluation {evaluation_path.name}: {exc}")
        return False
    return True


def grok_instruction(prompt: str) -> str:
    return (
        f"{prompt}\n\n"
        "Return only the evaluation, with the numeric grade at the beginning."
    )


def build_grok_command(
    grok_command: str,
    workspace: Path,
    prompt_path: Path,
) -> list[str]:
    return [
        grok_command,
        "--prompt-file",
        str(prompt_path),
        "--verbatim",
        "--model",
        TARGET_MODEL,
        "--reasoning-effort",
        TARGET_REASONING_EFFORT,
        "--cwd",
        str(workspace),
        "--output-format",
        "json",
        "--tools",
        "",
        "--max-turns",
        "1",
        "--no-auto-update",
        "--rules",
        "Do not use tools, MCP servers, plugins, skills, or subagents.",
    ]


def parse_grok_response(output: str) -> str:
    envelope = json.loads(output)
    if not isinstance(envelope, dict):
        raise ValueError("Grok output must be a JSON object")
    if envelope.get("type") == "error":
        raise ValueError(f"Grok returned an error: {envelope.get('message', '')}")

    response = envelope.get("text")
    if not isinstance(response, str) or not response.strip():
        raise ValueError("Grok output does not contain non-empty text")
    return response


def run_one_attempt(
    prompt: str,
    evaluation_path: Path,
    grok_command: str,
) -> bool:
    with tempfile.TemporaryDirectory(prefix="pm-llm-grok-eval-") as temp_dir:
        workspace = Path(temp_dir).resolve()
        prompt_path = workspace / "evaluation_prompt.txt"
        prompt_path.write_text(grok_instruction(prompt), encoding="utf-8")

        result = subprocess.run(
            build_grok_command(grok_command, workspace, prompt_path),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

    if result.returncode != 0:
        output = result.stderr.strip() or result.stdout.strip()
        if output:
            log(f"Grok exited with status {result.returncode}: {output[-2000:]}")
        else:
            log(f"Grok exited with status {result.returncode}")
        return False

    try:
        response = parse_grok_response(result.stdout)
        validate_evaluation_text(response)
    except Exception as exc:
        log(f"Invalid Grok evaluation for {evaluation_path.name}: {exc}")
        return False

    evaluation_path.write_text(response.strip() + "\n", encoding="utf-8")
    return True


def evaluate_until_valid(
    label: str,
    answering_model: str,
    question_path: Path,
    answer_path: Path,
    evaluation_path: Path,
    grok_command: str,
    retry_delay: float,
) -> bool:
    if has_valid_evaluation(evaluation_path):
        log(f"{label} Skipping valid evaluation: {evaluation_path.name}")
        return True

    prompt = build_evaluation_prompt(answering_model, question_path, answer_path)
    attempt = 0
    while True:
        attempt += 1
        log(f"{label} Evaluating {evaluation_path.name} (attempt {attempt})")
        try:
            if run_one_attempt(prompt, evaluation_path, grok_command):
                log(f"{label} Wrote valid evaluation: {evaluation_path.name}")
                return True
        except Exception as exc:
            log(f"{label} Evaluation attempt failed: {exc!r}")

        if retry_delay:
            log(f"{label} Retrying in {retry_delay:g} seconds")
            time.sleep(retry_delay)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    answers_folder = resolve_from_repo(args.answers_folder)
    questions_folder = resolve_from_repo(args.questions_folder)
    evaluation_folder = resolve_from_repo(EVALUATION_FOLDER)

    if not answers_folder.is_dir():
        print(f"Answers folder does not exist: {answers_folder}", file=sys.stderr)
        return 2
    if not questions_folder.is_dir():
        print(f"Questions folder does not exist: {questions_folder}", file=sys.stderr)
        return 2
    if shutil.which(args.grok_command) is None:
        print(f"Grok CLI executable was not found: {args.grok_command}", file=sys.stderr)
        return 2

    evaluation_folder.mkdir(parents=True, exist_ok=True)
    tasks = collect_tasks(answers_folder, questions_folder, evaluation_folder)
    pending = [task for task in tasks if not has_valid_evaluation(task[3])]

    log(f"Found {len(tasks)} answer(s); {len(pending)} evaluation(s) pending")
    log(
        f"Grok model={TARGET_MODEL!r}, reasoning_effort="
        f"{TARGET_REASONING_EFFORT!r}, max_workers={MAX_WORKERS}"
    )
    if not pending:
        log("All evaluations are already valid.")
        return 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(
                evaluate_until_valid,
                f"[{index}/{len(pending)}] {answering_model}",
                answering_model,
                question_path,
                answer_path,
                evaluation_path,
                args.grok_command,
                args.retry_delay,
            )
            for index, (
                answering_model,
                question_path,
                answer_path,
                evaluation_path,
            ) in enumerate(pending, start=1)
        ]
        for future in as_completed(futures):
            future.result()

    log("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
