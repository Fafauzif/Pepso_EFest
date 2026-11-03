#!/usr/bin/env python3
"""Explicit Filebin upload with a persistent receipt; requires curl + Python3.11.

No automatic retries after an uncertain POST. Inspect receipt/server listing.
"""
import argparse,datetime,hashlib,json,secrets,subprocess,urllib.request
from pathlib import Path
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--file',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True);a=ap.parse_args()
    if a.receipt.exists():raise SystemExit('Receipt already exists; inspect it rather than duplicate an upload.')
    with a.file.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    binid=secrets.token_hex(16);url='https://filebin.net/'+binid+'/'+a.file.name
    state={'status':'starting','local_file':str(a.file.resolve()),'bin_id':binid,'bin_url':'https://filebin.net/'+binid,'download_url':url,'bytes':a.file.stat().st_size,'sha256':h,'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    a.receipt.parent.mkdir(parents=True,exist_ok=True);a.receipt.write_text(json.dumps(state,indent=2)+'\n')
    body=a.receipt.with_suffix('.response.json');headers=a.receipt.with_suffix('.headers.txt')
    cmd=['curl','--silent','--show-error','--request','POST','--upload-file',str(a.file),'--header','Content-Type: application/zip','--header','Accept: application/json','--header','Content-SHA256: '+h,'--connect-timeout','20','--max-time','900','--dump-header',str(headers),'--output',str(body),'--write-out','%{http_code} %{size_upload} %{time_total}',url]
    x=subprocess.run(cmd,text=True,capture_output=True);state.update(curl_exit=x.returncode,metrics=x.stdout,stderr=x.stderr)
    try:state['response']=json.loads(body.read_text())
    except Exception:state['response_preview']=body.read_text()[:1000] if body.exists() else None
    state['status']='post_finished_pending_verification';a.receipt.write_text(json.dumps(state,indent=2)+'\n')
    try:
        req=urllib.request.Request(state['bin_url'],headers={'Accept':'application/json'})
        with urllib.request.urlopen(req,timeout=30) as r:listing=json.load(r)
        entry=next((e for e in listing.get('files',[]) if e.get('filename')==a.file.name),None)
        state['listing']=listing;state['expiry_utc']=listing.get('bin',{}).get('expired_at')
        state['verified_size']=bool(entry and entry.get('bytes')==state['bytes']);state['verified_sha256']=bool(entry and entry.get('sha256')==h)
        req=urllib.request.Request('https://filebin.net/sha256/'+binid)
        with urllib.request.urlopen(req,timeout=30) as r:server_hashes=r.read().decode()
        state['sha256_listing']=server_hashes
        state['status']='verified_uploaded' if state['verified_size'] and state['verified_sha256'] and h in server_hashes else 'not_fully_verified'
    except Exception as e:state['verification_error']=str(e);state['status']='not_fully_verified'
    state['finished_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();a.receipt.write_text(json.dumps(state,indent=2)+'\n');print(json.dumps(state,indent=2))
    if state['status']!='verified_uploaded':raise SystemExit(2)
if __name__=='__main__':main()
