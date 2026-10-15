"""Independent root review: fixed hashes, GLB structure and actually viewed evidence.
Does not rerun the producer's Blender checks or claim runtime acceptance.
"""
from pathlib import Path
import json, hashlib, struct

BASE = Path('E:/Project/yanzhou-battle-3d/component-detail-2026-10-14')
OUT = Path(__file__).parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def verify(folder):
    m=read(folder/'manifest.json')
    for f in m['files']:
        p=folder/f['path']
        assert p.stat().st_size==f['bytes'] and sha(p)==f['sha256'], str(p)
    return {'sha256':sha(folder/'manifest.json'),'files':len(m['files']),'bytes':sum(f['bytes'] for f in m['files'])}

A=BASE/'expansion-a-v01'
glbs=[]
for p in sorted((A/'models').glob('*.glb')):
    raw=p.read_bytes(); magic,version,length=struct.unpack_from('<4sII',raw)
    assert magic==b'glTF' and version==2 and length==len(raw)
    size,kind=struct.unpack_from('<II',raw,12); assert kind==0x4e4f534a
    doc=json.loads(raw[20:20+size])
    glbs.append({'path':str(p),'sha256':sha(p),'meshes':len(doc.get('meshes',[])),
      'surfaces':sum(len(m['primitives']) for m in doc.get('meshes',[])),
      'nodes':[{'name':n.get('name'), 'extras':n.get('extras',{})} for n in doc['nodes']],
      'materials':[{'name':m.get('name'),'pbr':m.get('pbrMetallicRoughness',{})} for m in doc.get('materials',[])],
      'embeddedImages':len(doc.get('images',[]))})
views=['PAWN-02-roundtrip-final.png','CHIPS-roundtrip-final.png','CONTROL-01-roundtrip-final.png',
 'PAWN-02-raking-material.png','PAWN-02-corner-fastening-detail-v03.png',
 'CHIP-01-tray-contact-side-final.png','CHIP-02-tray-contact-side-final.png',
 'CHIP-01-empty-tray-final.png','CHIP-02-empty-tray-final.png','CHIP-03-full-tray-final.png',
 'CHIP-03-lock-contact-detail-v03.png','CHIP-01-relief-detail-v03.png','CHIP-02-relief-detail-v03.png',
 'CONTROL-step-speed-detail-v03.png','CONTROL-pause-state-material.png']
result={'reviewer':'root, independent of A producer','date':'2026-10-15',
 'manifest':verify(A),'sourceSha256':sha(A/'models/expansion-a-source.blend'),
 'actualImageViews':[{'path':str(A/'renders'/v),'sha256':sha(A/'renders'/v)} for v in views],
 'independentGlbParse':glbs,
 'producerExecutedBlenderEvidence':read(A/'reports/verification.json'),
 'producerRenderProvenance':read(A/'reports/roundtrip-render-evidence.json'),
 'decision':'PAWN-02, CHIP-01/02/03, CONTROL-01 Q1/Q2 passed for scoped runtime integration; Q3 NotRun',
 'limits':['No independent Blender rerun','Scalar roughness exported as declared; source roughness maps are not asserted as runtime maps',
 'CONTROL step symbols are merged with STATIC; do not depress only its green PRESS_CAP and leave symbols floating',
 'GLB visibility extras require runtime application; static image does not validate input, motion or performance',
 'PAWN raking image has a cropped base and is used only for material evidence; full final roundtrip image covers the complete pawn']}
(OUT/'expansion-a-root-check-v02.json').write_bytes(json.dumps(result,ensure_ascii=False,indent=2).encode())
C=BASE/'expansion-c-v01';S=C/'review-supplement'
c={'reviewer':'root','date':'2026-10-15','originalManifest':verify(C),'supplementManifest':verify(S),
 'actualImageViews':[{'path':str(S/f'SLOT-01-{state}-full-frame.png'),'sha256':sha(S/f'SLOT-01-{state}-full-frame.png')} for state in ['reserved','history','focus']],
 'producerFramingEvidence':read(S/'framing-evidence.json'),
 'decision':'Three complete state views accepted: all four corners visible with margins; closes C review-v01 framing gap. Q1/Q2 complete; runtime mat pressure and Q3 still pending.'}
(OUT/'expansion-c-root-supplement-v02.json').write_bytes(json.dumps(c,ensure_ascii=False,indent=2).encode())
print(json.dumps({'A':result['manifest'],'A_glbs':len(glbs),'A_meshes':sum(x['meshes'] for x in glbs),'A_surfaces':sum(x['surfaces'] for x in glbs),'C':c['originalManifest'],'supplement':c['supplementManifest']},ensure_ascii=False))
