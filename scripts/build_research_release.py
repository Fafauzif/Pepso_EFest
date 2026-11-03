"""Package team-private repo snapshot without git/auth/tool environments or rebuildable DB."""
from pathlib import Path
import hashlib,json,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'deliverables'; OUT.mkdir(exist_ok=True)
EXCLUDE={
'research/2026-11-03/scale_discovery/raw/74xrbd4vxy_Raw_Dataset.csv',
'research/2026-11-03/scale_discovery/raw/574v66hf2v_PRDECT-ID_Dataset.csv',
}
def allowed(p):
 rel=p.relative_to(ROOT)
 return not(any(x in {'.git','__pycache__'} for x in rel.parts) or 'scale_pipeline/work/' in rel.as_posix() or rel.as_posix() in EXCLUDE or p.suffix=='.pyc' or p.name=='.env' or p.name.startswith('.env.'))
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and allowed(p) and p.name!='MANIFEST.sha256')
large=[str(p.relative_to(ROOT)) for p in files if p.stat().st_size>95_000_000]
assert not large,large
manifest=ROOT/'MANIFEST.sha256'
manifest.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix()+'\n' for p in files))
files.append(manifest)
for src,dst in [('research/2026-11-03/REPORT_FULL.md','Pepsodent_Research_Report.md'),('research/2026-11-03/plan/PLAN_v2.md','Pepsodent_Expanded_Research_Plan.md')]:shutil.copyfile(ROOT/src,OUT/dst)
(OUT/'synthesis').mkdir(exist_ok=True);shutil.copyfile(ROOT/'research/2026-11-03/synthesis/case_unit_price.png',OUT/'synthesis/case_unit_price.png')
archive=OUT/'Pepsodent_Research_Data_and_Repo.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
 for p in files:z.write(p,'Pepso_EFest/'+p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(files)
summary={'files':len(files),'zip_bytes':archive.stat().st_size,'zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'report_words':len((OUT/'Pepsodent_Research_Report.md').read_text().split()),'source_review_rows_screened':26125466,'canonical_written_records':298846,'international_adult_title_written_candidates':196872,'excluded':sorted(EXCLUDE)+['.git/**','**/__pycache__/**','scale_pipeline/work/**','credentials/environments'],'remote_push':False}
(OUT/'release_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
