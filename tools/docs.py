"""Maintain the document index and validate active Markdown links (stdlib only).

Usage: python tools/docs.py index | check
Historical snapshots and external projects are deliberately outside link checking.
"""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote, urlsplit
import json
import re
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ('archive/', 'docs/history/', 'media-analysis-lab/runs/', 'media-analysis-lab/examples/',
          'media-analysis-lab/skill-iteration/game-analysis-orchestra/',
          'yanzhou/history/exploration-2026-09-24/')
LINK = re.compile(r'\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)')

def files():
    raw = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '-z',
                                   '--cached', '--others', '--exclude-standard'])
    return sorted({p for p in raw.decode('utf-8').split('\0')
                   if p and (ROOT / p).is_file()})

def active(path):
    return path.endswith('.md') and not path.startswith(FROZEN)

def prose(text):
    # Template/example links in fenced code are not navigation.
    return re.sub(r'^(`{3,}|~{3,}).*?^\1\s*$', '', text, flags=re.M | re.S)

def anchors(text):
    found = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    counts = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(text), flags=re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading).strip().lower()
        slug = ''.join(c for c in heading if c in '-_ ' or unicodedata.category(c)[0] in 'LMN')
        slug = slug.replace(' ', '-')
        suffix = counts[slug]
        found.add(slug + (f'-{suffix}' if suffix else ''))
        counts[slug] += 1
    return found

def index():
    paths = [p for p in files() if p.startswith('yanzhou/')]
    groups = {}
    for p in paths:
        groups.setdefault(p.split('/')[1] if '/' in p[8:] else '项目入口', []).append(p)
    lines = ['# 言咒文件索引', '',
             '自动生成：`python tools/docs.py index`。当前工作树存在的Git跟踪或未忽略文件；不据此授予游戏材料阅读权限。', '',
             f'共 {len(paths)} 份。日常工作从[项目首页](../README.md)开始；历史内容按固定版本解释。', '']
    import posixpath
    for group, members in sorted(groups.items()):
        lines += [f'## {group}（{len(members)}）', '']
        for p in members:
            label = p.removeprefix('yanzhou/')
            target = posixpath.relpath(p, 'yanzhou/governance')
            lines.append(f'- [{label}]({target})')
        lines.append('')
    (ROOT/'yanzhou/governance/file-index.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    print(json.dumps({'indexed_files':len(paths),'groups':{k:len(v) for k,v in groups.items()}},ensure_ascii=False))

def check():
    paths = [p for p in files() if active(p)]
    errors = []; checked = 0; local_anchors = {}; frozen_links = 0
    for rel in paths:
        text = (ROOT/rel).read_text(encoding='utf-8-sig')
        for match in LINK.finditer(prose(text)):
            target = match[1].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('//'):
                continue
            checked += 1
            path = ((ROOT/rel).parent / unquote(parsed.path)).resolve() if parsed.path else ROOT/rel
            if not path.exists():
                errors.append({'file':rel,'target':target,'problem':'missing path'})
                continue
            if not parsed.fragment or path.suffix.lower()!='.md':
                continue
            try: dst = path.relative_to(ROOT).as_posix()
            except ValueError: continue
            if dst.startswith(FROZEN):
                frozen_links += 1
                continue
            if path not in local_anchors:
                local_anchors[path] = anchors(path.read_text(encoding='utf-8-sig'))
            if unquote(parsed.fragment) not in local_anchors[path]:
                errors.append({'file':rel,'target':target,'problem':'missing anchor'})
    print(json.dumps({'active_markdown_files':len(paths),'local_links_checked':checked,
                      'frozen_target_anchors_not_reinterpreted':frozen_links,
                      'errors':errors},ensure_ascii=False,indent=2))
    return 1 if errors else 0

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('index','check'):
        raise SystemExit('Usage: python tools/docs.py index | check')
    sys.exit(check() if sys.argv[1]=='check' else index())
