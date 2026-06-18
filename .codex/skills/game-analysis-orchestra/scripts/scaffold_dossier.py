from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_table(outline: dict[str, Any]) -> str:
    rows = ["| 证据 | 类型 | 说明 | 支撑模块 |", "| --- | --- | --- | --- |"]
    for item in outline.get("evidence_map", []):
        rows.append(f"| {item['id']}: `{item['path']}` | {item['type']} | {item.get('summary', '')} | {', '.join(item.get('modules', []))} |")
    return "\n".join(rows)


def visual_candidates(outline: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        item
        for item in outline.get("visual_evidence", [])
        if item.get("illustration_candidate") and item.get("status") in {"audited", "needs-review"}
    ]


def image_path_for_dossier(item: dict[str, Any], out_dir: Path) -> str:
    absolute = item.get("source_path_absolute")
    if absolute:
        try:
            return Path(os.path.relpath(Path(absolute), out_dir)).as_posix()
        except ValueError:
            return absolute
    return item["path"]


def visual_gallery(outline: dict[str, Any], out_dir: Path) -> list[str]:
    candidates = visual_candidates(outline)
    if not candidates:
        return [
            "## 图文证据",
            "",
            "- 暂无已核验的配图候选；若素材包含截图，请先完成 `visual/visual-audit.json`。",
            "",
        ]
    lines = ["## 图文证据", ""]
    for item in candidates[:10]:
        caption = item.get("caption_for_dossier") or item.get("summary") or item["id"]
        image_path = image_path_for_dossier(item, out_dir)
        lines.extend([f"![{item['id']} {caption}]({image_path})", "", f"{item['id']}：{caption}", ""])
    return lines


def module_block(module: dict[str, Any]) -> list[str]:
    title = module["title"]
    number = module["id"].replace("module-", "")
    lines = [f"## 模块{number}：{title}", "", "### 结论", "", module.get("claim", "待补写。"), ""]
    if module["id"] == "module-3":
        lines.extend(
            [
                "### 核心循环图",
                "",
                "```mermaid",
                "flowchart LR",
                "    Enter[进入游戏] --> Action[核心行为]",
                "    Action --> Output[产出]",
                "    Output --> Cost[消耗/约束]",
                "    Cost --> Feedback[反馈]",
                "    Feedback --> Return[回流]",
                "    Return --> Enter",
                "```",
                "",
            ]
        )
    if module["id"] == "module-4":
        lines.extend(
            [
                "### 系统关系图",
                "",
                "```mermaid",
                "flowchart TB",
                "    Core[核心系统] --> Action[玩家行动]",
                "    Action --> Resource[资源/约束]",
                "    Resource --> Feedback[反馈]",
                "    Feedback --> Core",
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "### 证据",
            "",
            "\n".join(f"- {e}" for e in module.get("evidence", [])) or "- 材料不足。",
            "",
            "### 对本项目的启示",
            "",
            "- 待补写。",
            "",
        ]
    )
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", required=True)
    parser.add_argument("--outline", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    pack = load_json(Path(args.pack).resolve())
    outline = load_json(Path(args.outline).resolve())
    out_dir = Path(args.out).resolve() / "drafts"
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = pack["project"]["slug"]

    lines = [
        f"# {outline['game_name']} 游戏拆解稿",
        "",
        "## 元信息",
        "",
        f"- 状态：{pack['project']['status']}",
        f"- 拆解范围：{pack['project']['analysis_scope']}",
        f"- 最后更新：{dt.date.today().isoformat()}",
        "",
        "## 目标问题",
        "",
        "\n".join(f"- {q}" for q in outline.get("target_questions", [])),
        "",
        "## 拆解结论摘要",
        "",
        "- 待根据分模块写作补写。",
        "",
        "## 证据地图",
        "",
        evidence_table(outline),
        "",
    ]
    lines.extend(visual_gallery(outline, out_dir))
    for module in outline.get("modules", []):
        lines.extend(module_block(module))
    lines.extend(
        [
            "## 对本项目的转化",
            "",
            "### 可借鉴结构",
            "",
            "- 待补写。",
            "",
            "### 可转化设计假设",
            "",
            "- H：待补写。",
            "",
            "### 当前状态",
            "",
            "Research / Prototype Lab",
            "",
            "## 未确认信息",
            "",
            "- 待补写。",
            "",
        ]
    )

    out_path = out_dir / f"{slug}-dossier.md"
    out_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
