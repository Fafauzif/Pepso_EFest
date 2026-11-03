#!/usr/bin/env python3
"""Rebuild/resume the exact finalized snapshot from its eight canonical inputs.
No network, actor, source mutation or package installation. Stdlib only.
"""
import argparse,json,pathlib,sys
import corpus_store as c
b=pathlib.Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--max-records',type=int,default=1000000);p.add_argument('--export',action='store_true',help='Write compressed portable exports after successful integrity check');a=p.parse_args()
 manifest=json.loads((b/'docs/snapshot_inputs.json').read_text());paths=[b.parent/x for x in manifest['ready_ingested']]
 missing=[str(x)for x in paths if not x.is_file()]
 if missing:p.error('Missing canonical inputs: '+str(missing))
 dbp=b/'work/corpus.sqlite';db=c.dbopen(dbp);report=c.ingest(db,paths,a.max_records,1000);integrity=db.execute('PRAGMA integrity_check').fetchall()
 if integrity!=[('ok',)]:raise RuntimeError('Derived database failed integrity check; preserve source inputs and rebuild work state: '+str(integrity[:3]))
 result={'ingestion':report,'integrity_check':'ok','stats':c.stats(db,dbp)}
 if a.export:result['exported']=c.export(db,b/'clean/export')
 (b/'clean/rebuild_report.json').write_text(json.dumps(result,indent=2)+'\n');(b/'clean/collection_stats.json').write_text(json.dumps(result['stats'],indent=2)+'\n');db.close();print(json.dumps({'integrity':'ok','unique_records':result['stats']['unique_platform_records'],'source_observations':result['stats']['source_observations'],'exported':result.get('exported')},indent=2))
if __name__=='__main__':main()
