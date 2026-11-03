#!/usr/bin/env python3
"""Build the complete portable private-team snapshot; never touches .git/remote."""
import argparse,hashlib,json,shutil,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'research/2026-11-03/scale_discovery/raw/74xrbd4vxy_Raw_Dataset.csv','research/2026-11-03/scale_discovery/raw/574v66hf2v_PRDECT-ID_Dataset.csv'}
LIMIT=45*1024*1024
PART=32*1024*1024
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def allowed(p):
    rel=p.relative_to(ROOT)
    return visible(rel) and not(any(x in {'.git','__pycache__','.pytest_cache','.venv','node_modules'} for x in rel.parts) or 'scale_pipeline/work/' in rel.as_posix() or rel.as_posix() in EXCLUDED or p.suffix=='.pyc' or p.name=='.env' or p.name.startswith('.env.'))
def visible(rel):
    return not any(x.startswith('.') and x not in {'.gitignore','.gitattributes'} for x in rel.parts)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--stage',type=Path,required=True);ap.add_argument('--previous-zip',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--stage-only',action='store_true');a=ap.parse_args()
    stage=a.stage.resolve();stage.mkdir(parents=True,exist_ok=True)
    if (stage/'Pepso_EFest').exists():shutil.rmtree(stage/'Pepso_EFest')
    dest=stage/'Pepso_EFest';dest.mkdir()
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and allowed(p):
            target=dest/p.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
    release=dest/'release';release.mkdir(exist_ok=True)
    entries=[]
    for p in sorted(dest.rglob('*')):
        if not p.is_file() or not visible(p.relative_to(dest)) or p.stat().st_size<LIMIT:continue
        rel=p.relative_to(dest).as_posix();h=sha(p);e={'path':rel,'bytes':p.stat().st_size,'sha256':h,'parts':[]}
        folder=release/'large_file_parts'/h;folder.mkdir(parents=True,exist_ok=True)
        with p.open('rb') as src:
            i=0
            while b:=src.read(PART):
                part=folder/f'part-{i:04d}.bin';part.write_bytes(b);e['parts'].append({'path':part.relative_to(dest).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()});i+=1
        p.unlink();entries.append(e)
    (release/'LARGE_FILES.json').write_text(json.dumps({'format':'lossless_concatenated_byte_parts_v1','part_maximum_bytes':PART,'restore_command':'python scripts/restore_large_files.py','note':'These legacy compressed exports are represented by exact byte parts. New integrated data are independently readable record-aware gzip shards. Original source bytes are preserved through exact reconstruction.','files':entries},indent=2)+'\n')
    with (dest/'.gitignore').open('a') as f:
        f.write('\n# Exact legacy restores are optional local caches; portable parts are tracked.\n')
        for e in entries:f.write('/'+e['path']+'\n')
        f.write('*.zip\n*.sqlite\n*.sqlite-*\n')
    oldcoverage=[];chunkmap={e['path']:e for e in entries}
    with zipfile.ZipFile(a.previous_zip) as z:
        for info in z.infolist():
            if info.is_dir():continue
            rel=info.filename.removeprefix('Pepso_EFest/');expected=hashlib.sha256(z.read(info)).hexdigest();p=dest/rel
            if rel=='MANIFEST.sha256':status='updated_release_manifest'
            elif p.exists():status='identical' if sha(p)==expected else 'updated_with_history_retained_or_derived'
            elif rel in chunkmap:
                assert chunkmap[rel]['sha256']==expected,(rel,'legacy byte reconstruction differs');status='exact_bytes_in_lossless_parts'
            else:raise AssertionError('Missing previous-release member: '+rel)
            oldcoverage.append({'path':rel,'previous_bytes':info.file_size,'previous_sha256':expected,'treatment':status})
    (release/'PREVIOUS_RELEASE_COVERAGE.json').write_text(json.dumps({'previous_zip_bytes':a.previous_zip.stat().st_size,'previous_zip_sha256':sha(a.previous_zip),'entries':oldcoverage,'missing_previous_members':0},indent=2)+'\n')
    info={'release_date':'2026-11-03','timezone':'Asia/Jakarta','baseline_commit':'423cce08921b611fd01fbf6d25a0f86b65986f76','remote_head_verified_same':True,'visibility_intent':'private_team','file_size_target_bytes':LIMIT,'large_logical_files_in_parts':len(entries),'git_lfs_required':False,'remote_push':False,'previous_release_coverage':len(oldcoverage),'excluded':sorted(EXCLUDED)+['.git/**','**/__pycache__/**','scale_pipeline/work/**','credentials/environments/caches'],'canonical_written_inventory':json.loads((dest/'research/2026-11-03/closure/integrated/INVENTORY.json').read_text())['written_records_all_retained_scopes']}
    (release/'RELEASE_INFO.json').write_text(json.dumps(info,indent=2)+'\n')
    (stage/'READ_BEFORE_COPYING.md').write_text('# Install this update\n\n1. Extract this ZIP outside your existing clone.\n2. Open the extracted Pepso_EFest folder. Copy its CONTENTS into your existing Pepso_EFest repository root; replace overlaps. Do not create Pepso_EFest/Pepso_EFest.\n3. Read START_HERE.md and release/INSTALL_WITH_GITHUB_DESKTOP.md.\n4. Review changes in GitHub Desktop, commit, and push to your private team repository. The assistant has not pushed.\n\nDo not copy the outer ZIP into the repository. All data needed for the new analysis are in portable shards. Five large legacy files are losslessly represented as parts; optional restore instructions are included. There are no required deletions from the original verified baseline.\n')
    files=sorted(p for p in dest.rglob('*') if p.is_file() and visible(p.relative_to(dest)) and p.name!='MANIFEST.sha256')
    assert all(p.stat().st_size<LIMIT for p in files),[(str(p),p.stat().st_size) for p in files if p.stat().st_size>=LIMIT]
    file_inventory=[{'path':p.relative_to(dest).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files if p!=release/'FILE_INVENTORY.json']
    (release/'FILE_INVENTORY.json').write_text(json.dumps({'files':file_inventory,'excludes_from_self_listing':['release/FILE_INVENTORY.json','MANIFEST.sha256']},indent=2)+'\n')
    files=sorted(p for p in dest.rglob('*') if p.is_file() and visible(p.relative_to(dest)) and p.name!='MANIFEST.sha256')
    (dest/'MANIFEST.sha256').write_text(''.join(sha(p)+'  '+p.relative_to(dest).as_posix()+'\n' for p in files))
    summary={'stage':str(dest),'files':len(files)+1,'bytes':sum(p.stat().st_size for p in files)+(dest/'MANIFEST.sha256').stat().st_size,'maximum_file_bytes':max(p.stat().st_size for p in files),'legacy_parts_files':len(entries),'previous_members':len(oldcoverage),'previous_missing':0,'repo_size_under_1GB':sum(p.stat().st_size for p in files)<1_000_000_000}
    if not a.stage_only:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(a.output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
            # Freeze the authoritative list; never sweep in transient cache writes.
            for p in files+[dest/'MANIFEST.sha256',stage/'READ_BEFORE_COPYING.md']:
                z.write(p,p.relative_to(stage).as_posix())
        with zipfile.ZipFile(a.output) as z:assert z.testzip() is None
        summary.update(zip_path=str(a.output),zip_bytes=a.output.stat().st_size,zip_sha256=sha(a.output))
    (a.output.parent/'FINAL_RELEASE_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
