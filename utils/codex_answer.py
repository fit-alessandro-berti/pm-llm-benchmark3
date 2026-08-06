"""Answer PM-LLM-Benchmark questions using the OpenAI Codex CLI.

Hard-code TARGET_MODEL_NAME (answer filename prefix), TARGET_MODEL (codex --model),
TARGET_REASONING_EFFORT, and CODEX_COMMAND below, then run:

    python -m utils.codex_answer
    # or: python utils/codex_answer.py
"""

from __future__ import annotations

import os
import shlex
import subprocess
import sys
import time
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

SLEEP_BETWEEN_QUESTIONS_SEC = 60
QUESTIONS_DIR = "questions"
ANSWERS_DIR = "answers"


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
        print(f"Skipping (already answered): {answer_path}")
        return True

    os.makedirs(ANSWERS_DIR, exist_ok=True)
    prompt = build_prompt(question_name, answer_path)

    cmd_str = CODEX_COMMAND.format(
        prompt=prompt,
        model=TARGET_MODEL,
        effort=TARGET_REASONING_EFFORT,
    )
    cmd = shlex.split(cmd_str)

    print("Running:", cmd_str)
    result = subprocess.run(cmd, cwd=str(Path.cwd()))
    if result.returncode != 0:
        print(f"codex exited with status {result.returncode} for {question_name}")
        return False

    if not is_completed_output(answer_path):
        print(f"No completed answer written to {answer_path}")
        return False

    print(f"Wrote {answer_path}")
    return True


def main() -> None:
    chdir_repo_root()

    if not os.path.isdir(QUESTIONS_DIR):
        print(f"Missing {QUESTIONS_DIR}/ directory", file=sys.stderr)
        sys.exit(1)

    questions = list_questions()
    print(
        f"Codex answering with model_name={TARGET_MODEL_NAME!r}, "
        f"model={TARGET_MODEL!r}, reasoning_effort={TARGET_REASONING_EFFORT!r}"
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

    print(f"{len(pending)} question(s) remaining")

    for index, q in enumerate(pending):
        path = answer_path_for(q, TARGET_MODEL_NAME)
        # Re-check immediately before each run (file may have appeared meanwhile).
        if is_completed_output(path):
            print(f"\n[{index + 1}/{len(pending)}] Skipping (already answered): {path}")
            continue

        print(f"\n[{index + 1}/{len(pending)}] {q} -> {path}")
        ok = run_codex(q, path)
        if not ok:
            print(f"Failed on {q}; continuing to next question after sleep")

        if index + 1 < len(pending):
            print(
                f"Sleeping {SLEEP_BETWEEN_QUESTIONS_SEC} seconds before next question..."
            )
            time.sleep(SLEEP_BETWEEN_QUESTIONS_SEC)

    print("\nDone.")


if __name__ == "__main__":
    main()
