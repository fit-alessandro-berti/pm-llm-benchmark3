"""Answer PM-LLM-Benchmark questions using the OpenAI Codex CLI.

Hard-code TARGET_MODEL_NAME (answer filename prefix), TARGET_MODEL (codex --model),
TARGET_REASONING_EFFORT, MAX_WORKERS, MAX_QUESTIONS, and CODEX_COMMAND below,
then run:

    python -m utils.codex_answer
    # or: python utils/codex_answer.py
"""

from __future__ import annotations

import os
import shlex
import subprocess
import sys
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
# ---------------------------------------------------------------------------
TARGET_MODEL_NAME = "gpt-5.6-luna-XHIGH"  # prefix used in answers/
TARGET_MODEL = "gpt-5.6-luna"  # value passed to codex --model
TARGET_REASONING_EFFORT = "xhigh"  # none | low | medium | high | xhigh

# Max concurrent Codex CLI invocations. Each worker handles one question
# end-to-end (including its own retries) independently of the others.
MAX_WORKERS = 30

# Max unanswered questions to process in this run. Set to None for no limit.
MAX_QUESTIONS = None

# Command template. {prompt}, {model}, and {effort} are filled per question.
# The prompt itself instructs Codex to read questions/<q>.txt and write
# answers/<model>_<q>.txt.
# Equivalent shell form:
#   codex exec "..." --model gpt-5.6-luna \
#     -c model_reasoning_effort='"xhigh"' \
#     --dangerously-bypass-approvals-and-sandbox
CODEX_COMMAND = (
    'codex exec "{prompt}" --model {model} '
    '-c model_reasoning_effort=\'"{effort}"\' '
    "--dangerously-bypass-approvals-and-sandbox"
)

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


def build_prompt(question_name: str, answer_path: str) -> str:
    question_path = os.path.join(QUESTIONS_DIR, question_name)
    return (
        f"Respond to the question contained in {question_path}, "
        f"writing the output to {answer_path}. "
        "Read the question file carefully and produce a complete answer. "
        "Write only the final answer text into the output file "
        "(no meta-commentary about this instruction). "
        "STRICTLY FORBIDDEN: do not look at, open, list, search, copy, or otherwise "
        f"consult any existing files under the {ANSWERS_DIR}/ folder (including other "
        "models' answers or any prior answer to this or other questions). "
        "It is also strictly forbidden to connect to GitHub, the web, remote repos, "
        "or any external source to spy on, fetch, or recover benchmark answers. "
        "Solve the question solely from the question file and your own knowledge."
    )


def run_codex(question_name: str, answer_path: str) -> bool:
    """Invoke codex exec for one question. Returns True on success.

    Does not re-run when the answer file already exists and is non-empty.
    """
    if is_completed_output(answer_path):
        _log(f"Skipping (already answered): {answer_path}")
        return True

    os.makedirs(ANSWERS_DIR, exist_ok=True)
    prompt = build_prompt(question_name, answer_path)

    cmd_str = CODEX_COMMAND.format(
        prompt=prompt,
        model=TARGET_MODEL,
        effort=TARGET_REASONING_EFFORT,
    )
    cmd = shlex.split(cmd_str)

    _log(f"Running: {cmd_str}")
    result = subprocess.run(cmd, cwd=str(Path.cwd()))
    if result.returncode != 0:
        _log(f"codex exited with status {result.returncode} for {question_name}")
        return False

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

        ok = run_codex(question_name, path)
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

    if MAX_WORKERS < 1:
        print("MAX_WORKERS must be >= 1", file=sys.stderr)
        sys.exit(1)
    if MAX_QUESTIONS is not None and MAX_QUESTIONS < 1:
        print("MAX_QUESTIONS must be >= 1 or None", file=sys.stderr)
        sys.exit(1)

    questions = list_questions()
    print(
        f"Codex answering with model_name={TARGET_MODEL_NAME!r}, "
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
        print(f"Running up to {MAX_WORKERS} concurrent Codex process(es)")
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
