"""Read-only independent B/D source-package and GLB audit. No Blender/Godot run."""
from pathlib import Path
from datetime import datetime
import hashlib, json, struct, io
import numpy as np
from PIL import Image

BASE = Path('E:/Project/yanzhou-battle-3d/component-detail-2026-10-14')
OUT = Path(__file__).parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))

VIEWS = {
 'b': ['WAND-02-front-clay-v03.png','WAND-02-side-clay-v03.png','WAND-02-back-clay-v03.png',
       'WAND-02-quarter-clay-v03.png','WAND-02-claws-detail-clay-v03.png',
       'WAND-02-material-final.png','WAND-02-head-raking-final.png','WAND-02-grip-seam-final.png',
       'WAND-02-purpose-ordinary-final.png','WAND-02-purpose-focus-final.png','WAND-02-roundtrip-final.png',
       'WAND-02-collar-bore-cutaway-final.png','WAND-02-table-contact-final.png'],
 'd': ['DECOR-01-roundtrip-final.png','DECOR-01-spine-material-final-v02.png','DECOR-01-paper-corner-final-v02.png',
       'DECOR-02-roundtrip-final.png','DECOR-02-raking-material-final-v02.png','DECOR-02-claw-contact-final-v02.png',
       'DECOR-02-support-cutaway-clay-v02.png','DECOR-03-roundtrip-final.png','DECOR-03-raking-material-final-v02.png',
       'DECOR-03-sand-preview-final.png','DECOR-03-sand-near-final.png','DECOR-03-sand-elapsed-final.png',
       'DECOR-03-neck-final-v02.png']}

def load_glb(p):
    raw=p.read_bytes();magic,version,length=struct.unpack_from('<4sII',raw)
    assert magic==b'glTF' and version==2 and length==len(raw), str(p)
    offset=12; doc=None; binary=None
    while offset<len(raw):
        size,kind=struct.unpack_from('<II',raw,offset);chunk=raw[offset+8:offset+8+size]
        if kind==0x4e4f534a:doc=json.loads(chunk)
        elif kind==0x004e4942:binary=chunk
        offset+=8+size
    return doc,binary

def node_matrix(n):
    if 'matrix' in n:return np.array(n['matrix'],dtype=float).reshape(4,4,order='F')
    x,y,z,w=n.get('rotation',[0,0,0,1]);m=np.eye(4)
    m[:3,:3]=np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],
                           [2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],
                           [2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]]) @ np.diag(n.get('scale',[1,1,1]))
    m[:3,3]=n.get('translation',[0,0,0]);return m

