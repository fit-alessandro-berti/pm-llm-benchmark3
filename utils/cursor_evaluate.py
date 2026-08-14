"""Evaluate PM-LLM-Benchmark answers with the Cursor CLI (`agent`).

Writes into the same evaluation directory as utils/grok_evaluate.py.

Run from any directory with::

    python -m utils.cursor_evaluate
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


# Base id passed to `agent --model`. Effort is appended as a hyphen suffix
# (e.g. cursor-grok-4.6-high). Leave TARGET_REASONING_EFFORT empty when the
# base id is already a full effort-suffixed slug.
TARGET_MODEL = "cursor-grok-4.6"
TARGET_REASONING_EFFORT = "high"
MAX_WORKERS = 75
DEFAULT_RETRY_DELAY_SECONDS = 17.0
EVALUATION_FOLDER = Path("evaluation-grok-4.6")

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


def cursor_model_spec() -> str:
    """Compose the value passed to `agent --model`."""
    if TARGET_REASONING_EFFORT:
        return f"{TARGET_MODEL}-{TARGET_REASONING_EFFORT}"
    return TARGET_MODEL


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate every answer with the Cursor CLI in non-interactive mode."
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
        "--agent-command",
        default="agent",
        help="Cursor CLI executable (default: agent).",
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


def agent_instruction(prompt_path: Path) -> str:
    return (
        f"Read the evaluation request in {prompt_path}. Perform exactly the "
        "evaluation requested there and return only the evaluation, with the "
        "numeric grade at the beginning. Do not inspect any other files. Do not "
        "use web search, network access, MCP, connectors, skills, plugins, "
        "subagents, or tools other than reading the specified prompt file."
    )


def build_agent_command(
    agent_command: str,
    workspace: Path,
    prompt_path: Path,
) -> list[str]:
    return [
        agent_command,
        "-p",
        agent_instruction(prompt_path),
        "--output-format",
        "json",
        "--mode",
        "ask",
        "--model",
        cursor_model_spec(),
        "--trust",
        "--sandbox",
        "disabled",
        "--workspace",
        str(workspace),
    ]


def parse_agent_response(output: str) -> str:
    text = output.strip()
    if not text:
        raise ValueError("Cursor output is empty")

    try:
        envelope = json.loads(text)
    except json.JSONDecodeError:
        envelope = json.loads(text.splitlines()[-1])

    if not isinstance(envelope, dict):
        raise ValueError("Cursor output must be a JSON object")
    if envelope.get("is_error") or envelope.get("type") == "error":
        detail = envelope.get("result") or envelope.get("message") or ""
        raise ValueError(f"Cursor returned an error: {detail}")

    response = envelope.get("result")
    if not isinstance(response, str) or not response.strip():
        raise ValueError("Cursor output does not contain non-empty result text")
    return response


def run_one_attempt(
    prompt: str,
    evaluation_path: Path,
    agent_command: str,
) -> bool:
    with tempfile.TemporaryDirectory(prefix="pm-llm-cursor-eval-") as temp_dir:
        workspace = Path(temp_dir).resolve()
        prompt_path = workspace / "evaluation_prompt.txt"
        prompt_path.write_text(prompt, encoding="utf-8")

        result = subprocess.run(
            build_agent_command(agent_command, workspace, prompt_path),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

    if result.returncode != 0:
        output = result.stderr.strip() or result.stdout.strip()
        if output:
            log(f"Cursor exited with status {result.returncode}: {output[-2000:]}")
        else:
            log(f"Cursor exited with status {result.returncode}")
        return False

    try:
        response = parse_agent_response(result.stdout)
        validate_evaluation_text(response)
    except Exception as exc:
        log(f"Invalid Cursor evaluation for {evaluation_path.name}: {exc}")
        return False

    evaluation_path.write_text(response.strip() + "\n", encoding="utf-8")
    return True


def evaluate_until_valid(
    label: str,
    answering_model: str,
    question_path: Path,
    answer_path: Path,
    evaluation_path: Path,
    agent_command: str,
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
            if run_one_attempt(prompt, evaluation_path, agent_command):
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
    if shutil.which(args.agent_command) is None:
        print(
            f"Cursor CLI executable was not found: {args.agent_command}",
            file=sys.stderr,
        )
        return 2

    evaluation_folder.mkdir(parents=True, exist_ok=True)
    tasks = collect_tasks(answers_folder, questions_folder, evaluation_folder)
    pending = [task for task in tasks if not has_valid_evaluation(task[3])]

    log(f"Found {len(tasks)} answer(s); {len(pending)} evaluation(s) pending")
    log(
        f"Cursor model={cursor_model_spec()!r}, reasoning_effort="
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
                args.agent_command,
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
