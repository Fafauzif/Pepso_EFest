#!/usr/bin/env python3
"""Losslessly archive user uploads. Stdlib; never edits originals."""
import argparse, gzip, hashlib, json, shutil
from pathlib import Path

def digest(p):
    with p.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input-dir',type=Path,required=True);args=ap.parse_args()
    closure=Path(__file__).resolve().parents[1];out=closure/'raw/user_runs';out.mkdir(parents=True,exist_ok=True)
    records=[]
    for src in sorted(args.input_dir.iterdir()):
        if not src.is_file():continue
        dst=out/(src.name+'.gz') if src.suffix=='.json' else out/src.name
        if src.suffix=='.json':
            with src.open('rb') as fi,dst.open('wb') as fo,gzip.GzipFile(filename='',mode='wb',fileobj=fo,mtime=0,compresslevel=9) as z:shutil.copyfileobj(fi,z)
            with gzip.open(dst,'rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==digest(src)
        else:shutil.copyfile(src,dst)
        disposition='source_input'
        if 'shopee' in src.name:disposition='excluded_from_case_analysis_error_or_wrong_target_retained_for_audit'
        records.append({'original_filename':src.name,'original_bytes':src.stat().st_size,'original_sha256':digest(src),'archive_path':dst.relative_to(closure).as_posix(),'archive_bytes':dst.stat().st_size,'archive_sha256':digest(dst),'encoding':'gzip_exact_original_bytes' if src.suffix=='.json' else 'unchanged','disposition':disposition})
    (closure/'raw/UPLOAD_REGISTER.json').write_text(json.dumps({'archived_at':'2026-11-03','provenance':'User attachments from this conversation; originals unchanged; gzip decompresses to exact uploaded bytes. JSON locators are zero-based array indices unless source analysis states otherwise.','files':records},indent=2)+'\n')
    print(json.dumps({'files':len(records),'original_bytes':sum(x['original_bytes'] for x in records),'archive_bytes':sum(x['archive_bytes'] for x in records)}))
if __name__=='__main__':main()
