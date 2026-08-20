"""Answer PM-LLM-Benchmark questions using the Cursor CLI (`agent`).

Hard-code TARGET_MODEL_NAME (answer filename prefix), TARGET_MODEL (agent --model),
TARGET_REASONING_EFFORT, MAX_WORKERS, and MAX_QUESTIONS below, then run:

    python -m utils.cursor_answer
    # or: python utils/cursor_answer.py
"""

from __future__ import annotations

import os
import shutil
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
TARGET_MODEL_NAME = "claude-opus-4-8-high"  # prefix used in answers/
# Currently available Cursor models (`agent --list-models`, 2026-08-14):
#   auto
#   gpt-5.3-codex-low, gpt-5.3-codex-low-fast, gpt-5.3-codex, gpt-5.3-codex-fast,
#   gpt-5.3-codex-high, gpt-5.3-codex-high-fast, gpt-5.3-codex-xhigh,
#   gpt-5.3-codex-xhigh-fast
#   gpt-5.2, gpt-5.2-low, gpt-5.2-low-fast, gpt-5.2-fast, gpt-5.2-high,
#   gpt-5.2-high-fast, gpt-5.2-xhigh, gpt-5.2-xhigh-fast
#   cursor-grok-4.6-low, cursor-grok-4.6-low-fast, cursor-grok-4.6-medium,
#   cursor-grok-4.6-medium-fast, cursor-grok-4.6-high, cursor-grok-4.6-high-fast,
#   cursor-grok-4.6-xhigh, cursor-grok-4.6-xhigh-fast
#   composer-2.5, composer-2.5-fast
#   claude-opus-5-low, claude-opus-5-low-fast, claude-opus-5-medium,
#   claude-opus-5-medium-fast, claude-opus-5-high, claude-opus-5-high-fast,
#   claude-opus-5-thinking-low, claude-opus-5-thinking-low-fast,
#   claude-opus-5-thinking-medium, claude-opus-5-thinking-medium-fast,
#   claude-opus-5-thinking-high, claude-opus-5-thinking-high-fast,
#   claude-opus-5-thinking-xhigh, claude-opus-5-thinking-xhigh-fast,
#   claude-opus-5-thinking-max, claude-opus-5-thinking-max-fast
#   gpt-5.6-sol-none, gpt-5.6-sol-none-fast, gpt-5.6-sol-low, gpt-5.6-sol-low-fast,
#   gpt-5.6-sol-medium, gpt-5.6-sol-medium-fast, gpt-5.6-sol-high,
#   gpt-5.6-sol-high-fast, gpt-5.6-sol-xhigh, gpt-5.6-sol-xhigh-fast,
#   gpt-5.6-sol-max, gpt-5.6-sol-max-fast
#   claude-fable-5-low, claude-fable-5-medium, claude-fable-5-high,
#   claude-fable-5-xhigh, claude-fable-5-max, claude-fable-5-thinking-low,
#   claude-fable-5-thinking-medium, claude-fable-5-thinking-high,
#   claude-fable-5-thinking-xhigh, claude-fable-5-thinking-max
#   cursor-grok-4.5-low, cursor-grok-4.5-low-fast, cursor-grok-4.5-medium,
#   cursor-grok-4.5-medium-fast, cursor-grok-4.5-high, cursor-grok-4.5-high-fast
#   gemini-3.7-flash-low, gemini-3.7-flash-medium, gemini-3.7-flash-high
#   claude-sonnet-5-low, claude-sonnet-5-medium, claude-sonnet-5-high,
#   claude-sonnet-5-xhigh, claude-sonnet-5-max, claude-sonnet-5-thinking-low,
#   claude-sonnet-5-thinking-medium, claude-sonnet-5-thinking-high,
#   claude-sonnet-5-thinking-xhigh, claude-sonnet-5-thinking-max
#   gpt-5.6-luna-none, gpt-5.6-luna-none-fast, gpt-5.6-luna-low,
#   gpt-5.6-luna-low-fast, gpt-5.6-luna-medium, gpt-5.6-luna-medium-fast,
#   gpt-5.6-luna-high, gpt-5.6-luna-high-fast, gpt-5.6-luna-xhigh,
#   gpt-5.6-luna-xhigh-fast, gpt-5.6-luna-max, gpt-5.6-luna-max-fast
#   claude-opus-4-8-low, claude-opus-4-8-low-fast, claude-opus-4-8-medium,
#   claude-opus-4-8-medium-fast, claude-opus-4-8-high, claude-opus-4-8-high-fast,
#   claude-opus-4-8-xhigh, claude-opus-4-8-xhigh-fast, claude-opus-4-8-max,
#   claude-opus-4-8-max-fast, claude-opus-4-8-thinking-low,
#   claude-opus-4-8-thinking-low-fast, claude-opus-4-8-thinking-medium,
#   claude-opus-4-8-thinking-medium-fast, claude-opus-4-8-thinking-high,
#   claude-opus-4-8-thinking-high-fast, claude-opus-4-8-thinking-xhigh,
#   claude-opus-4-8-thinking-xhigh-fast, claude-opus-4-8-thinking-max,
#   claude-opus-4-8-thinking-max-fast
#   gpt-5.5-none, gpt-5.5-none-fast, gpt-5.5-low, gpt-5.5-low-fast,
#   gpt-5.5-medium, gpt-5.5-medium-fast, gpt-5.5-high, gpt-5.5-high-fast,
#   gpt-5.5-extra-high, gpt-5.5-extra-high-fast
#   gpt-5.6-terra-none, gpt-5.6-terra-none-fast, gpt-5.6-terra-low,
#   gpt-5.6-terra-low-fast, gpt-5.6-terra-medium, gpt-5.6-terra-medium-fast,
#   gpt-5.6-terra-high, gpt-5.6-terra-high-fast, gpt-5.6-terra-xhigh,
#   gpt-5.6-terra-xhigh-fast, gpt-5.6-terra-max, gpt-5.6-terra-max-fast
#   claude-4.6-sonnet-medium, claude-4.6-sonnet-medium-thinking
#   claude-opus-4-7-low, claude-opus-4-7-low-fast, claude-opus-4-7-medium,
#   claude-opus-4-7-medium-fast, claude-opus-4-7-high, claude-opus-4-7-high-fast,
#   claude-opus-4-7-xhigh, claude-opus-4-7-xhigh-fast, claude-opus-4-7-max,
#   claude-opus-4-7-max-fast, claude-opus-4-7-thinking-low,
#   claude-opus-4-7-thinking-low-fast, claude-opus-4-7-thinking-medium,
#   claude-opus-4-7-thinking-medium-fast, claude-opus-4-7-thinking-high,
#   claude-opus-4-7-thinking-high-fast, claude-opus-4-7-thinking-xhigh,
#   claude-opus-4-7-thinking-xhigh-fast, claude-opus-4-7-thinking-max,
#   claude-opus-4-7-thinking-max-fast
#   gpt-5.4-low, gpt-5.4-medium, gpt-5.4-medium-fast, gpt-5.4-high,
#   gpt-5.4-high-fast, gpt-5.4-xhigh, gpt-5.4-xhigh-fast
#   claude-4.6-opus-high, claude-4.6-opus-max, claude-4.6-opus-high-thinking,
#   claude-4.6-opus-max-thinking
#   claude-4.5-opus-high, claude-4.5-opus-high-thinking
#   gemini-3.6-flash-minimal, gemini-3.6-flash-low, gemini-3.6-flash-medium,
#   gemini-3.6-flash-high
#   gemini-3.1-pro
#   gpt-5.4-mini-none, gpt-5.4-mini-low, gpt-5.4-mini-medium, gpt-5.4-mini-high,
#   gpt-5.4-mini-xhigh
#   gpt-5.4-nano-none, gpt-5.4-nano-low, gpt-5.4-nano-medium, gpt-5.4-nano-high,
#   gpt-5.4-nano-xhigh
#   claude-4.5-sonnet, claude-4.5-sonnet-thinking
#   gpt-5.1-low, gpt-5.1, gpt-5.1-high
#   gemini-3-flash, gemini-3.5-flash
#   claude-4-sonnet, claude-4-sonnet-thinking
#   gpt-5-mini
#   kimi-k3-low, kimi-k3-high, kimi-k3-max
#   kimi-k2.7-code
#   glm-5.2-high, glm-5.2-max
# Base id passed to `agent --model`. Effort is appended as a hyphen suffix
# (e.g. claude-opus-5-thinking-high). Cursor does not accept [effort=...]
# overrides. You may also paste a full effort-suffixed slug here and leave
# TARGET_REASONING_EFFORT empty.
TARGET_MODEL = "claude-opus-4-8"
# none | low | medium | high | xhigh | extra-high | max | minimal; "" to omit
TARGET_REASONING_EFFORT = "high"

