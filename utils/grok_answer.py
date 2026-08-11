"""Answer PM-LLM-Benchmark questions using the xAI Grok CLI.

Hard-code TARGET_MODEL_NAME (answer filename prefix), TARGET_MODEL (grok --model),
TARGET_REASONING_EFFORT, MAX_WORKERS, and MAX_QUESTIONS below, then run:

    python -m utils.grok_answer
    # or: python utils/grok_answer.py

This script is for *answering* only. Evaluation uses utils/grok_evaluate.py with
its own TARGET_MODEL / TARGET_REASONING_EFFORT.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    from utils.script_bootstrap import chdir_repo_root
except ModuleNotFoundError:
    from script_bootstrap import chdir_repo_root

from common import clean_model_name, is_completed_output

# ---------------------------------------------------------------------------
# Hard-coded run configuration — edit these before launching.
# (Independent of utils/grok_evaluate.py judge settings.)
# ---------------------------------------------------------------------------
TARGET_MODEL_NAME = "grok-4.5"  # prefix used in answers/
TARGET_MODEL = "grok-4.5"  # value passed to grok --model
TARGET_REASONING_EFFORT = "high"  # low | medium | high | xhigh

# Max concurrent Grok CLI invocations. Each worker handles one question
# end-to-end (including its own retries) independently of the others.
MAX_WORKERS = 10

# Max unanswered questions to process in this run. Set to None for no limit.
MAX_QUESTIONS = None

# Grok CLI executable name or path.
GROK_COMMAND = "grok"

# Used only when MAX_WORKERS == 1 (sequential mode).
SLEEP_BETWEEN_QUESTIONS_SEC = 60
# Backoff after consecutive failures of the *same* question. After the last
# entry, further retries keep using that delay (max every 10 minutes).
RETRY_BACKOFF_SEC = (60, 300, 600)
QUESTIONS_DIR = "questions"
ANSWERS_DIR = "answers"

_print_lock = threading.Lock()


def _log(msg: str) -> None:
    with _print_lock:
        print(msg, flush=True)


def list_questions() -> list[str]:
    return sorted(
        name for name in os.listdir(QUESTIONS_DIR) if name.endswith(".txt")
    )


def answer_path_for(question_name: str, model_name: str) -> str:
    base = question_name if question_name.endswith(".txt") else question_name + ".txt"
    return os.path.join(ANSWERS_DIR, clean_model_name(model_name) + "_" + base)


def build_prompt(question_text: str) -> str:
    return (
        "Answer the following process-mining benchmark question completely and "
        "carefully. Write only the final answer text "
        "(no meta-commentary about this instruction).\n\n"
        f"{question_text.strip()}\n"
    )


def build_grok_command(workspace: Path, prompt_path: Path) -> list[str]:
    return [
        GROK_COMMAND,
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


def run_grok(question_name: str, answer_path: str) -> bool:
    """Invoke grok for one question. Returns True on success.

    Does not re-run when the answer file already exists and is non-empty.
    Reads the question, calls the CLI with tools disabled, and writes the
    parsed response to answer_path (same isolation pattern as grok_evaluate).
    """
    if is_completed_output(answer_path):
        _log(f"Skipping (already answered): {answer_path}")
        return True

    question_path = os.path.join(QUESTIONS_DIR, question_name)
    try:
        question_text = Path(question_path).read_text(encoding="utf-8")
    except OSError as exc:
        _log(f"Failed to read {question_path}: {exc}")
        return False

    if not question_text.strip():
        _log(f"Question file is empty: {question_path}")
        return False

    os.makedirs(ANSWERS_DIR, exist_ok=True)
    prompt = build_prompt(question_text)

    with tempfile.TemporaryDirectory(prefix="pm-llm-grok-answer-") as temp_dir:
        workspace = Path(temp_dir).resolve()
        prompt_path = workspace / "answer_prompt.txt"
        prompt_path.write_text(prompt, encoding="utf-8")

        cmd = build_grok_command(workspace, prompt_path)
        _log(f"Running: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

    if result.returncode != 0:
        output = result.stderr.strip() or result.stdout.strip()
        if output:
            _log(f"grok exited with status {result.returncode}: {output[-2000:]}")
        else:
            _log(f"grok exited with status {result.returncode} for {question_name}")
        return False

    try:
        response = parse_grok_response(result.stdout)
    except Exception as exc:
        _log(f"Invalid Grok answer for {question_name}: {exc}")
        return False

    # Re-check before write in case another worker finished first.
    if is_completed_output(answer_path):
        _log(f"Skipping write (already answered): {answer_path}")
        return True

    Path(answer_path).write_text(response.strip() + "\n", encoding="utf-8")

    if not is_completed_output(answer_path):
        _log(f"No completed answer written to {answer_path}")
        return False

    _log(f"Wrote {answer_path}")
    return True


def process_question(question_name: str, label: str) -> bool:
    """Run one question to completion with independent retries. Thread-safe."""
    path = answer_path_for(question_name, TARGET_MODEL_NAME)
    if is_completed_output(path):
        _log(f"{label} Skipping (already answered): {path}")
        return True

    _log(f"{label} {question_name} -> {path}")
    fail_count = 0
    while True:
        # Re-check in case another worker (or a previous attempt) finished it.
        if is_completed_output(path):
            _log(f"{label} Skipping (already answered): {path}")
            return True

        ok = run_grok(question_name, path)
        if ok:
            return True
        delay = RETRY_BACKOFF_SEC[min(fail_count, len(RETRY_BACKOFF_SEC) - 1)]
        fail_count += 1
        _log(
            f"{label} Failed on {question_name} (attempt {fail_count}); "
            f"retrying same question after {delay} seconds..."
        )
        time.sleep(delay)


def main() -> None:
    chdir_repo_root()

    if not os.path.isdir(QUESTIONS_DIR):
        print(f"Missing {QUESTIONS_DIR}/ directory", file=sys.stderr)
        sys.exit(1)

    if shutil.which(GROK_COMMAND) is None:
        print(f"Grok CLI executable was not found: {GROK_COMMAND}", file=sys.stderr)
        sys.exit(1)

    if MAX_WORKERS < 1:
        print("MAX_WORKERS must be >= 1", file=sys.stderr)
        sys.exit(1)
    if MAX_QUESTIONS is not None and MAX_QUESTIONS < 1:
        print("MAX_QUESTIONS must be >= 1 or None", file=sys.stderr)
        sys.exit(1)

    questions = list_questions()
    print(
        f"Grok answering with model_name={TARGET_MODEL_NAME!r}, "
        f"model={TARGET_MODEL!r}, reasoning_effort={TARGET_REASONING_EFFORT!r}, "
        f"max_workers={MAX_WORKERS}, max_questions={MAX_QUESTIONS}"
    )
    print(f"{len(questions)} question file(s) under {QUESTIONS_DIR}/")

    # Only questions without an existing non-empty answer are executed.
    pending: list[str] = []
    for q in questions:
        path = answer_path_for(q, TARGET_MODEL_NAME)
        if is_completed_output(path):
            print(f"Skipping (already answered): {path}")
        else:
            pending.append(q)

    pending_count = len(pending)
    if MAX_QUESTIONS is not None:
        pending = pending[:MAX_QUESTIONS]

    total = len(pending)
    print(f"{pending_count} question(s) remaining; {total} selected for this run")
    if not pending:
        print("\nDone.")
        return

    if MAX_WORKERS == 1:
        # Sequential path preserves the original inter-question sleep.
        for index, q in enumerate(pending):
            process_question(q, label=f"[{index + 1}/{total}]")
            if index + 1 < total:
                print(
                    f"Sleeping {SLEEP_BETWEEN_QUESTIONS_SEC} seconds "
                    f"before next question..."
                )
                time.sleep(SLEEP_BETWEEN_QUESTIONS_SEC)
    else:
        # Concurrent: each question runs independently on its own worker
        # (own subprocess + own retry/backoff loop).
        print(f"Running up to {MAX_WORKERS} concurrent Grok process(es)")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {
                executor.submit(
                    process_question, q, f"[{index + 1}/{total}]"
                ): q
                for index, q in enumerate(pending)
            }
            for future in as_completed(futures):
                q = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    _log(f"Unexpected error on {q}: {exc!r}")

    print("\nDone.")


if __name__ == "__main__":
    main()
