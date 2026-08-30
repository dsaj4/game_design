from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .embedding_cache import (
    DEFAULT_MODEL_ID,
    DEFAULT_MODEL_REVISION,
    EmbeddingCacheError,
    build_embedding_cache,
    load_embedding_cache,
    write_embedding_cache,
)
from .engine import CatalogError, GenerationError, generate_card, load_catalog
from .experiment import ExperimentError, load_experiment_config, run_comparison


DEFAULT_CATALOG = Path(__file__).parents[1] / "data" / "catalog.json"
DEFAULT_EXPERIMENT = Path(__file__).parents[1] / "data" / "experiment.json"
DEFAULT_EMBEDDING_CACHE = Path(__file__).parents[1] / "data" / "embedding-cache.json"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        prog="semantic-card-engine",
        description="Compile semantic concepts into deterministic card IR.",
    )
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="Validate the semantic catalog.")
    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate one deterministic card IR.",
    )
    generate_parser.add_argument("--concept", action="append", required=True)
    generate_parser.add_argument("--action", action="append", default=[])
    generate_parser.add_argument("--core", default="neutral")
    compare_parser = subparsers.add_parser(
        "compare",
        help="Run the deterministic 48-input semantic-physics comparison.",
    )
    compare_parser.add_argument("--experiment", type=Path, default=DEFAULT_EXPERIMENT)
    compare_parser.add_argument(
        "--embedding-cache",
        type=Path,
        default=DEFAULT_EMBEDDING_CACHE,
    )
    compare_parser.add_argument("--manual-only", action="store_true")
    compare_parser.add_argument("--output", type=Path)
    build_parser = subparsers.add_parser(
        "build-embeddings",
        help="Build a pinned offline embedding cache.",
    )
    build_parser.add_argument("--experiment", type=Path, default=DEFAULT_EXPERIMENT)
    build_parser.add_argument("--output", type=Path, default=DEFAULT_EMBEDDING_CACHE)
    build_parser.add_argument("--model-id", default=DEFAULT_MODEL_ID)
    build_parser.add_argument("--revision", default=DEFAULT_MODEL_REVISION)
    args = parser.parse_args()

    try:
        if args.command == "validate":
            catalog = load_catalog(args.catalog)
            print(
                "OK "
                f"version={catalog.version} "
                f"concepts={len(catalog.concepts)} "
                f"actions={len(catalog.actions)} "
                f"laws={len(catalog.laws)} "
                f"cores={len(catalog.cores)}"
            )
            return 0
        if args.command == "generate":
            catalog = load_catalog(args.catalog)
            card = generate_card(
                catalog,
                concept_ids=args.concept,
                action_ids=args.action,
                core_id=args.core,
            )
            print(json.dumps(card, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        config = load_experiment_config(args.experiment)
        if args.command == "build-embeddings":
            payload = build_embedding_cache(
                config,
                model_id=args.model_id,
                model_revision=args.revision,
            )
            write_embedding_cache(args.output, payload)
            print(
                "OK "
                f"model={payload['model']['id']} "
                f"revision={payload['model']['revision']} "
                f"entries={len(payload['entries'])} "
                f"dimension={payload['model']['dimension']} "
                f"digest={payload['digest']} "
                f"output={args.output}"
            )
            return 0
        embedding_cache = None
        if not args.manual_only:
            embedding_cache = load_embedding_cache(args.embedding_cache, config)
        report = run_comparison(config, embedding_cache)
        if args.output is None:
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        route_summaries = {
            route: payload["summary"] for route, payload in report["routes"].items()
        }
        print(
            "OK "
            f"version={config.version} "
            f"inputs={report['input_count']} "
            f"digest={report['digest']} "
            f"output={args.output}"
        )
        print(json.dumps(route_summaries, ensure_ascii=False, sort_keys=True))
        return 0
    except (
        CatalogError,
        EmbeddingCacheError,
        ExperimentError,
        GenerationError,
        OSError,
        json.JSONDecodeError,
    ) as error:
        parser.exit(2, f"error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
