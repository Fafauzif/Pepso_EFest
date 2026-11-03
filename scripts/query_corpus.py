#!/usr/bin/env python3
"""Stream portable corpus shards. Example: --platform tiktok --contains sensodyne."""
import argparse,gzip,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def iter_records():
    folder=ROOT/'research/2026-11-03/closure/integrated'
    inv=json.loads((folder/'INVENTORY.json').read_text())
    for item in inv['shards']:
        with gzip.open(folder/item['path'],'rt',encoding='utf-8') as f:
            for line in f:yield json.loads(line)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--platform');ap.add_argument('--contains');ap.add_argument('--limit',type=int,default=10);a=ap.parse_args();n=0
    for r in iter_records():
        if a.platform and r['platform']!=a.platform:continue
        if a.contains and a.contains.casefold() not in r['text_original'].casefold():continue
        print(json.dumps(r,ensure_ascii=False));n+=1
        if n>=a.limit:break
if __name__=='__main__':main()
