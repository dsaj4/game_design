from __future__ import annotations

import argparse
from pathlib import Path


CHECKS = [
    ("outline/outline.md exists", lambda root: (root / "outline" / "outline.md").exists()),
    ("outline/outline.json exists", lambda root: (root / "outline" / "outline.json").exists()),
    ("draft exists", lambda root: any((root / "drafts").glob("*-dossier.md")) if (root / "drafts").exists() else False),
]


def visual_audit_expected(root: Path) -> bool:
    return (root / "visual" / "visual-audit.json").exists()


def contains_any(text: str, candidates: list[str]) -> bool:
    lowered = text.lower()
    return any(candidate.lower() in lowered for candidate in candidates)


def contains_eight_modules(text: str) -> bool:
    chinese = all(f"模块{i}" in text for i in range(1, 9))
    english = all(f"module {i}" in text.lower() or f"module-{i}" in text.lower() for i in range(1, 9))
    return chinese or english


def has_chinese_body(text: str) -> bool:
    cjk_count = sum(1 for char in text if "\u4e00" <= char <= "\u9fff")
    return cjk_count >= 200


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
                ("contains eight modules", contains_eight_modules(draft_text)),
                ("contains evidence map", contains_any(draft_text, ["## 证据地图", "## Evidence Map"])),
                (
                    "contains visual evidence section",
                    contains_any(draft_text, ["## 图文证据", "## Visual Evidence", "## Illustrated Evidence"]) if visual_audit_expected(root) else True,
                ),
                ("contains core loop diagram", contains_any(draft_text, ["核心循环图", "Core Loop"]) and "```mermaid" in draft_text),
                (
                    "contains system relation diagram",
                    contains_any(draft_text, ["系统关系图", "System Relation", "System Architecture"]) and draft_text.count("```mermaid") >= 2,
                ),
                ("uses Simplified Chinese body", has_chinese_body(draft_text)),
                ("contains project transfer", contains_any(draft_text, ["## 对本项目的转化", "## Project Transfer", "## Transfer To This Project"])),
                ("contains unknowns", contains_any(draft_text, ["## 未确认信息", "## Unknowns", "## Unconfirmed Information"])),
            ]
        )
    else:
        results.extend(
            [
                ("contains eight modules", False),
                ("contains evidence map", False),
                ("contains core loop diagram", False),
                ("contains system relation diagram", False),
                ("uses Simplified Chinese body", False),
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
