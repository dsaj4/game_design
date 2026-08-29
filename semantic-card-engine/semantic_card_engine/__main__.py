from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .engine import CatalogError, GenerationError, generate_card, load_catalog


DEFAULT_CATALOG = Path(__file__).parents[1] / "data" / "catalog.json"


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
    args = parser.parse_args()

    try:
        catalog = load_catalog(args.catalog)
        if args.command == "validate":
            print(
                "OK "
                f"version={catalog.version} "
                f"concepts={len(catalog.concepts)} "
                f"actions={len(catalog.actions)} "
                f"laws={len(catalog.laws)} "
                f"cores={len(catalog.cores)}"
            )
            return 0
        card = generate_card(
            catalog,
            concept_ids=args.concept,
            action_ids=args.action,
            core_id=args.core,
        )
        print(json.dumps(card, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (CatalogError, GenerationError, OSError, json.JSONDecodeError) as error:
        parser.exit(2, f"error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
