"""Package strict evaluation prompts for manual evaluation with ChatGPT.

For every model represented in ``answers/``, this script creates one ZIP archive
containing the 56 evaluation prompts for that model.  Run it from any directory
with::

    python -m utils.zip_evaluation

The generated directory is intentionally not deleted when the process exits so
that its ZIP files can be uploaded to ChatGPT.
"""

from __future__ import annotations

import argparse
import io
import shutil
import sys
import tempfile
import zipfile
from collections import defaultdict
from contextlib import redirect_stdout
from pathlib import Path

try:
    from utils.script_bootstrap import add_repo_root_to_path
except ModuleNotFoundError:
    from script_bootstrap import add_repo_root_to_path

add_repo_root_to_path()

from common import model_session
from file_utils import read_file_with_fallback
from utils import forge_eval_prompt
from utils.script_bootstrap import REPO_ROOT


EXPECTED_PROMPTS_PER_MODEL = 56
TEMP_DIR_PREFIX = "pm-llm-zip-evaluation-"
EVALUATION_FOLDER_NAME = "evaluation-GPT-5.6-Sol-Pro"

GPT_PROMPT = f"""I have attached a ZIP archive containing exactly 56 independent .txt evaluation prompts.

For every .txt file in the attached archive:
1. Read and execute the evaluation prompt in that file independently.
2. Write only the resulting evaluation to an output .txt file. Put the numeric grade at the beginning, exactly as the evaluation prompt requests.
3. Give the output file exactly the same filename as its corresponding input file.

Return one ZIP archive containing exactly those 56 completed .txt files at the archive root. Do not rename, omit, combine, or add files, and do not include directories or the original prompts. The returned ZIP must be directly extractable into `{EVALUATION_FOLDER_NAME}/`.
"""


def resolve_from_repo(path: Path) -> Path:
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create one ZIP of strict evaluation prompts for each answer model."
        )
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
        help=(
            "Question directory relative to the repository root (default: questions)."
        ),
    )
    return parser.parse_args(argv)


def collect_answers_by_model(
    answers_folder: Path,
    questions_folder: Path,
) -> dict[str, list[tuple[Path, Path]]]:
    """Return model -> sorted ``(answer, question)`` pairs after validation."""
    grouped: dict[str, list[tuple[Path, Path]]] = defaultdict(list)

    for answer_path in sorted(answers_folder.glob("*.txt")):
        model_and_question = answer_path.name.split("_cat", 1)
        if (
            len(model_and_question) != 2
            or not model_and_question[0]
            or not model_and_question[1]
        ):
            raise ValueError(f"Malformed answer filename: {answer_path.name}")

        model, question_suffix = model_and_question
        question_path = questions_folder / f"cat{question_suffix}"
        if not question_path.is_file():
            raise FileNotFoundError(
                f"No matching question for {answer_path.name}: {question_path}"
            )
        grouped[model].append((answer_path, question_path))

    if not grouped:
        raise ValueError(f"No answer files found in {answers_folder}")

    invalid_counts = {
        model: len(entries)
        for model, entries in grouped.items()
        if len(entries) != EXPECTED_PROMPTS_PER_MODEL
    }
    if invalid_counts:
        details = ", ".join(
            f"{model}={count}" for model, count in sorted(invalid_counts.items())
        )
        raise ValueError(
            f"Every model must have exactly {EXPECTED_PROMPTS_PER_MODEL} answers; "
            f"found {details}"
        )

    return dict(grouped)


def build_strict_evaluation_prompt(
    model: str,
    answer_path: Path,
    question_path: Path,
) -> str:
    """Forge a prompt while explicitly enabling severe/strict evaluation."""
    answer = read_file_with_fallback(answer_path)
    with model_session(TRIAL_SEVERE_EVALUATION=True):
        # ``forge`` currently emits a diagnostic for some reasoning models.  It
        # is unrelated to this script's user-facing output, so keep it quiet.
        with redirect_stdout(io.StringIO()):
            prompt, image = forge_eval_prompt.forge(
                str(question_path),
                answer,
                answering_model_name=model,
            )

    if image is not None:
        raise ValueError(f"Expected a text question, got an image for {answer_path.name}")
    return prompt


def create_archives(
    answers_by_model: dict[str, list[tuple[Path, Path]]],
) -> Path:
    """Create the model archives and return their persistent temporary folder."""
    output_folder = Path(tempfile.mkdtemp(prefix=TEMP_DIR_PREFIX)).resolve()
    try:
        for model, entries in sorted(answers_by_model.items()):
            archive_path = output_folder / f"{model}.zip"
            with zipfile.ZipFile(
                archive_path,
                mode="w",
                compression=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            ) as archive:
                for answer_path, question_path in entries:
                    prompt = build_strict_evaluation_prompt(
                        model,
                        answer_path,
                        question_path,
                    )
                    archive.writestr(answer_path.name, prompt)
    except Exception:
        shutil.rmtree(output_folder)
        raise

    return output_folder


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    answers_folder = resolve_from_repo(args.answers_folder)
    questions_folder = resolve_from_repo(args.questions_folder)

    if not answers_folder.is_dir():
        print(f"Answers folder does not exist: {answers_folder}", file=sys.stderr)
        return 2
    if not questions_folder.is_dir():
        print(f"Questions folder does not exist: {questions_folder}", file=sys.stderr)
        return 2

    try:
        answers_by_model = collect_answers_by_model(
            answers_folder,
            questions_folder,
        )
        output_folder = create_archives(answers_by_model)
    except (OSError, ValueError) as exc:
        print(f"Could not create evaluation ZIP files: {exc}", file=sys.stderr)
        return 2

    print(
        f"Created {len(answers_by_model)} ZIP archive(s), each containing "
        f"{EXPECTED_PROMPTS_PER_MODEL} strict evaluation prompts."
    )
    print(f"Temporary folder: {output_folder}")
    print()
    print()
    print()
    print("Attach one ZIP file at a time and give GPT-5.6 Sol Pro this prompt:")
    print()
    print(GPT_PROMPT.rstrip())
    print()
    print()
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
