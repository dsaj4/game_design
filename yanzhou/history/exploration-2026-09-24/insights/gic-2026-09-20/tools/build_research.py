"""Rebuild GIC provenance and authored case cards from an explicit local source export."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + '\n', encoding='utf-8', newline='\n')


def save_json(path: Path, value: object) -> None:
    write(path, json.dumps(value, ensure_ascii=False, indent=2))


def clean(value: str) -> str:
    return value.replace('|', '／').replace('\n', ' ')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--commit', required=True)
    args = parser.parse_args()
    records = json.loads(args.source.read_text(encoding='utf-8'))['records']
    reviews = json.loads((ROOT / 'review-data.json').read_text(encoding='utf-8'))['reviews']
    manifest_path = ROOT / 'source-manifest.json'
    old_manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    retrieved = old_manifest.get('retrieved_at', datetime.fromtimestamp(args.source.stat().st_mtime, timezone.utc).isoformat())
    matched = {}
    game_manifest = []
    notes = ['# 逐款来源笔记', '', 'Project ID：game-002-optimization。日期：2026-09-20。以下为对 GIC 描述的自写转述，未以原图、试玩或官方规则书独立核实。', '', '每个 T 编号对应一种游戏；同站多档案合并，不增加独立来源数量。原文副本仅存在本地 .raw，不进入 Git。', '']
    ledger = ['# 24款逐案处理索引', '', '研究状态：Research / Provisional。处理结果是研究决定，不是玩法采纳。完整机制、差异和反例见每款研究卡。', '', '| 顺序 | 游戏 | 档案数 | 研究处理／更新 | 去向 |', '| --- | --- | --- | --- | --- |']
    for i, review in enumerate(reviews, 1):
        selected = [r for r in records if re.search(review['pattern'], r['archive_id'])]
        if not selected:
            raise ValueError(f'No archive matched: {review["name"]}')
        for record in selected:
            if record['archive_id'] in matched:
                raise ValueError(f'Duplicate assignment: {record["archive_id"]}')
            matched[record['archive_id']] = f'T{i:02d}'
        filename = f'{i:02d}-{review["slug"]}.md'
        sources = '\n'.join(f'- [{r["archive_id"]}]({r["archive_image_url"]})' for r in selected)
        destinations = '、'.join(review['directions']) or '研究后置／仅方法参考'
        card = f'''# T{i:02d} · {review['name']}

Project ID：`game-002-optimization`。状态：`Research / Provisional`。日期：2026-09-20。

## 来源与证据边界

来自 [GIC 档案馆](https://www.9cards.cn/gic/) 的 {len(selected)} 份记录；下列为该站原图地址，可按档案 ID 在站内检索。读取依据为公开网页内的 innovation_cn/en 正文；同站多记录不等于独立交叉验证。未观看视频、未玩原作、未核实当前版本或商业表现。

{sources}

## 吸收：来源实际描述了什么

{review['fact']}

**输入—行动—输出—回流（本轮结构归纳）：**{review['loop']}。

**玩家为什么可能在意（推断）：**{review['insight']}

## 适配：与 RC1 的关系

{review['fit']}

**保留结构：**{review['transfer']}

**不迁移／雷同与范围风险：**{review['reject']}

## 更新决定

{review['update']}

去向：{destinations}。这是候选形成过程，不是 Qualified GDD Material 或正式 Evaluation。

## 未确认信息与下一步

{review['unknown']}

下一步按[方向比较与验证](../directions.md)检查实际取舍；若需要准确复现原作，先补官方规则与当前版本证据，不用本档案替代规则书。

[返回逐案索引](../case-index.md) · [流程](../workflow.md)
'''
        write(ROOT / 'cases' / filename, card)
        notes.extend([f'## T{i:02d} · {review["name"]}', '', review['fact'], '', sources, ''])
        ledger.append(f'| {i:02d} | [{review["name"]}](cases/{filename}) | {len(selected)} | {clean(review["update"])} | {destinations} |')
        game_manifest.append({'evidence_id': f'T{i:02d}', 'name': review['name'], 'case': f'cases/{filename}', 'archive_ids': [r['archive_id'] for r in selected]})
    write(ROOT / 'source-notes.md', '\n'.join(notes))
    write(ROOT / 'case-index.md', '\n'.join(ledger))
    inventory = ['# GIC 全目录登记', '', f'抓取日期：2026-09-20。共 {len(records)} 份档案。标题/创新摘要已用于范围筛选；24款共 {len(matched)} 份正文进入深读，其余只做目录级筛选，不声称逐款完整评估。', '', '同游戏可有多个 ID，不能把档案数当作游戏数。名称保留站点原写法；标题拼写差异不自动合并为新游戏。只登记元数据与链接，不提交第三方正文和图片。', '', '| # | 档案 ID／原图 | 游戏 | 类别 | GIC年份 | 处理 |', '| --- | --- | --- | --- | --- | --- |']
    for i, r in enumerate(records, 1):
        inventory.append(f'| {i} | [{clean(r["archive_id"])}]({r["archive_image_url"]}) | {clean(r["name_cn"] or r["name_en"])} | {r["game_type_key"]} | {r["gic_year"]} | {matched.get(r["archive_id"], "目录筛选；未完整分析")} |')
    write(ROOT / 'catalog.md', '\n'.join(inventory))
    baseline_paths = ['workspaces/game-002/game-design-workflow/gdd/GDD-2026-09-14-yanzhou-full-game.md', 'workspaces/game-002/game-design-workflow/gdd/yanzhou-rc1/02-grammar-and-configuration.md', 'workspaces/game-002/game-design-workflow/gdd/yanzhou-rc1/04-elements-and-environment.md']
    manifest = {'version':'1.0', 'project_id':'game-002-optimization', 'source_project_id':'game-002', 'source_url':'https://www.9cards.cn/gic/', 'retrieved_at':retrieved, 'source_export_sha256':digest(args.source), 'source_commit':args.commit, 'baseline_version':'GDD-G002-FULL-001 / 1.0 RC1', 'baseline_scope':'用户指定入口及02构句/04元素正文，02按有关条款读取，未递归检索历史素材', 'baseline_files':[{'path':p,'sha256':digest(REPO / p)} for p in baseline_paths], 'archive_count':len(records), 'selected_game_count':len(reviews), 'selected_archive_count':len(matched), 'evidence_kind':'secondary archive text; no gameplay testing', 'snapshot_policy':'third-party full text and image downloads remain ignored under .raw', 'games':game_manifest, 'archives':[{'id':r['archive_id'], 'name_cn':r['name_cn'], 'name_en':r['name_en'], 'source_url':r['archive_image_url'], 'text_sha256':hashlib.sha256((r['innovation_cn']+'\n'+r['innovation_en']).encode('utf-8')).hexdigest(), 'review':matched.get(r['archive_id'],'index-only')} for r in records]}
    save_json(manifest_path, manifest)
    pack = {'version':'1.0','project':{'game_name':'GIC 24款创新机制与《言咒》迁移研究','slug':'gic-yanzhou','analysis_scope':'只分析来源可支持的机制结构及RC1适配；不写新GDD、不推定原作完整规则或商业表现','status':'Research / Provisional','target_questions':['哪些结构真正增加实体词卡的机会成本？','哪些改变能保留战前编排与自动执行？','五个方向如何最小化验证并独立决定去留？'],'source_note':'外部检索由用户明确授权；游戏分析技能仅用于证据与八模块组织，技能中的旧项目背景不适用。'},'text_sources':[{'path':'source-notes.md','role':'GIC公开档案的自写事实转述与逐条来源','description':'24款来源描述，T01–T24；原始文本哈希见source-manifest.json'},{'path':'../../../../'+baseline_paths[0],'role':'用户指定设计基线','description':'game-002全游戏GDD RC1；新玩法不得被视为既有规则'}],'images':[]}
    save_json(ROOT / 'materialpack.json', pack)
    print(json.dumps({'archives':len(records),'selected_games':len(reviews),'selected_archives':len(matched)},ensure_ascii=True))


if __name__ == '__main__':
    main()
