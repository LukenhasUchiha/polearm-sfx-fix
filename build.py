"""Build: python build.py --divine PATH_TO_DIVINE_EXE (LSLib 1.20.4)."""
import argparse,hashlib,json,pathlib,shutil,subprocess,zipfile,xml.etree.ElementTree as ET
from verify import verify
ROOT=pathlib.Path(__file__).parent
VERSION='1.2.0'
RESOURCE=pathlib.Path('Public/WeaponSFXRepair/Content/[PAK]_WeaponSFXRepair/_merged')
def run(*args):subprocess.run([str(x) for x in args],check=True)
def main():
 p=argparse.ArgumentParser();p.add_argument('--divine',required=True);args=p.parse_args()
 exe=pathlib.Path(args.divine).resolve();assert exe.is_file()
 verify(ROOT/'src')
 stage=ROOT/'build/package';dist=ROOT/'dist';dist.mkdir(exist_ok=True,parents=True)
 # A dedicated stage prevents stray editor files from entering the PAK.
 if stage.exists():
  assert stage.resolve().is_relative_to((ROOT/'build').resolve())
  shutil.rmtree(stage)
 meta=stage/'Mods/WeaponSFXRepair/meta.lsx';meta.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(ROOT/'src/Mods/WeaponSFXRepair/meta.lsx',meta)
 lsf=stage/RESOURCE.with_suffix('.lsf');lsf.parent.mkdir(parents=True,exist_ok=True)
 run(exe,'-g','bg3','-a','convert-resource','-s',ROOT/'src'/RESOURCE.with_suffix('.lsx'),'-d',lsf)
 pak=dist/'WeaponSFXRepair.pak'
 run(exe,'-g','bg3','-a','create-package','-s',stage,'-d',pak)
 check=ROOT/'build/unpacked'
 if check.exists():
  assert check.resolve().is_relative_to((ROOT/'build').resolve())
  shutil.rmtree(check)
 run(exe,'-g','bg3','-a','extract-package','-s',pak,'-d',check)
 assert {str(x.relative_to(check)).replace('\\','/') for x in check.rglob('*') if x.is_file()}=={'Mods/WeaponSFXRepair/meta.lsx',str(RESOURCE.with_suffix('.lsf')).replace('\\','/')}
 assert (check/RESOURCE.with_suffix('.lsf')).read_bytes()==lsf.read_bytes()
 run(exe,'-g','bg3','-a','convert-resource','-s',check/RESOURCE.with_suffix('.lsf'),'-d',check/RESOURCE.with_suffix('.lsx'))
 verify(check)
 def canon(n):return (n.tag,tuple(sorted(n.attrib.items())),tuple(canon(c) for c in n))
 resource=ET.parse(check/RESOURCE.with_suffix('.lsx')).getroot()
 digest=hashlib.sha256(json.dumps(canon(resource),ensure_ascii=True,separators=(',',':')).encode()).hexdigest()
 expected=json.loads((ROOT/'docs/validated-resource.json').read_text())['canonical_sha256']
 assert digest==expected,'Animation data differ from the gameplay-tested release baseline'
 archive=dist/f'PolearmSFXFix-{VERSION}.zip'
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:z.write(pak,'WeaponSFXRepair.pak')
 with zipfile.ZipFile(archive) as z:assert z.namelist()==['WeaponSFXRepair.pak'] and z.read('WeaponSFXRepair.pak')==pak.read_bytes()
 (dist/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.name+'\n' for f in (pak,archive)),encoding='ascii')
 print('Verified source, packaged resources, binary roundtrip and Vortex ZIP.')
if __name__=='__main__':main()
