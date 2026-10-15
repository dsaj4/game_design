"""Read-only evidence audit. Manual viewing is declared, never inferred from hashes."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import struct

ROOT = Path('E:/Project/yanzhou-godot')
EVIDENCE = ROOT / 'evidence/development-batch-10/expansion-source-06'
OUT = Path(__file__).with_name('q3-expansion-source-06-evidence.json')
VIEWED = '''01-tabletop 02-player-closeup 03-enemy-closeup 04-dark-closeup
05-resource-closeup 06-guard-closeup 10-card-closeup component-07-caster-future
07-completion-source 08-completion-appear 11-shield-use component-03-drawer-open
demon-07-lock-detail demon-08-save-error component-10-terminal demon-04-reveal-mid
demon-09-player-attack demon-10-enemy-attack demon-11-interrupt component-04-hover
component-08-hourglass-near component-09-hourglass-paid'''.split()

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def fingerprint(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def numbers(rect):
    return [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', rect)]

manifest = read(EVIDENCE / 'execution-manifest.json')
runs = read(EVIDENCE / 'runs.json')
data = {
    'auditUtc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewDate': '2026-10-15',
    'reviewer': 'component_detail_design / D',
    'executionBy': 'root; D did not rerun Godot or package checks',
    'scope': manifest['scope'],
    'conclusion': 'Limited visual Q3 Pass for the named 19 components in these two rendered viewports; packaging for review may proceed',
    'userArtAcceptance': False,
    'manualViewingMethod': 'view_image, full PNG; the 22 names below were actually viewed at both resolutions',
    'manualViewedNames': VIEWED,
    'executionManifest': fingerprint(EVIDENCE / 'execution-manifest.json'),
    'runsFile': fingerprint(EVIDENCE / 'runs.json'),
    'identity': {k: manifest[k] for k in ['codeCommit', 'debugAssemblySha256', 'debugAssemblyLastWriteUtc', 'executableSha256', 'runnerSha256', 'packaged', 'componentManifests']},
    'workingTreeBoundary': 'Execution manifest records working-tree changes; codeCommit alone is not the complete source identity.',
    'slotBinding': {
        'method': 'NextPass on actual wovenbody with slot and cloth masks plus shading normal; no mesh indentation',
        'readBy': 'D, targeted source lines',
        'runtimeUniformProbe': 'NotRun',
        'files': [],
    },
    'resolutions': [],
    'residuals': [
        'Some Chinese periods wrap alone; no content clipping observed in the viewed captures.',
        'The PgUp/Dn auxiliary page hint wraps at 1366; the actual page indicator and buttons remain visible.',
        'Tinted alpha shells do not reproduce optical transmission/refraction.',
        'Only the shield card has the new detailed ink illustration; other card categories retain existing graphics.',
    ],
    'notCovered': ['OS input', 'continuous playback/foreground performance', 'arbitrary camera or transparency sorting angles', 'all material inventory/card illustrations', 'all 109 design states', 'other viewport sizes', 'independent package execution', 'user final art acceptance'],
}
for name in ['godot/ComponentTableAssets.cs', 'godot/CompleteMainCards.cs']:
    item = fingerprint(ROOT / name)
    expected = next(x['sha256'] for x in manifest['sourceFiles'] if x['path'].replace('\\', '/') == name)
    item.update(executionManifestSha256=expected, matchesExecutionManifest=item['sha256'] == expected)
    assert item['matchesExecutionManifest'], name
    data['slotBinding']['files'].append(item)

for resolution in ['1920x1080', '1366x768']:
    folder = EVIDENCE / resolution
    result = read(folder / 'physical-result.json')
    run = next(x for x in runs if x['resolution'] == resolution)
    assert result['passed'] and run['passed'] and run['exitCode'] == 0
    assert len(result['results']) == 72 and all(x['status'] == 'Pass' for x in result['results'])
    stderr = (folder / 'stderr.log').read_text(encoding='utf-8-sig')
    images = []
    for path in sorted(folder.glob('*.png')):
        item = fingerprint(path)
        item['dimensions'] = list(struct.unpack('>II', path.read_bytes()[16:24]))
        item['actuallyViewedByD'] = path.stem in VIEWED
        images.append(item)
    assert len(images) == 34 and sum(x['actuallyViewedByD'] for x in images) == 22
    caster = next(x for x in result['componentUi'] if x['capture'] == 'component-07-caster-future')
    captions = caster['worldCaptions']
    upper = numbers(captions[0]['rect'])
    lower = numbers(captions[2]['rect'])
    entry = {
        'resolution': resolution,
        'run': run,
        'resultCount': len(result['results']),
        'passCount': sum(x['status'] == 'Pass' for x in result['results']),
        'input': result['input'],
        'resultFiles': [fingerprint(folder / x) for x in ['physical-result.json', 'stdout.log', 'stderr.log']],
        'stderr': {'empty': not stderr.strip(), 'warningCount': stderr.count('WARNING:'), 'errorCount': len(re.findall(r'^\s*ERROR:', stderr, re.M)), 'warningLines': [x for x in stderr.splitlines() if 'WARNING:' in x]},
        'images': images,
        'manualViewedCount': 22,
        'captureCount': len(images),
        'casterCaptionGapPx': lower[1] - upper[1] - upper[3],
        'casterWorldCaptions': captions,
        'casterPaper': caster['papers'],
        'casterButtons': caster['buttons'],
        'hoverPaper': next(x for x in result['componentUi'] if x['capture'] == 'component-04-hover')['papers'],
        'mainGlass': next(x for x in result['renderCosts'] if x['capture'] == '01-tabletop')['glass'],
        'casterGlass': next(x for x in result['renderCosts'] if x['capture'] == 'component-07-caster-future')['glass'],
        'manualTimedCues': result['cues'],
        'allAssertedCheckNames': [x['name'] for x in result['results']],
    }
    assert entry['stderr']['errorCount'] == 0
    data['resolutions'].append(entry)

data['counts'] = {'pngHashed': 68, 'pngActuallyViewedByD': 44, 'pngNotDirectlyViewedByD': 24, 'assertionsRead': 144}
design = Path('E:/Project/yanzhou-workspace/workspace/2026-10-14_yanzhou/component-design-status.md')
table = '\n'.join(x for x in design.read_text(encoding='utf-8-sig').splitlines() if x.startswith('|'))
data['designSnapshotTable'] = {'rowLines': len(table.splitlines()), 'sha256': hashlib.sha256(table.encode('utf-8')).hexdigest(), 'expectedUnchangedSha256': '200a7178930369bbaecf9d9f64629af13b3ac4252c8c1e5113228f96fcb3fd37'}
assert data['designSnapshotTable']['sha256'] == data['designSnapshotTable']['expectedUnchangedSha256']
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'output': fingerprint(OUT), 'counts': data['counts'], 'runs': [{'resolution': x['resolution'], 'passCount': x['passCount'], 'stderr': x['stderr'], 'captionGapPx': x['casterCaptionGapPx']} for x in data['resolutions']], 'designSnapshotTable': data['designSnapshotTable']}, ensure_ascii=True))