def inspect_glb(path):
    d,b=load_glb(path)
    types={5120:'i1',5121:'u1',5122:'<i2',5123:'<u2',5125:'<u4',5126:'<f4'}
    widths={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4,'MAT4':16}
    def accessor(idx):
        a=d['accessors'][idx];v=d['bufferViews'][a['bufferView']];dt=np.dtype(types[a['componentType']]);n=widths[a['type']]
        assert 'sparse' not in a
        return np.ndarray((a['count'],n),dt,buffer=b,offset=v.get('byteOffset',0)+a.get('byteOffset',0),
                          strides=(v.get('byteStride',dt.itemsize*n),dt.itemsize)).copy()
    nodes=d.get('nodes',[]);parents={ch:i for i,n in enumerate(nodes) for ch in n.get('children',[])};transforms={}
    def world(i):
        if i not in transforms:transforms[i]=(world(parents[i]) if i in parents else np.eye(4)) @ node_matrix(nodes[i])
        return transforms[i]
    summaries=[];all_visible=[];nonfinite=0;degenerate=0;missing_uv=[];missing_normals=[];surfaces=0;all_positions={}
    for i,n in enumerate(nodes):
        if 'mesh' not in n:continue
        positions=[];tris=0
        for pi,p in enumerate(d['meshes'][n['mesh']]['primitives']):
            assert p.get('mode',4)==4
            surfaces+=1;at=p['attributes'];v=accessor(at['POSITION']);nonfinite+=int(np.count_nonzero(~np.isfinite(v)))
            if 'TEXCOORD_0' not in at:missing_uv.append([n.get('name'),pi])
            else:nonfinite+=int(np.count_nonzero(~np.isfinite(accessor(at['TEXCOORD_0']))))
            if 'NORMAL' not in at:missing_normals.append([n.get('name'),pi])
            else:nonfinite+=int(np.count_nonzero(~np.isfinite(accessor(at['NORMAL']))))
            ix=accessor(p['indices']).reshape(-1) if 'indices' in p else np.arange(len(v))
            t=ix.reshape(-1,3);tris+=len(t)
            area2=np.linalg.norm(np.cross(v[t[:,1]]-v[t[:,0]],v[t[:,2]]-v[t[:,0]]),axis=1)
            degenerate+=int(np.count_nonzero(area2<=1e-14))
            positions.append((world(i) @ np.column_stack([v,np.ones(len(v))]).T).T[:,:3])
        pts=np.concatenate(positions);all_positions[n.get('name')]=pts;extra=n.get('extras',{})
        visible=extra.get('default_visible',True) and not extra.get('qa_bounds_exclude',False)
        if visible:all_visible.append(pts)
        summaries.append({'name':n.get('name'),'extras':extra,'triangles':tris,'defaultBoundsIncluded':visible,
                          'min_m':pts.min(0).tolist(),'max_m':pts.max(0).tolist(),'dimensions_mm':((pts.max(0)-pts.min(0))*1000).tolist()})
    material=[]
    for m in d.get('materials',[]):
        pbr=m.get('pbrMetallicRoughness',{});item={'name':m.get('name'),'roughnessFactor':pbr.get('roughnessFactor',1),
        'metallicFactor':pbr.get('metallicFactor',1),'extensions':m.get('extensions',{}),'alphaMode':m.get('alphaMode','OPAQUE'),
        'baseColorFactor':pbr.get('baseColorFactor',[1,1,1,1]),'emissiveFactor':m.get('emissiveFactor',[0,0,0]),
        'normalTexture':m.get('normalTexture'),'baseColorTexture':pbr.get('baseColorTexture')}
        if 'metallicRoughnessTexture' in pbr:
            tex=d['textures'][pbr['metallicRoughnessTexture']['index']];im=d['images'][tex['source']];bv=d['bufferViews'][im['bufferView']]
            off=bv.get('byteOffset',0);arr=np.array(Image.open(io.BytesIO(b[off:off+bv['byteLength']])).convert('RGB'))/255
            item['decodedRoughnessMean']=float(arr[:,:,1].mean()*item['roughnessFactor'])
            item['decodedMetallicMean']=float(arr[:,:,2].mean()*item['metallicFactor'])
        material.append(item)
    for im in d.get('images',[]):
        assert 'bufferView' in im, 'External image dependency: '+str(path)
        bv=d['bufferViews'][im['bufferView']];off=bv.get('byteOffset',0);Image.open(io.BytesIO(b[off:off+bv['byteLength']])).verify()
    pts=np.concatenate(all_visible)
    result={'path':str(path),'sha256':sha(path),'meshCount':len(d.get('meshes',[])),'surfaces':surfaces,
            'nodes':summaries,'rootExtras':[n.get('extras',{}) for n in nodes if n.get('name','').endswith('__ROOT')],
            'defaultVisibleBounds_mm':{'min':(pts.min(0)*1000).tolist(),'max':(pts.max(0)*1000).tolist(),'dimensions':((pts.max(0)-pts.min(0))*1000).tolist()},
            'nonfiniteComponents':nonfinite,'degenerateTrianglesAtCrossNorm1e_14':degenerate,'missingUv':missing_uv,'missingNormals':missing_normals,
            'embeddedImagesDecoded':len(d.get('images',[])),'materials':material,'extensionsUsed':d.get('extensionsUsed',[])}
    if path.stem=='DECOR-02':
        pts=all_positions['DECOR-02__GLASS'];center=np.array([0,.034,0]);r=np.linalg.norm(pts-center,axis=1)*1000
        result['independentGlassShellRadii_mm']={'min':float(r.min()),'max':float(r.max()),'nominalInner':28.125,'nominalOuter':29.925}
    if path.stem=='WAND-02':
        pts=all_positions['WAND-02__PURPOSE_COLLAR'];r=np.linalg.norm(pts[:,[0,2]],axis=1)*1000
        result['independentCollarVertexRadius_mm']={'min':float(r.min()),'max':float(r.max()),'expectedBore':5.85}
        rp=path.parent.parent/'reports/resting-pose.json'
        if rp.exists():
            resting=read(rp);a=np.deg2rad(resting['glTF_table_y_up_rotation_x_deg']);v=np.concatenate(all_visible)
            h=np.cos(a)*v[:,1]-np.sin(a)*v[:,2]+resting['glTF_table_translation_y_m']
            result['independentGlbRestPose_mm']={'minAll':float(h.min()*1000),'minTail':float(h[v[:,1]<.03].min()*1000),
              'minHead':float(h[v[:,1]>.14].min()*1000),'penetratingVerticesBelow1e_6m':int(np.count_nonzero(h<-.000001)),
              'claim':'Binary GLB positions transformed with supplied pose; no engine or gravity/friction simulation.'}
    return result

