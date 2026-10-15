"""Read-only independent checks of the frozen E asset package; writes this review's evidence only."""
from pathlib import Path
import hashlib, json, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageFont

BASE = Path('E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/expansion-e-v01')
OUT = Path(__file__).parent / 'expansion-e-independent-check-v01.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
manifest = read(BASE / 'manifest.json')
layout = read(BASE / 'ui/layouts.json')['layouts']
measurement = read(BASE / 'checks/text-measurements.json')
selfcheck = read(BASE / 'checks/verification.json')
font_path = Path(selfcheck['font']['path'])
errors = []

def overlap(a, b):
    return min(a[0]+a[2],b[0]+b[2]) > max(a[0],b[0]) and min(a[1]+a[3],b[1]+b[3]) > max(a[1],b[1])

for name, info in layout.items():
    if info['bodyFontPx'] != 18: errors.append([name, 'body font'])
    if info['component'] == 'TXT-02':
        if info['clipSizePx'] != [7,16] or info['foldPx'] != 15 or info['screenMarginPx'] != 24:
            errors.append([name, 'fixed ornament or screen margin'])
    else:
        if info['contentWidthPx'] not in [320,380] or info['titleFontPx'] != 24:
            errors.append([name, 'actual content width/title'])
        if 'closeHitRect' in info:
            close = info['closeHitRect']
            if close[2:] != [44,44] or overlap(close, info['contentRect']): errors.append([name, 'close overlap/size'])
        if 'footerRect' in info and overlap(info['footerRect'], info['contentRect']): errors.append([name, 'footer overlap'])

fonts = {size: ImageFont.truetype(str(font_path), size) for size in (18,24)}
remeasured = []
for row in measurement:
    box = fonts[row['fontPx']].getbbox(row['text'])
    width = box[2]-box[0]
    rect = row['rect']; bounds = row['glyphBounds']
    fits = width <= rect[2] and bounds[0] >= rect[0] and bounds[1] >= rect[1] and bounds[2] <= rect[0]+rect[2] and bounds[3] <= rect[1]+rect[3]
    if not fits: errors.append([row['tag'], 'glyph bounds', row['text']])
    remeasured.append({'tag':row['tag'],'fontPx':row['fontPx'],'text':row['text'],'remeasuredWidth':width,'fits':fits})

svgs = list((BASE/'sources/svg').rglob('*.svg'))
for path in svgs:
    tree = ET.parse(path)
    bad = [el.tag for el in tree.iter() if el.tag.rsplit('}',1)[-1] in ('text','image','foreignObject')]
    if bad: errors.append([str(path.relative_to(BASE)),bad])

pngs = list((BASE/'runtime').rglob('*.png'))
transparent_dirty = partial_white = 0
for path in pngs:
    im = Image.open(path)
    if im.mode != 'RGBA': errors.append([str(path.relative_to(BASE)),im.mode]); continue
    arr = np.array(im)
    transparent_dirty += int(np.count_nonzero((arr[:,:,3] == 0) & np.any(arr[:,:,:3] != 0,axis=2)))
    partial_white += int(np.count_nonzero((arr[:,:,3] > 0) & (arr[:,:,3] < 255) & np.all(arr[:,:,:3] == 255,axis=2)))
original = np.array(Image.open(BASE/'runtime/png/txt02-216-2line-bottom/composite@2x.png'))
probe = np.array(Image.open(BASE/'checks/editable-paper-color-probe.png'))
changed = int(np.count_nonzero(np.any(original != probe,axis=2)))
if not changed or transparent_dirty or partial_white: errors.append(['alpha or edit probe',changed,transparent_dirty,partial_white])

views = ['txt02-four-directions-1x.png','text-review-1366x768-1x.png','text-review-1920x1080-1x.png','txt03-long-content-pages-1x.png','editable-layers-atlas.png','alpha-edge-white-black-burgundy.png']
result = {'package':'COMPONENT-EXPANSION-E-01','manifestSha256':sha(BASE/'manifest.json'),
          'manifestFileCount':len(manifest['files']),'fullManifestBytesAndHashes':'607/607 verified independently by root; not claimed rerun by D',
          'svgActuallyParsed':len(svgs),'svgDynamicTextOrEmbeddedImageErrors':0 if not errors else 'see errors',
          'runtimePngActuallyChecked':len(pngs),'layoutCount':len(layout),'fontPath':str(font_path),'fontSha256':sha(font_path),
          'glyphRemeasurements':remeasured,'transparentNonzeroRGBPixels':transparent_dirty,'partialAlphaPureWhitePixels':partial_white,
          'sourceEditProbeChangedPixelsIndependentlyCompared':changed,'sourceRegeneration':'Asset agent executed; D read source and checked derived pixel change, did not rerun production generator',
          'actuallyViewedImages':[{'path':str(BASE/'renders'/v),'sha256':sha(BASE/'renders'/v)} for v in views],
          'errors':errors,'scope':'offline source structure, actual font/layout, alpha and visual review; RuntimeNotRun'}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('glyphRemeasurements','actuallyViewedImages')},ensure_ascii=False,indent=2))
