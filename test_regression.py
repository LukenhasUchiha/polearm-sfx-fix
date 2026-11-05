"""Checks chronological animation-event ordering."""
import pathlib,shutil,tempfile,unittest,xml.etree.ElementTree as ET
from verify import verify,attrs
ROOT=pathlib.Path(__file__).parent
class EventOrderRegression(unittest.TestCase):
 def test_validated_release_passes(self):
  verify(ROOT/'src')
 def test_appending_early_sound_after_late_footstep_fails(self):
  with tempfile.TemporaryDirectory(prefix='weapon-sfx-test-') as folder:
   base=pathlib.Path(folder)/'src';shutil.copytree(ROOT/'src',base)
   file=base/'Public/WeaponSFXRepair/Content/[PAK]_WeaponSFXRepair/_merged.lsx'
   tree=ET.parse(file)
   n=next(n for n in tree.findall('./region/node/children/node') if attrs(n)['Name']=='HUM_MS_Rig_SP_CMBT_Melee_RHand_01_Attack')
   ch=n.find('children');sound=next(e for e in ch if attrs(e).get('ID')=='Whoosh_Combat')
   ch.remove(sound);ch.append(sound)
   tree.write(file,encoding='utf-8',xml_declaration=True)
   with self.assertRaisesRegex(AssertionError,'out-of-order events'):
    verify(base)
if __name__=='__main__':unittest.main()
