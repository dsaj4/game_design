from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any


LAB_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMPT = LAB_ROOT / "prompts" / "game-analysis-dossier.md"
DEFAULT_TEMPLATE = LAB_ROOT / "templates" / "game-analysis-dossier-template.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def sha256_short(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def bullet(items: list[str], fallback: str = "材料不足，待补充。") -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)


def resolve_from_pack(pack_path: Path, relative: str) -> Path:
    return (pack_path.parent / relative).resolve()


def collect_text_sources(pack: dict[str, Any], pack_path: Path) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    for source in pack.get("text_sources", []):
        path = resolve_from_pack(pack_path, source["path"])
        content = read_text(path)
        sources.append(
            {
                "path": source["path"],
                "role": source.get("role", ""),
                "description": source.get("description", ""),
                "content": content,
                "hash": sha256_short(content),
                "lines": str(content.count("\n") + 1),
            }
        )
    return sources


def build_evidence_table(pack: dict[str, Any], text_sources: list[dict[str, str]]) -> str:
    rows = ["| 证据 | 类型 | 说明 | 支撑模块 |", "| --- | --- | --- | --- |"]
    for source in text_sources:
        desc = source["description"] or source["role"]
        rows.append(f"| `{source['path']}` | 文本 | {desc} | 全局 / 核心循环 / 系统拆解 |")
    for image in pack.get("images", []):
        tags = ", ".join(image.get("evidence_tags", [])) or "未标注"
        rows.append(f"| `{image['path']}` | 图片 | {image['caption']} | {tags} |")
    return "\n".join(rows)


def build_image_evidence(pack: dict[str, Any]) -> str:
    chunks: list[str] = []
    for index, image in enumerate(pack.get("images", []), start=1):
        chunks.append(f"### 图片 {index}: `{image['path']}`")
        chunks.append("")
        chunks.append(f"- 说明：{image['caption']}")
        tags = ", ".join(image.get("evidence_tags", [])) or "未标注"
        chunks.append(f"- 证据标签：{tags}")
        chunks.append("- 观察点：")
        chunks.append(bullet(as_list(image.get("observations"))))
        chunks.append("")
    return "\n".join(chunks).rstrip()


def build_analysis_packet(pack: dict[str, Any], pack_path: Path, text_sources: list[dict[str, str]]) -> str:
    project = pack["project"]
    prompt = read_text(DEFAULT_PROMPT)
    template = read_text(DEFAULT_TEMPLATE)
    today = dt.date.today().isoformat()

    source_blocks: list[str] = []
    for source in text_sources:
        source_blocks.append(f"## 文本材料：`{source['path']}`")
        source_blocks.append("")
        source_blocks.append(f"- 角色：{source['role']}")
        source_blocks.append(f"- 说明：{source['description']}")
        source_blocks.append(f"- 行数：{source['lines']}")
        source_blocks.append(f"- 哈希：`{source['hash']}`")
        source_blocks.append("")
        source_blocks.append("```md")
        source_blocks.append(source["content"].rstrip())
        source_blocks.append("```")
        source_blocks.append("")

    return "\n".join(
        [
            f"# {project['game_name']}游戏拆解任务包",
            "",
            "## 任务元信息",
            "",
            f"- 生成日期：{today}",
            f"- 状态：{project['status']}",
            f"- 拆解范围：{project['analysis_scope']}",
            f"- 素材包：`{pack_path.name}`",
            f"- 来源备注：{project.get('source_note', '未填写')}",
            "",
            "## 目标问题",
            "",
            bullet(as_list(project.get("target_questions"))),
            "",
            "## 写作提示词",
            "",
            prompt.rstrip(),
            "",
            "## 图片证据表",
            "",
            build_image_evidence(pack),
            "",
            "## 文本材料",
            "",
            "\n".join(source_blocks).rstrip(),
            "",
            "## 输出模板",
            "",
            "```md",
            template.rstrip(),
            "```",
            "",
        ]
    )


