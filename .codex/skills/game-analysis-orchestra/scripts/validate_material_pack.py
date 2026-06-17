from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def load_pack(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"material pack not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", required=True)
    args = parser.parse_args()

    pack_path = Path(args.pack).resolve()
    pack = load_pack(pack_path)
    project = pack.get("project")
    if not isinstance(project, dict):
        fail("missing object: project")

    required = ["game_name", "slug", "analysis_scope", "status", "target_questions"]
    for key in required:
        if not project.get(key):
            fail(f"missing project.{key}")
    if not isinstance(project.get("target_questions"), list) or not project["target_questions"]:
        fail("project.target_questions must be a non-empty array")

    text_sources = pack.get("text_sources", [])
    images = pack.get("images", [])
    if not text_sources and not images:
        fail("need at least one text source or one image")

    for source in text_sources:
        rel = source.get("path")
        if not rel:
            fail("text source missing path")
        path = (pack_path.parent / rel).resolve()
        if not path.exists():
            fail(f"text source not found: {path}")

    for image in images:
        rel = image.get("path")
        if not rel:
            fail("image missing path")
        path = (pack_path.parent / rel).resolve()
        if not path.exists():
            fail(f"image not found: {path}")
        if not image.get("observations"):
            fail(f"image missing observations: {rel}")

    print(f"OK: {pack_path}")
    print(f"Game: {project['game_name']}")
    print(f"Text sources: {len(text_sources)}")
    print(f"Images: {len(images)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
