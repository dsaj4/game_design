"""Check provenance coverage, local links, UTF-8 and unchanged design inputs."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
PROJECT = ROOT.parents[1]


def main() -> int:
    manifest = json.loads((ROOT / 'source-manifest.json').read_text(encoding='utf-8'))
    reviews = json.loads((ROOT / 'review-data.json').read_text(encoding='utf-8'))['reviews']
    cases = sorted((ROOT / 'cases').glob('*.md'))
    checks = []
    checks.append(('24款独立研究卡', len(cases) == len(reviews) == manifest['selected_game_count'] == 24))
    ids = [archive_id for game in manifest['games'] for archive_id in game['archive_ids']]
    checks.append(('40份深读档案唯一归属', len(ids) == len(set(ids)) == manifest['selected_archive_count'] == 40))
    catalog_ids = {r['id'] for r in manifest['archives']}
    checks.append(('224份目录与深读来源闭合', len(catalog_ids) == manifest['archive_count'] == 224 and set(ids) <= catalog_ids))
    checks.append(('深读档案逐条登记一致', {r['id'] for r in manifest['archives'] if r['review'] != 'index-only'} == set(ids)))
    unchanged = all(hashlib.sha256((REPO / f['path']).read_bytes()).hexdigest() == f['sha256'] for f in manifest['baseline_files'])
    checks.append(('3份设计来源文件与本轮哈希一致', unchanged))
    files = [p for p in ROOT.rglob('*') if p.is_file() and '.raw' not in p.parts and '__pycache__' not in p.parts and p.suffix in {'.md','.json','.py'}]
    files += [PROJECT / 'idea-inbox/2026-09-20-gic-design-directions.md', PROJECT / 'questions/Q-20260920-gic-design-directions.md']
    bad_encoding = []
    broken = []
    for path in files:
        text = path.read_text(encoding='utf-8')
        if '\ufffd' in text:
            bad_encoding.append(str(path))
        if path.suffix == '.json':
            json.loads(text)
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', text):
                target = target.strip('<>').split('#',1)[0]
                if not target or re.match(r'^[a-zA-Z]+://', target):
                    continue
                candidate = (path.parent / unquote(target)).resolve()
                if not candidate.exists():
                    broken.append(f'{path.relative_to(REPO)} -> {target}')
    checks.append(('UTF-8可读、JSON合法、无替换乱码', not bad_encoding))
    checks.append(('本轮Markdown本地链接可解析', not broken))
    source_notes = (ROOT / 'source-notes.md').read_text(encoding='utf-8')
    checks.append(('24个来源编号均在笔记中', all(f'## T{i:02d} ' in source_notes for i in range(1,25))))
    case_text = '\n'.join(p.read_text(encoding='utf-8') for p in cases)
    checks.append(('逐案都有吸收/适配/更新/未知', all(all(h in p.read_text(encoding='utf-8') for h in ['## 吸收','## 适配','## 更新决定','## 未确认信息']) for p in cases)))
    inbox = (PROJECT / 'idea-inbox/2026-09-20-gic-design-directions.md').read_text(encoding='utf-8')
    checks.append(('五候选保留Raw资格与模板审查', all(f'C-GIC-{c}' in inbox for c in 'ABCDE') and 'Agent Proposal / Raw Idea / Unqualified' in inbox and '## 资格确认记录' in inbox))
    report = ['# 本轮文档检查', '', '日期：2026-09-20。检查对象是研究文件及来源链；不代表玩法测试、平衡或用户体验通过。', '', '| 检查 | 结果 |', '| --- | --- |']
    report += [f'| {name} | {"PASS" if ok else "FAIL"} |' for name,ok in checks]
    report += ['', f'合计：{sum(ok for _,ok in checks)}/{len(checks)}。', '', '另已通过材料包验证与[八模块结构检查](phase1-check.md)。本轮0场模拟、0个可玩原型、0位真人受试者。', '', '人工核对：新渠道/初态/目标/布场/模式均标明与RC1差异；GIC描述、研究推断、agent候选分开；同站多档案不作独立证据；短摘要且未补全的条目未计入24款；原图与第三方原文在忽略目录，不随Git提交。']
    if broken:
        report += ['', '本地链接错误：', *broken]
    if bad_encoding:
        report += ['', '编码错误：', *bad_encoding]
    (ROOT / 'checks/review-check.md').write_text('\n'.join(report)+'\n',encoding='utf-8',newline='\n')
    for name,ok in checks:
        print(('PASS: ' if ok else 'FAIL: ')+name)
    if broken:
        print('\n'.join(broken))
    return 0 if all(ok for _,ok in checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