def build_draft(pack: dict[str, Any], text_sources: list[dict[str, str]]) -> str:
    project = pack["project"]
    seed = pack.get("draft_seed", {})
    today = dt.date.today().isoformat()
    source_names = ", ".join(f"`{source['path']}`" for source in text_sources)
    image_names = ", ".join(f"`{image['path']}`" for image in pack.get("images", []))
    core_loop = seed.get(
        "core_loop_mermaid",
        "flowchart LR\n    Enter[进入游戏] --> Action[核心行为]\n    Action --> Output[产出]\n    Output --> Spend[消耗]\n    Spend --> Growth[成长]\n    Growth --> Return[回流]\n    Return --> Enter",
    )
    system_graph = seed.get(
        "system_mermaid",
        "flowchart TB\n    Combat[战斗系统]\n    Resource[资源系统]\n    Growth[成长系统]\n    Content[内容系统]\n    Combat --> Resource\n    Resource --> Growth\n    Growth --> Combat\n    Content --> Combat",
    )

    return "\n".join(
        [
            f"# {project['game_name']}游戏拆解稿",
            "",
            "## 元信息",
            "",
            f"- 状态：{project['status']}",
            f"- 拆解范围：{project['analysis_scope']}",
            f"- 材料来源：文本 {source_names}；图片 {image_names}",
            f"- 最后更新：{today}",
            "",
            "## 目标问题",
            "",
            bullet(as_list(project.get("target_questions"))),
            "",
            "## 拆解结论摘要",
            "",
            bullet(as_list(seed.get("summary"))),
            "",
            "## 证据地图",
            "",
            build_evidence_table(pack, text_sources),
            "",
            "## 模块1：游戏核心定位、基础信息、商业大盘复盘",
            "",
            "### 核心定位",
            "",
            seed.get("positioning", "材料不足，待补充。"),
            "",
            "### 商业与市场表现",
            "",
            "当前素材未提供可核验商业数据。本阶段不编写流水、留存、评分或榜单结论。",
            "",
            "### 对本项目的启示",
            "",
            bullet(as_list(seed.get("project_transfer"))[:2]),
            "",
            "## 模块2：全局玩家体验与底层设计目标",
            "",
            "### 全链路体感",
            "",
            seed.get("experience", "材料不足，待补充。"),
            "",
            "### 情绪价值",
            "",
            "当前样例重点观察策略规划、组合触发、资源取舍和战斗反馈带来的掌控感。",
            "",
            "### 对本项目的启示",
            "",
            bullet(as_list(seed.get("project_transfer"))[2:4]),
            "",
            "## 模块3：核心玩法循环",
            "",
            "### 核心循环图",
            "",
            "```mermaid",
            core_loop.rstrip(),
            "```",
            "",
            "### 逐环节拆解",
            "",
            bullet(as_list(seed.get("core_loop_notes"))),
            "",
            "### 对本项目的启示",
            "",
            bullet(as_list(seed.get("project_transfer"))[4:5]),
            "",
            "## 模块4：全链路游戏架构拆解",
            "",
            "### 系统关系图",
            "",
            "```mermaid",
            system_graph.rstrip(),
            "```",
            "",
            "### 系统拆分",
            "",
            bullet(as_list(seed.get("architecture_notes"))),
            "",
            "### 对本项目的启示",
            "",
            bullet(as_list(seed.get("project_transfer"))[5:6]),
            "",
            "## 模块5：内容与关卡体系",
            "",
            "### 节奏判断",
            "",
            bullet(as_list(seed.get("content_notes"))),
            "",
            "### 对本项目的启示",
            "",
            "第一阶段应先验证单局战斗与组合学习曲线，不急于扩展完整关卡和长线内容系统。",
            "",
            "## 模块6：数值体系与经济资源闭环",
            "",
            "### 闭环判断",
            "",
            bullet(as_list(seed.get("economy_notes"))),
            "",
            "### 对本项目的启示",
            "",
            "费用和组合触发条件应作为第一阶段核心变量，先验证取舍压力是否清楚，再考虑成长和商业资源。",
            "",
            "## 模块7：叙事体系、角色 IP 与视听包装",
            "",
            "### 叙事与视觉判断",
            "",
            bullet(as_list(seed.get("narrative_notes"))),
            "",
            "### 对本项目的启示",
            "",
            "核心卡身份可以通过视觉锚点和战斗反馈强化，但第一阶段不应依赖完整世界观才能让玩法成立。",
            "",
            "## 模块8：优劣复盘与可落地优化方案",
            "",
            "### 可复用亮点",
            "",
            bullet(as_list(seed.get("strengths"))),
            "",
            "### 真实短板",
            "",
            bullet(as_list(seed.get("weaknesses"))),
            "",
            "### 优化方案",
            "",
            "- 若组合触发条件过多，优先减少响应窗口和状态层级，保证玩家能预测下一步收益。",
            "- 若资源压力不明显，优先调整费用刷新与关键牌消耗，而不是增加更多资源类型。",
            "",
            "## 对本项目的转化",
            "",
            "### 可借鉴结构",
            "",
            bullet(as_list(seed.get("project_transfer"))),
            "",
            "### 可转化设计假设",
            "",
            bullet(as_list(seed.get("hypotheses"))),
            "",
            "### 当前状态",
            "",
            "Research / Prototype Lab。该拆解只用于验证分析工作流，不进入 Accepted。",
            "",
            "## 未确认信息",
            "",
            bullet(as_list(seed.get("unknowns")), fallback="暂无。"),
            "",
        ]
    )


