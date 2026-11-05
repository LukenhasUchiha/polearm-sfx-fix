import hashlib,json,pathlib,struct,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).parent

def attrs(n):return {a.get('id'):a.get('value') for a in n.findall('attribute')}

def canon(n):
 a=dict(n.attrib)
 if n.tag=='attribute' and a.get('type')=='float':a['value']=struct.pack('<f',float(a['value'])).hex()
 return (n.tag,tuple(sorted(a.items())),tuple(canon(c) for c in n))

def verify(base):
 tree=ET.parse(base/'Public/WeaponSFXRepair/Content/[PAK]_WeaponSFXRepair/_merged.lsx')
 nodes=tree.findall('./region/node/children/node')
 expected={r['id']:r for r in json.loads((ROOT/'docs/audit.json').read_text())['resources']}
 assert len(nodes)==15 and {attrs(n)['ID'] for n in nodes}==set(expected)
 markers=vocals=throws=0
 for n in nodes:
  a=attrs(n);es=n.findall('./children/node');ts=[float(attrs(e)['Time']) for e in es]
  assert ts==sorted(ts),a['Name']+' has out-of-order events'
  assert all(0<=t<=float(a['Duration']) for t in ts)
  assert len(es)==expected[a['ID']]['events'],a['Name']+' has missing/extra events'
  for e in es:
   ea=attrs(e);prop=e.find('./children/node')
   if ea.get('TextKeyType')=='13':
    vocals+=1
    assert attrs(prop)=={'EVocalType':'1','Resource':'','SoundObjectIndex':'4'}
   if ea.get('ID')=='Whoosh_Combat':
    p=attrs(prop);assert p['Resource']=='726624f9-f7e5-42ff-ccf7-061a84f6237d'
    assert p['SoundObjectIndex']==('3' if '_Shove_' in a['Name'] else '2' if '_LHand_' in a['Name'] else '1')
   if ea.get('ID')=='Whoosh_Throw':
    throws+=1
    assert attrs(prop)=={'Resource':'1920c04b-f081-431c-b44f-65e5fd5e4733','SoundObjectIndex':'1'}
  digest=hashlib.sha256(json.dumps(canon(n),ensure_ascii=True,separators=(',',':')).encode()).hexdigest()
  assert digest==expected[a['ID']]['canonical_sha256'],a['Name']+' differs from tested animation data'
  markers+=sum(attrs(e).get('ID')=='CastPierce' for e in es)
 assert markers==3 and vocals==13 and throws==4
 meta=ET.parse(base/'Mods/WeaponSFXRepair/meta.lsx');mi=attrs(meta.find('.//node[@id="ModuleInfo"]'))
 assert mi['UUID']=='2ed1e60b-3e21-4abe-8448-ab90502a88d8'
 assert int(mi['Version64'])==(1<<55)|(2<<47)|1
 assert meta.find('.//node[@id="Target"]/attribute[@value="Story"]') is not None
 assert not list(base.rglob('*.lua'))
if __name__=='__main__':verify(ROOT/'src');print('PASS')
