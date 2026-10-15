"""Read-only GLB/PBR audit for independent C review; not a Blender/Godot run."""
from pathlib import Path
import json, struct, hashlib, io
from PIL import Image
import numpy as np

BASE=Path('E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/expansion-c-v01')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
data=[]
for path in sorted((BASE/'models').glob('*.glb')):
    raw=path.read_bytes(); magic,version,length=struct.unpack_from('<4sII',raw)
    assert magic==b'glTF' and version==2 and length==len(raw)
    offset=12; doc=None; binary=None
    while offset < len(raw):
        size,kind=struct.unpack_from('<II',raw,offset); chunk=raw[offset+8:offset+8+size]
        if kind==0x4E4F534A:doc=json.loads(chunk)
        elif kind==0x004E4942:binary=chunk
        offset+=8+size
    mats=[]
    for mat in doc.get('materials',[]):
        pbr=mat.get('pbrMetallicRoughness',{}); item={'name':mat.get('name'),'metallicFactor':pbr.get('metallicFactor',1),'roughnessFactor':pbr.get('roughnessFactor',1)}
        if 'metallicRoughnessTexture' in pbr:
            tx=doc['textures'][pbr['metallicRoughnessTexture']['index']]
            im=doc['images'][tx['source']]; bv=doc['bufferViews'][im['bufferView']]; start=bv.get('byteOffset',0)
            arr=np.array(Image.open(io.BytesIO(binary[start:start+bv['byteLength']])).convert('RGB'))/255
            item['effectiveRoughnessMean']=float(arr[:,:,1].mean()*item['roughnessFactor'])
            item['effectiveMetallicMean']=float(arr[:,:,2].mean()*item['metallicFactor'])
        else:
            item['effectiveRoughnessMean']=item['roughnessFactor']; item['effectiveMetallicMean']=item['metallicFactor']
        mats.append(item)
    data.append({'file':str(path),'sha256':sha(path),'version':version,'roots':[n.get('name') for n in doc['nodes'] if n.get('name','').endswith('__ROOT')],
                 'namedStateOrMovingNodes':[n.get('name') for n in doc['nodes'] if '__' in n.get('name','')],
                 'meshCount':len(doc.get('meshes',[])),'materials':mats,'embeddedImageCount':len(doc.get('images',[]))})

views=['FINAL-GLB-roundtrip-assembly-neutral.png','FINAL-GLB-roundtrip-contact-detail.png','Q1-runtime-edge-profile-clay.png','Q1-mat-hem-detail-clay.png','Q1-slot-depression-detail-clay.png','Q1-drawer-join-detail-clay.png','Q1-final-rail-installation-cutaway-clay.png','Q1-final-drawer-mounts-clay.png','MAT-01-runtime-fit-weave-hem-detail.png','MAT-01-runtime-fit-raking.png','FINAL-MAT-felt-underside.png','FINAL-SLOT-cloth-pressure-neutral.png','SLOT-01-reserved.png','SLOT-01-history.png','SLOT-01-focus.png','FINAL-DRAWER-neutral.png','DRAWER-01-handle-detail.png','TABLE-01-runtime-fit-raking.png']
result={'package':'COMPONENT-EXPANSION-C-01','manifestSha256':sha(BASE/'manifest.json'),'sourceSha256':sha(BASE/'models/expansion-c-source.blend'),
        'fullManifestHashVerification':'152/152 verified by root, not claimed rerun by D','independentGlbParseAndMrDecode':data,
        'actuallyViewedImages':[{'path':str(BASE/'renders'/v),'sha256':sha(BASE/'renders'/v)} for v in views],
        'renderProvenance':read(BASE/'reports/render-provenance.json'),
        'assetAgentExecutedBlenderEvidence':{'verification':read(BASE/'reports/verification.json'),'installation':read(BASE/'reports/installation-check.json')},
        'Dscope':'18 actual image views, independent GLB JSON and embedded MR decoding; no rerun of Blender/Godot/physics',
        'decision':{'TABLE-01':'Q1/Q2 Pass, scoped integration allowed','MAT-01':'Q1/Q2 Pass, scoped integration allowed','DRAWER-01':'Q1/Q2 Pass, scoped integration allowed; camera/input Q3 pending','SLOT-01':'Geometry/empty pressure reviewed; complete reserved/history/focus images pending; Q3 host pressure binding NotRun'}}
out=Path(__file__).parent/'expansion-c-independent-check-v01.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'manifestSha256':result['manifestSha256'],'sourceSha256':result['sourceSha256'],'glbs':len(data),'actualImages':len(views),
                  'runtimeTableMaterials':next(x['materials'] for x in data if x['file'].endswith('TABLE-01-runtime-fit.glb'))},ensure_ascii=False,indent=2))
