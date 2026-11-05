"""Validate this context overlay's files and principal arithmetic, not survey truth."""
from pathlib import Path
import hashlib,json,math,zipfile
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'research/2026-11-04/survey_results'
manifest=json.loads((D/'sources/package_manifest.json').read_text())
for rec in manifest['files']:
 p=ROOT/rec['path']
 assert p.is_file(),f'Missing {p}'
 assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256'],f'Changed {p}'
read=lambda n:json.loads((D/'data/aggregates'/n).read_text())
m=read('metrics.json');p=read('paired.json');c=read('counts.json');s=read('sensitivity.json')
assert (m['submitted'],m['eligible'],m['excluded'])==(50,49,1)
assert (m['self_chooser_family_payer'],m['self_shopper_family_payer'],m['solo_living_family_payer'])==(24,25,21)
assert (p['n'],p['both'],p['other_only'],p['tooth_only'],p['neither'])==(21,10,6,3,2)
assert math.isclose(p['exact_mcnemar_p'],.5078125)
assert c['preference_code']['No specific product preference']==31
assert s['desired_preference_manual_by_availability']['EXPLICIT_NO_PREFERENCE']['Saya mendapat produk yang saya inginkan']==22
assert sum(c['reasons'].values())>49 # multiple selection, not exclusive shares
model=json.loads((D/'model/scenarios.json').read_text())
for n,x in model['scenarios'].items():
 q=model['screened_per_equivalent_arm']*x['qualified']
 first_t=q*x['first_t'];first_c=q*x['first_c']
 r_t=first_t*x['repeat_t'];r_c=first_c*x['repeat_c']
 delta=first_t+r_t-first_c-r_c
 assert math.isclose(delta,x['incremental_paid_100g_equivalents'])
 assert math.isclose(delta*x['net_contribution_per_100g']-x['program_cost'],x['net_after_program'])
 assert x['net_after_program']<0
assert math.isclose(model['scenarios']['base']['net_after_program'],-33340000)
assert math.isclose(24100/190*100,12684.21052631579)
assert math.isclose(23500/(24100/190*100),1.8526970954356847)
assert 2*4000-(1000+450)==6550 < 40000000/6000
with zipfile.ZipFile(D/'documents/Pepsodent_Executive_Summary_and_Appendices.docx') as z:
 doc=z.read('word/document.xml').decode();styles=z.read('word/styles.xml').decode()
 assert 'Menguatkan pilihan' in doc
 assert '<w:pBdr' not in doc and '<w:pBdr' not in styles
 assert len([x for x in z.namelist() if x.startswith('word/media/')])==12
# Privacy boundary: no survey exports, contact datasets, reviewer conversations or git metadata in this overlay.
for rel in manifest['files']:
 path=rel['path'].lower()
 assert not path.endswith('.xlsx')
 assert '.git/' not in path and not path.endswith('preference_coding_manifest.csv')
 assert 'review_round' not in path and 'private_working' not in path
print(f'PASS: {len(manifest["files"])} file hashes; inclusion, roles, paired counts, preference coding, case price, all scenarios, and Word media/border checks.')
print('These checks do not authenticate participants, prove treatment effects, or reproduce clinical outcomes.')
