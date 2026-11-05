import pathlib,xml.etree.ElementTree as ET,json
ROOT=pathlib.Path(__file__).parent
def attrs(n):return {a.get('id'):a.get('value') for a in n.findall('attribute')}
def verify(base):
 tree=ET.parse(base/'Public/WeaponSFXRepair/Content/[PAK]_WeaponSFXRepair/_merged.lsx')
 nodes=tree.findall('./region/node/children/node')
 expected={r['id'] for r in json.loads((ROOT/'docs/audit.json').read_text())['resources']}
 assert len(nodes)==10 and {attrs(n)['ID'] for n in nodes}==expected
 markers=0
 for n in nodes:
  a=attrs(n);es=n.findall('./children/node');ts=[float(attrs(e)['Time']) for e in es]
  assert ts==sorted(ts),a['Name']+' has out-of-order events'
  assert all(0<=t<=float(a['Duration']) for t in ts)
  sounds=[e for e in es if attrs(e).get('ID')=='Whoosh_Combat'];assert len(sounds)==1
  prop=attrs(sounds[0].find('./children/node'));assert prop['Resource']=='726624f9-f7e5-42ff-ccf7-061a84f6237d'
  assert prop['SoundObjectIndex']==('2' if '_LHand_' in a['Name'] else '1')
  markers+=sum(attrs(e).get('ID')=='CastPierce' for e in es)
 assert markers==3
 meta=ET.parse(base/'Mods/WeaponSFXRepair/meta.lsx');mi=attrs(meta.find('.//node[@id="ModuleInfo"]'))
 assert mi['UUID']=='2ed1e60b-3e21-4abe-8448-ab90502a88d8'
 assert int(mi['Version64'])==(1<<55)|(1<<47)
 assert meta.find('.//node[@id="Target"]/attribute[@value="Story"]') is not None
 assert not list(base.rglob('*.lua'))
if __name__=='__main__':verify(ROOT/'src');print('PASS')