def audit(group,assets):
    folder=BASE/f'expansion-{group}-v01';mp=folder/'manifest.json'
    manifest={'status':'PendingNotFrozen'}
    if mp.exists():
        m=read(mp);fail=[]
        for f in m['files']:
            p=folder/f['path']
            if not p.exists() or p.stat().st_size!=f['bytes'] or sha(p)!=f['sha256']:fail.append(f['path'])
        manifest={'status':'Pass' if not fail else 'Fail','sha256':sha(mp),'files':len(m['files']),
                  'bytes':sum(f['bytes'] for f in m['files']),'mismatches':fail}
    reports={}
    for name in ['verification.json','contact-measurements.json','roundtrip-render-evidence.json','runtime-mesh-bindings.json','final-detail-evidence.json','sand-state-evidence.json','resting-pose.json','per-component-edit-probes.json','asset-bindings.json']:
        p=folder/'reports'/name
        if p.exists():reports[name]={'path':str(p),'sha256':sha(p),'producerExecutedEvidence':read(p)}
    probe_check=[]
    if group=='d':
        probes=read(folder/'reports/per-component-edit-probes.json')
        for p in probes['probes']:
            values={}
            for state,rec in p['exports'].items():
                path=folder/rec['file'];assert sha(path)==rec['sha256'] and path.stat().st_size==rec['bytes']
                d,b=load_glb(path);coords=[]
                for mesh in d['meshes']:
                    for prim in mesh['primitives']:
                        a=d['accessors'][prim['attributes']['POSITION']];v=d['bufferViews'][a['bufferView']]
                        arr=np.ndarray((a['count'],3),'<f4',buffer=b,offset=v.get('byteOffset',0)+a.get('byteOffset',0),strides=(v.get('byteStride',12),4)).copy()
                        coords.append(arr)
                c=np.concatenate(coords);c=c[np.lexsort((c[:,2],c[:,1],c[:,0]))]
                values[state]={'file':str(path),'fileSha256':sha(path),'sortedPositionBytesSha256':hashlib.sha256(c.tobytes()).hexdigest(),'positionCount':len(c)}
            probe_check.append({'component':p['component'],'independentlyDecodedProbeGeometryChanged':values['before']['sortedPositionBytesSha256']!=values['after']['sortedPositionBytesSha256'],'exports':values})
    result={'reviewer':'component_detail_design (D), independent of asset producer','date':datetime.now().astimezone().isoformat(),
       'package':f'COMPONENT-EXPANSION-{group.upper()}-01','manifest':manifest,
       'source':{'path':str(folder/f'models/expansion-{group}-source.blend'),'sha256':sha(folder/f'models/expansion-{group}-source.blend')},
       'independentGlbAudit':[inspect_glb(folder/f'models/{a}.glb') for a in assets],
       'actuallyViewedImages':[{'path':str(folder/'renders'/n),'sha256':sha(folder/'renders'/n)} for n in VIEWS[group]],
       'producerEvidenceReadNotRerun':reports,
       'independentProbeGeometryComparison':probe_check,
       'scope':['D actual image views and read-only bytes/hash, GLB binary geometry/material/image parsing',
                'No independent Blender reopen/export/physics rerun; those tests belong to asset producer',
                'No Godot, OS input, transparency sorting, performance or user art acceptance'],
       'decision':'See companion review; this script records evidence rather than granting visual approval.'}
    target=OUT/f'expansion-{group}-independent-check-v01.json';target.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'group':group,'manifest':manifest,'source':result['source']['sha256'],'glbs':len(assets),
          'images':len(VIEWS[group]),'bounds':{Path(g['path']).stem:g['defaultVisibleBounds_mm'] for g in result['independentGlbAudit']},
          'issues':[{k:g[k] for k in ['nonfiniteComponents','degenerateTrianglesAtCrossNorm1e_14','missingUv','missingNormals']} for g in result['independentGlbAudit']]},ensure_ascii=False))

if __name__=='__main__':
    audit('b',['WAND-02']);audit('d',['DECOR-01','DECOR-02','DECOR-03'])
