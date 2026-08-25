#!/usr/bin/env python3
"""List the models whose answers are closest to a given model."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

EMBEDDINGS_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = EMBEDDINGS_DIR / "output"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Compute cosine distance between a model and every other model, "
            "then list the most similar models."
        )
    )
    parser.add_argument(
        "model",
        help="Model name (as used in answers/ filenames, or a unique substring).",
    )
    parser.add_argument(
        "--embeddings-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Directory of per-answer embedding JSON files (default: embeddings/output).",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="How many nearest models to list (default: 5).",
    )
    return parser.parse_args(argv)


def parse_answer_stem(stem: str) -> tuple[str, str] | None:
    # answers/<model>_catXX_YY_<slug>.txt
    if "_cat" not in stem:
        return None
    model, question = stem.split("_cat", 1)
    if not model:
        return None
    return model, "cat" + question


def load_model_embeddings(embeddings_dir: Path) -> dict[str, dict[str, np.ndarray]]:
    if not embeddings_dir.is_dir():
        raise SystemExit(
            f"Embeddings directory not found: {embeddings_dir}\n"
            "Run embeddings/embed_answers.py first."
        )

    models: dict[str, dict[str, np.ndarray]] = defaultdict(dict)
    for path in embeddings_dir.glob("*.json"):
        parsed = parse_answer_stem(path.stem)
        if parsed is None:
            continue
        try:
            with open(path, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, json.JSONDecodeError):
            continue

        embedding = payload.get("embedding") if isinstance(payload, dict) else payload
        if not isinstance(embedding, list) or not embedding:
            continue

        model, key = parsed
        models[model][key] = np.asarray(embedding, dtype=np.float64)

    if not models:
        raise SystemExit(
            f"No valid embeddings in {embeddings_dir}. Run embeddings/embed_answers.py first."
        )
    return models


def resolve_model(query: str, models: list[str]) -> str:
    if query in models:
        return query

    lower_map = {name.lower(): name for name in models}
    if query.lower() in lower_map:
        return lower_map[query.lower()]

    matches = [name for name in models if query.lower() in name.lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        listing = "\n".join(f"  {name}" for name in sorted(matches))
        raise SystemExit(f"Ambiguous model {query!r}. Matches:\n{listing}")

    raise SystemExit(f"Unknown model {query!r}. No embeddings found for it.")


def l2_normalize(vector: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def model_centroid(answer_embeddings: dict[str, np.ndarray]) -> np.ndarray:
    stacked = np.vstack(list(answer_embeddings.values()))
    return l2_normalize(stacked.mean(axis=0))


def cosine_distance(left: np.ndarray, right: np.ndarray) -> float:
    similarity = float(np.dot(left, right))
    similarity = max(-1.0, min(1.0, similarity))
    return 1.0 - similarity


def aligned_cosine_distance(
    left_answers: dict[str, np.ndarray],
    right_answers: dict[str, np.ndarray],
) -> float:
    """Mean cosine distance over answers that share the same question."""
    shared_keys = set(left_answers) & set(right_answers)
    if not shared_keys:
        return cosine_distance(model_centroid(left_answers), model_centroid(right_answers))

    distances = [
        cosine_distance(l2_normalize(left_answers[key]), l2_normalize(right_answers[key]))
        for key in shared_keys
    ]
    return float(np.mean(distances))


def nearest_models(
    query_model: str,
    models: dict[str, dict[str, np.ndarray]],
    top_n: int,
) -> list[tuple[str, float]]:
    query_answers = models[query_model]
    ranked = []
    for other_model, other_answers in models.items():
        if other_model == query_model:
            continue
        ranked.append((other_model, aligned_cosine_distance(query_answers, other_answers)))
    ranked.sort(key=lambda item: (item[1], item[0]))
    return ranked[: max(0, top_n)]


def main(argv=None) -> int:
    args = parse_args(argv)
    if args.top < 1:
        raise SystemExit("--top must be at least 1")

    models = load_model_embeddings(args.embeddings_dir)
    query_model = resolve_model(args.model, list(models))
    nearest = nearest_models(query_model, models, args.top)

    if not nearest:
        raise SystemExit(f"No other models to compare with {query_model!r}.")

    print(
        f"Top-{len(nearest)} similar models to {query_model} "
        "(mean cosine distance over aligned question answers, lower is closer):"
    )
    name_width = max(len(name) for name, _ in nearest)
    for rank, (name, distance) in enumerate(nearest, start=1):
        print(f"{rank}. {name:<{name_width}}  {distance:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
