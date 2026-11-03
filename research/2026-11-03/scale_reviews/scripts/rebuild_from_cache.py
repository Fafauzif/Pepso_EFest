#!/usr/bin/env python3
"""Reparse immutable fragment bytes as UTF8, reconcile source manifests, no network requests."""
import collections,csv,datetime,hashlib,importlib.util,json,math,re
from pathlib import Path
B=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('collector',Path(__file__).with_name('collect_full_tar.py'));mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
targets={r['product_id']:r for r in json.loads((B/'targets.json').read_text())}
oldlogs={r['url']:r for r in json.loads((B.parent/'access_reviews'/'tryandreview_collection_log.json').read_text())}
logs=[];rows=[];changed=0
for p in sorted((B/'raw').glob('*_log.json')):
 l=json.loads(p.read_text());mt=re.fullmatch(r'(\d+)_(\d+)_log.json',p.name);pid=l.get('product_id') or (mt[1] if mt else None);page=l.get('page') or (int(mt[2]) if mt else None)
 raw=B/'raw'/f'tar_{pid}_p{page}.html'
 if pid not in targets or not raw.exists():logs.append(l);continue
 if l.get('status')!='success':l['original_parse_error']=l.get('error');l['status']='success';l['recovered_from_raw_cache']=True
 l['product_id']=pid;l['page']=page;l['product_name']=targets[pid]['product_name'];l['raw_file']=str(raw.relative_to(B));l['bytes']=len(raw.read_bytes());l['sha256']=hashlib.sha256(raw.read_bytes()).hexdigest();when=l['retrieved_at_utc']
 if l.get('baseline_cache_reused') and l['url'] in oldlogs:when=oldlogs[l['url']]['retrieved_at_utc'];l['raw_first_collected_at_utc']=when
 rr=mod.extract(raw.read_bytes(),pid,page,targets[pid]['product_name'],l['raw_file'],when)
 cp=B/'clean'/'pages'/f'{pid}_{page}.json'
 old={r['record_id']:r for r in json.loads(cp.read_text())} if cp.exists() else {}
 for r in rr:
  if r['record_id'] in old and r['review_text']!=old[r['record_id']]['review_text']:changed+=1
  r['parser_encoding']='UTF-8 explicit; raw unchanged'
 cp.write_text(json.dumps(rr,ensure_ascii=False,indent=2));rows.extend(rr);l['parser_encoding']='UTF-8 explicit';l['rows']=len(rr);logs.append(l)
out=list({r['record_id']:r for r in rows}.values());out.sort(key=lambda x:(x['product_id'],x['record_id']))
(B/'clean'/'tryandreview_reviews.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
if out:
 with (B/'clean'/'tryandreview_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
(B/'source_register.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
oldids={r['record_id'] for r in json.loads((B.parent/'access_reviews'/'clean'/'tryandreview_reviews.json').read_text())}
by=[]
for pid,t in targets.items():
 pp=[l for l in logs if l.get('product_id')==pid and l.get('status')=='success'];rr=[r for r in out if r['product_id']==pid];expected=math.ceil(t['displayed_review_count']/5)
 by.append({'product_id':pid,'product_name':t['product_name'],'source_displayed_count':t['displayed_review_count'],'expected_pages':expected,'successful_pages':len(pp),'distinct_review_ids':len(rr),'count_reconciles':len(rr)==t['displayed_review_count'],'page_numbers_complete':{l['page'] for l in pp}==set(range(1,expected+1))})
report={'target_count':len(targets),'requested_pages':sum(math.ceil(t['displayed_review_count']/5) for t in targets.values()),'successful_pages':sum(l['status']=='success' for l in logs),'raw_record_occurrences':len(rows),'unique_records':len(out),'baseline_overlap_records':sum(r['record_id'] in oldids for r in out),'net_new_record_ids':sum(r['record_id'] not in oldids for r in out),'target_displayed_total':sum(t['displayed_review_count'] for t in targets.values()),'rating_counts':dict(collections.Counter(r['rating'] for r in out)),'incentive_counts':dict(collections.Counter(r['incentive_status'] for r in out)),'profile_country_counts':dict(collections.Counter(r['profile_country_raw'] for r in out)),'UTF8_text_repairs_this_rebuild':changed,'per_product':by,'interpretation':'enumerated public pages; count reconciliation does not establish unique people, representativeness, or unchanged point-in-time universe'}
(B/'quality_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
