from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


MODULES = [
    ("module-1", "游戏核心定位、基础信息、商业大盘复盘", "medium"),
    ("module-2", "全局玩家体验与底层设计目标", "high"),
    ("module-3", "核心玩法循环", "high"),
    ("module-4", "全链路游戏架构拆解", "high"),
    ("module-5", "内容与关卡体系", "medium"),
    ("module-6", "数值体系与经济资源闭环", "medium"),
    ("module-7", "叙事体系、角色 IP 与视听包装", "low"),
    ("module-8", "优劣复盘与可落地优化方案", "high"),
]


TAG_MODULE_HINTS = {
    "core": "module-3",
    "core-loop": "module-3",
    "核心循环": "module-3",
    "combat": "module-4",
    "战斗系统": "module-4",
    "system": "module-4",
    "economy": "module-6",
    "费用取舍": "module-6",
    "content": "module-5",
    "narrative": "module-7",
    "ui": "module-7",
    "组合规则": "module-4",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_evidence(pack: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = []
    for index, source in enumerate(pack.get("text_sources", []), start=1):
        evidence.append(
            {
                "id": f"T{index}",
                "type": "text",
                "path": source["path"],
                "summary": source.get("description") or source.get("role", ""),
                "modules": ["module-2", "module-3", "module-4"],
            }
        )
    for index, image in enumerate(pack.get("images", []), start=1):
        modules = set()
        for tag in image.get("evidence_tags", []):
            modules.add(TAG_MODULE_HINTS.get(tag, "module-4"))
        if not modules:
            modules.add("module-4")
        evidence.append(
            {
                "id": f"I{index}",
                "type": "image",
                "path": image["path"],
                "summary": image.get("caption", ""),
                "observations": image.get("observations", []),
                "modules": sorted(modules),
            }
        )
    return evidence


def write_outline_md(path: Path, outline: dict[str, Any]) -> None:
    rows = ["| 模块 | 核心判断 | 证据 | 未确认信息 | 优先级 |", "| --- | --- | --- | --- | --- |"]
    for module in outline["modules"]:
        rows.append(
            f"| {module['title']} | {module['claim']} | {', '.join(module['evidence'])} | {', '.join(module['open_questions'])} | {module['write_priority']} |"
        )
    evidence_rows = ["| ID | 类型 | 来源 | 说明 | 支撑模块 |", "| --- | --- | --- | --- | --- |"]
    for item in outline["evidence_map"]:
        evidence_rows.append(
            f"| {item['id']} | {item['type']} | `{item['path']}` | {item['summary']} | {', '.join(item['modules'])} |"
        )
    content = "\n".join(
        [
            f"# {outline['game_name']} 拆解大纲",
            "",
            "## 总论点",
            "",
            outline["thesis"],
            "",
            "## 目标问题",
            "",
            "\n".join(f"- {q}" for q in outline["target_questions"]),
            "",
            "## 证据地图",
            "",
            "\n".join(evidence_rows),
            "",
            "## 模块规划",
            "",
            "\n".join(rows),
            "",
            "## 图示计划",
            "",
            "- 核心循环图：模块3，用于解释输入、行动、产出、消耗、反馈和回流。",
            "- 系统关系图：模块4，用于解释系统联动。",
            "",
        ]
    )
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    pack_path = Path(args.pack).resolve()
    out_dir = Path(args.out).resolve() / "outline"
    out_dir.mkdir(parents=True, exist_ok=True)
    pack = load_json(pack_path)
    project = pack["project"]
    evidence = build_evidence(pack)

    modules = []
    for module_id, title, priority in MODULES:
        module_evidence = [item["id"] for item in evidence if module_id in item["modules"]]
        modules.append(
            {
                "id": module_id,
                "title": title,
                "claim": "待根据证据补写。",
                "evidence": module_evidence,
                "open_questions": ["材料不足时补写未确认信息。"],
                "write_priority": priority,
            }
        )

    outline = {
        "game_name": project["game_name"],
        "slug": project["slug"],
        "scope": project["analysis_scope"],
        "target_questions": project["target_questions"],
        "thesis": "待根据素材包补写总论点。",
        "evidence_map": evidence,
        "modules": modules,
        "diagrams": [
            {"type": "core_loop", "module": "module-3", "purpose": "解释玩家输入、行动、产出、消耗、反馈和回流。"},
            {"type": "system_relation", "module": "module-4", "purpose": "解释主要系统之间的输入、输出和反馈关系。"},
        ],
    }

    (out_dir / "outline.json").write_text(json.dumps(outline, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    write_outline_md(out_dir / "outline.md", outline)
    print(f"Wrote {out_dir / 'outline.json'}")
    print(f"Wrote {out_dir / 'outline.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