def build_quality_check(pack: dict[str, Any], draft: str, text_sources: list[dict[str, str]]) -> str:
    seed = pack.get("draft_seed", {})
    checks = [
        ("至少 1 个文本材料", len(text_sources) >= 1),
        ("至少 1 个图片材料", len(pack.get("images", [])) >= 1),
        ("八大模块齐全", all(f"模块{i}" in draft for i in range(1, 9))),
        ("包含核心循环图", "核心循环图" in draft and "```mermaid" in draft),
        ("包含系统关系图", "系统关系图" in draft and draft.count("```mermaid") >= 2),
        ("包含证据地图", "## 证据地图" in draft),
        ("包含项目转化", "## 对本项目的转化" in draft),
        ("至少 1 条设计假设", len(as_list(seed.get("hypotheses"))) >= 1),
        ("未确认信息单独列出", "## 未确认信息" in draft),
    ]
    passed = sum(1 for _, ok in checks if ok)
    rows = ["| 检查项 | 结果 |", "| --- | --- |"]
    for name, ok in checks:
        rows.append(f"| {name} | {'PASS' if ok else 'NEEDS WORK'} |")

    return "\n".join(
        [
            f"# {pack['project']['game_name']}质量检查",
            "",
            f"- 通过：{passed} / {len(checks)}",
            f"- 判定：{'可进入人工评审' if passed == len(checks) else '需要补材料或补结构'}",
            "",
            "\n".join(rows),
            "",
            "## 下一步建议",
            "",
            "- 用真实游戏截图替换示例图，检查截图是否能支撑核心循环和系统联动判断。",
            "- 把视频转写或人工游玩记录补进文本材料，减少纯推断内容。",
            "- 若要进入正式研究案例，再按 `research/08-analysis-quality-system/review-rubric.md` 打分。",
            "",
        ]
    )


def write_output(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a game analysis packet from image and text materials.")
    parser.add_argument("--pack", required=True, help="Path to materialpack.json")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--check", action="store_true", help="Return non-zero when quality gates fail")
    args = parser.parse_args()

    pack_path = Path(args.pack).resolve()
    out_dir = Path(args.out).resolve()
    pack = load_json(pack_path)
    text_sources = collect_text_sources(pack, pack_path)
    slug = pack["project"]["slug"]

    packet = build_analysis_packet(pack, pack_path, text_sources)
    draft = build_draft(pack, text_sources)
    quality = build_quality_check(pack, draft, text_sources)

    packet_path = out_dir / f"{slug}-analysis-packet.md"
    draft_path = out_dir / f"{slug}-draft.md"
    quality_path = out_dir / f"{slug}-quality-check.md"

    write_output(packet_path, packet)
    write_output(draft_path, draft)
    write_output(quality_path, quality)

    print(f"Wrote {packet_path}")
    print(f"Wrote {draft_path}")
    print(f"Wrote {quality_path}")

    if args.check and "NEEDS WORK" in quality:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
