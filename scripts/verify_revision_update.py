from pathlib import Path
import hashlib,json,zipfile
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'release/REVISION_UPDATE_2026-11-05.json').read_text())
for row in m['files']:
 p=r/row['path']
 assert p.is_file(),str(p)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],str(p)
f=json.loads((r/'research/2026-11-05/revision/finance/finance.json').read_text())
b=f['cases']['base']['summary']
assert abs(b['operating_surplus_after_launch']-b['ending_working_capital']-b['cumulative_cash_after_launch'])<.01
assert b['npv']>0 and b['payback_quarter']==11
with zipfile.ZipFile(r/'research/2026-11-05/revision/documents/Pepsodent_Executive_Summary_Revised.docx') as z:assert z.testzip() is None
print('Verified current revision files, DOCX integrity and principal financial reconciliation. This does not validate assumed uptake or margins.')
