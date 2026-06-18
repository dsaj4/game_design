from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has_content(value: Any) -> bool:
    return isinstance(value, list) and any(str(item).strip() for item in value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True)
    args = parser.parse_args()

    root = Path(args.workspace).resolve()
    audit_path = root / "visual" / "visual-audit.json"
    if not audit_path.exists():
        raise SystemExit(f"ERROR: visual audit not found: {audit_path}")

    audit = load_json(audit_path)
    frames = audit.get("frames", [])
    results: list[tuple[str, bool]] = [
        ("visual-audit.json exists", True),
        ("has frames", bool(frames)),
    ]
    audited = [frame for frame in frames if frame.get("status") == "audited"]
    needs_review = [frame for frame in frames if frame.get("status") == "needs-review"]
    useful = [
        frame
        for frame in audited
        if has_content(frame.get("visible_elements"))
        or has_content(frame.get("ocr_candidates"))
        or has_content(frame.get("gameplay_observations"))
        or has_content(frame.get("ui_affordances"))
        or has_content(frame.get("state_changes"))
    ]
    illustrated = [frame for frame in frames if frame.get("illustration_candidate")]
    results.extend(
        [
            ("has audited or needs-review frames", bool(audited or needs_review)),
            ("audited frames contain visual observations", bool(useful)),
            ("has module assignments", all(frame.get("supports_modules") for frame in frames)),
            ("has illustration candidates", bool(illustrated)),
        ]
    )

    rows = ["| Check | Result |", "| --- | --- |"]
    passed = 0
    for name, ok in results:
        passed += 1 if ok else 0
        rows.append(f"| {name} | {'PASS' if ok else 'NEEDS WORK'} |")
    report = "\n".join(
        [
            "# Visual Audit Check",
            "",
            f"- Audited frames: {len(audited)}",
            f"- Needs-review frames: {len(needs_review)}",
            f"- Illustration candidates: {len(illustrated)}",
            f"- Passed: {passed} / {len(results)}",
            f"- Status: {'PASS' if passed == len(results) else 'NEEDS WORK'}",
            "",
            "\n".join(rows),
            "",
        ]
    )
    checks_dir = root / "checks"
    checks_dir.mkdir(parents=True, exist_ok=True)
    out_path = checks_dir / "visual-audit-check.md"
    out_path.write_text(report, encoding="utf-8", newline="\n")
    print(f"Wrote {out_path}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
