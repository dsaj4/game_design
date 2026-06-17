from __future__ import annotations

import argparse
from pathlib import Path


CHECKS = [
    ("outline/outline.md exists", lambda root: (root / "outline" / "outline.md").exists()),
    ("outline/outline.json exists", lambda root: (root / "outline" / "outline.json").exists()),
    ("draft exists", lambda root: any((root / "drafts").glob("*-dossier.md")) if (root / "drafts").exists() else False),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True)
    args = parser.parse_args()

    root = Path(args.workspace).resolve()
    results: list[tuple[str, bool]] = []
    for name, check in CHECKS:
        results.append((name, check(root)))

    draft_text = ""
    drafts_dir = root / "drafts"
    if drafts_dir.exists():
        drafts = list(drafts_dir.glob("*-dossier.md"))
        if drafts:
            draft_text = drafts[0].read_text(encoding="utf-8")

    if draft_text:
        results.extend(
            [
                ("contains eight modules", all(f"模块{i}" in draft_text for i in range(1, 9))),
                ("contains evidence map", "## 证据地图" in draft_text),
                ("contains core loop diagram", "核心循环图" in draft_text and "```mermaid" in draft_text),
                ("contains system relation diagram", "系统关系图" in draft_text and draft_text.count("```mermaid") >= 2),
                ("contains project transfer", "## 对本项目的转化" in draft_text),
                ("contains unknowns", "## 未确认信息" in draft_text),
            ]
        )
    else:
        results.extend(
            [
                ("contains eight modules", False),
                ("contains evidence map", False),
                ("contains core loop diagram", False),
                ("contains system relation diagram", False),
                ("contains project transfer", False),
                ("contains unknowns", False),
            ]
        )

    checks_dir = root / "checks"
    checks_dir.mkdir(parents=True, exist_ok=True)
    rows = ["| Check | Result |", "| --- | --- |"]
    passed = 0
    for name, ok in results:
        passed += 1 if ok else 0
        rows.append(f"| {name} | {'PASS' if ok else 'NEEDS WORK'} |")
    report = "\n".join(
        [
            "# Phase 1 Check",
            "",
            f"- Passed: {passed} / {len(results)}",
            f"- Status: {'PASS' if passed == len(results) else 'NEEDS WORK'}",
            "",
            "\n".join(rows),
            "",
        ]
    )
    out_path = checks_dir / "phase1-check.md"
    out_path.write_text(report, encoding="utf-8", newline="\n")
    print(f"Wrote {out_path}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
