#!/usr/bin/env python3
"""Restore exact legacy files from portable lossless parts (optional, stdlib).

New corpus shards work without this step. Legacy rebuilds may need these files.
Restored paths are ignored by Git; don't add them with git add -f.
"""
import argparse,hashlib,json,os,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--only',action='append',help='Exact repository-relative logical path; repeat for multiple files');ap.add_argument('--list',action='store_true');args=ap.parse_args()
    manifest=ROOT/'release/LARGE_FILES.json'
    if not manifest.exists():raise SystemExit('No portable part manifest here; this working tree may already contain the full legacy files.')
    entries=json.loads(manifest.read_text())['files']
    if args.list:
        for e in entries:print(e['path'],e['bytes'],e['sha256'])
        return
    if args.only:
        requested=set(args.only);known={e['path'] for e in entries}
        if requested-known:raise SystemExit('Unknown paths: '+', '.join(sorted(requested-known)))
        entries=[e for e in entries if e['path'] in requested]
    for e in entries:
        target=ROOT/e['path'];target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():
            if target.stat().st_size==e['bytes'] and sha(target)==e['sha256']:print('Already exact:',e['path']);continue
            raise SystemExit('Refusing to replace changed file: '+e['path'])
        fd,name=tempfile.mkstemp(prefix='.restore-',dir=target.parent);os.close(fd);temp=Path(name)
        try:
            with temp.open('wb') as out:
                for part in e['parts']:
                    p=ROOT/part['path']
                    if p.stat().st_size!=part['bytes'] or sha(p)!=part['sha256']:raise ValueError('Part checksum mismatch: '+part['path'])
                    with p.open('rb') as src:
                        while block:=src.read(1024*1024):out.write(block)
            if temp.stat().st_size!=e['bytes'] or sha(temp)!=e['sha256']:raise ValueError('Restored checksum mismatch: '+e['path'])
            os.replace(temp,target);print('Restored exact bytes:',e['path'])
        finally:temp.unlink(missing_ok=True)
if __name__=='__main__':main()
