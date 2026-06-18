from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TAG_MODULE_HINTS = {
    "core": "module-3",
    "core-loop": "module-3",
    "combat": "module-4",
    "combat-system": "module-4",
    "system": "module-4",
    "economy": "module-6",
    "content": "module-5",
    "progression": "module-5",
    "narrative": "module-7",
    "ui": "module-7",
    "deckbuilding": "module-4",
    "risk": "module-8",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def module_hints(tags: list[str]) -> list[str]:
    modules = {TAG_MODULE_HINTS.get(tag, "module-4") for tag in tags}
    return sorted(modules or {"module-4"})


def build_audit(pack: dict[str, Any]) -> dict[str, Any]:
    frames = []
    for index, image in enumerate(pack.get("images", []), start=1):
        image_id = f"I{index}"
        frames.append(
            {
                "id": f"V{index}",
                "image_id": image_id,
                "path": image["path"],
                "source_caption": image.get("caption", ""),
                "source_observations": image.get("observations", []),
                "status": "not-audited",
                "direct_image_read": False,
                "reader": "",
                "confidence": "low",
                "visible_elements": [],
                "ocr_candidates": [],
                "gameplay_observations": [],
                "ui_affordances": [],
                "state_changes": [],
                "supports_modules": module_hints(image.get("evidence_tags", [])),
                "conflicts": [],
                "illustration_candidate": False,
                "caption_for_dossier": "",
            }
        )
    return {
        "version": "0.1",
        "game_name": pack["project"]["game_name"],
        "slug": pack["project"]["slug"],
        "method": "Fill with multimodal model or manual visual inspection. Do not treat source captions as independent visual reading.",
        "frames": frames,
    }


def write_md(path: Path, audit: dict[str, Any]) -> None:
    rows = [
        "| ID | Image | Status | Confidence | Visible/gameplay notes | Modules | Illustration |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for frame in audit["frames"]:
        notes = "; ".join(frame.get("gameplay_observations", [])) or "not audited yet"
        rows.append(
            f"| {frame['id']} ({frame['image_id']}) | `{frame['path']}` | {frame['status']} | {frame['confidence']} | {notes} | {', '.join(frame['supports_modules'])} | {frame['illustration_candidate']} |"
        )
    content = "\n".join(
        [
            f"# {audit['game_name']} Visual Audit",
            "",
            "This file records independent visual reading of screenshots/keyframes. Source captions are useful hints, but they are not enough to mark a frame audited.",
            "",
            "## Frame Audit",
            "",
            "\n".join(rows),
            "",
        ]
    )
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    pack = load_json(Path(args.pack).resolve())
    out_dir = Path(args.out).resolve() / "visual"
    out_dir.mkdir(parents=True, exist_ok=True)
    audit = build_audit(pack)
    json_path = out_dir / "visual-audit.json"
    md_path = out_dir / "visual-audit.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    write_md(md_path, audit)
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