# Max concurrent Cursor CLI invocations. Each worker handles one question
# end-to-end (including its own retries) independently of the others.
MAX_WORKERS = 57

# Max unanswered questions to process in this run. Set to None for no limit.
MAX_QUESTIONS = None

# Cursor CLI executable name or path.
AGENT_COMMAND = "agent"

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


def cursor_model_spec() -> str:
    """Compose the value passed to `agent --model`."""
    if TARGET_REASONING_EFFORT:
        return f"{TARGET_MODEL}-{TARGET_REASONING_EFFORT}"
    return TARGET_MODEL


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


def build_agent_command(prompt: str) -> list[str]:
    return [
        AGENT_COMMAND,
        "-p",
        prompt,
        "--model",
        cursor_model_spec(),
        "--force",
        "--trust",
        "--sandbox",
        "disabled",
    ]


def run_cursor(question_name: str, answer_path: str) -> bool:
    """Invoke `agent -p` for one question. Returns True on success.

    Does not re-run when the answer file already exists and is non-empty.
    """
    if is_completed_output(answer_path):
        _log(f"Skipping (already answered): {answer_path}")
        return True

    os.makedirs(ANSWERS_DIR, exist_ok=True)
    prompt = build_prompt(question_name, answer_path)
    cmd = build_agent_command(prompt)

    _log(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=str(Path.cwd()))
    if result.returncode != 0:
        _log(f"agent exited with status {result.returncode} for {question_name}")
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

        ok = run_cursor(question_name, path)
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

    if shutil.which(AGENT_COMMAND) is None:
        print(f"Cursor CLI executable was not found: {AGENT_COMMAND}", file=sys.stderr)
        sys.exit(1)

    if MAX_WORKERS < 1:
        print("MAX_WORKERS must be >= 1", file=sys.stderr)
        sys.exit(1)
    if MAX_QUESTIONS is not None and MAX_QUESTIONS < 1:
        print("MAX_QUESTIONS must be >= 1 or None", file=sys.stderr)
        sys.exit(1)

    questions = list_questions()
    print(
        f"Cursor answering with model_name={TARGET_MODEL_NAME!r}, "
        f"model={cursor_model_spec()!r}, reasoning_effort={TARGET_REASONING_EFFORT!r}, "
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
        print(f"Running up to {MAX_WORKERS} concurrent Cursor process(es)")
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
