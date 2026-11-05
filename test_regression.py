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
class VoiceRegression(unittest.TestCase):
 def mutate_and_reject(self,change):
  with tempfile.TemporaryDirectory(prefix='weapon-voice-test-') as folder:
   base=pathlib.Path(folder)/'src';shutil.copytree(ROOT/'src',base)
   file=base/'Public/WeaponSFXRepair/Content/[PAK]_WeaponSFXRepair/_merged.lsx'
   tree=ET.parse(file);change(tree)
   tree.write(file,encoding='utf-8',xml_declaration=True)
   with self.assertRaises(AssertionError):verify(base)
 def test_missing_voice_is_rejected(self):
  def change(tree):
   n=tree.find('./region/node/children/node');ch=n.find('children')
   ch.remove(next(e for e in ch if attrs(e).get('TextKeyType')=='13'))
  self.mutate_and_reject(change)
 def test_wrong_voice_emitter_is_rejected(self):
  def change(tree):
   n=next(e for e in tree.findall('.//node[@id="Events"]') if attrs(e).get('TextKeyType')=='13')
   n.find('./children/node/attribute[@id="SoundObjectIndex"]').set('value','1')
  self.mutate_and_reject(change)
 def test_gameplay_event_timing_change_is_rejected(self):
  def change(tree):
   n=next(e for e in tree.findall('.//node[@id="Events"]') if attrs(e).get('TextKeyType')=='8')
   a=n.find('attribute[@id="Time"]');a.set('value',str(float(a.get('value'))+0.001))
  self.mutate_and_reject(change)
 def test_missing_throw_sound_is_rejected(self):
  def change(tree):
   for n in tree.findall('./region/node/children/node'):
    ch=n.find('children')
    e=next((e for e in ch if attrs(e).get('ID')=='Whoosh_Throw'),None)
    if e is not None:ch.remove(e);return
   raise AssertionError('No throw sound in release fixture')
  self.mutate_and_reject(change)
if __name__=='__main__':unittest.main()
