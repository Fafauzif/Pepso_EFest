#!/usr/bin/env python3
"""Resumable public TAR pagination collector. Four workers, stop429, no auth/paid service.
Reuses baseline raw pages; targeted histories have explicit source-displayed count bounds.
"""
import argparse,concurrent.futures,csv,datetime,hashlib,json,math,re,shutil,threading,time,urllib.error,urllib.request
from pathlib import Path
from lxml import html
B=Path(__file__).resolve().parents[1]; OLD=B.parent/'access_reviews'; STOP=threading.Event()

def stamp():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def extract(b,pid,page,product,raw,when):
 d=html.fromstring(b.decode("utf-8"));out=[]
 for i,e in enumerate(d.xpath('//*[@itemprop="reviewBody"]')):
  card=e
  while card is not None and not (card.tag=='div' and card.get('class')=='card mt-3'):card=card.getparent()
  if card is None:continue
  text=e.text_content().strip();ids=card.xpath('.//a[@data-id]/@data-id');rid=ids[0] if ids else hashlib.sha256((pid+text).encode()).hexdigest()[:16]
  full=' '.join(card.text_content().split());age=re.search(r'Usia\s*:\s*(\d+)\s*tahun',full)
  rev=re.search(r'Diulas:\s*(.*?)(?:Tanggal penggunaan:|[0-5]/5)',full);use=re.search(r'Tanggal penggunaan:\s*(.*?)(?:[0-5]/5)',full)
  rating=card.xpath('.//meta[@itemprop="ratingValue"]/@content');country=card.xpath('.//*[@class="card-name d-block"]/text()')
  inc='received_free_explicit' if 'Menerimanya secara gratis' in full else ('purchased_self_explicit' if any(x in full for x in ['Membelinya sendiri','Membelinya dengan uang sendiri','Dibeli sendiri']) else 'not_established')
  out.append({'record_id':'TAR-'+rid,'source_id':f'TARFULL-{pid}-p{page}','source_url':f'https://www.tryandreview.com/id/reviews/{pid}?page={page}','platform':'TryandReview','product_id':pid,'product_name':product,'review_text':text,'rating':float(rating[0]) if rating else None,'published_raw':rev[1].strip() if rev else None,'published_at_utc':None,'usage_date_raw':use[1].strip() if use else None,'profile_country_raw':country[0].strip() if country else None,'incentive_status':inc,'self_reported_age':int(age[1]) if age else None,'age_verified':False,'premium_to_basic_verified':False,'retrieved_at_utc':when,'raw_file':raw,'raw_locator':'reviewBody ordinal '+str(i),'selection_caveat':'public default pagination; current selfreported profile age/country not verified purchase demographics; no confirmed Premium-to-Basic transition'})
 return out

def fetch(task):
 target,page=task;pid=target['product_id'];u=f'https://www.tryandreview.com/id/reviews/{pid}?page={page}';name=f'tar_{pid}_p{page}.html';p=B/'raw'/name;cp=B/'clean'/'pages'/f'{pid}_{page}.json';lp=B/'raw'/f'{pid}_{page}_log.json'
 if cp.exists() and lp.exists():return json.loads(lp.read_text()),json.loads(cp.read_text())
 if STOP.is_set():return {'source_id':f'TARFULL-{pid}-p{page}','url':u,'status':'skipped_after429'},[]
 now=stamp();reused=False
 try:
  if not p.exists() and (OLD/'raw'/name).exists():shutil.copy2(OLD/'raw'/name,p);reused=True
  if not p.exists():
   time.sleep(.3)
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (compatible; public research)'}),timeout=16) as r:b=r.read(5*1024*1024)
   p.write_bytes(b)
  else:b=p.read_bytes()
  rows=extract(b,pid,page,target['product_name'],str(p.relative_to(B)),now)
  nextpages=html.fromstring(b).xpath('//*[@class="more-review"]/@data-next-page')
  log={'source_id':f'TARFULL-{pid}-p{page}','url':u,'status':'success','page':page,'product_id':pid,'product_name':target['product_name'],'retrieved_at_utc':now,'baseline_cache_reused':reused,'raw_file':str(p.relative_to(B)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'rows':len(rows),'next_page_displayed':nextpages}
  cp.write_text(json.dumps(rows,ensure_ascii=False,indent=2));lp.write_text(json.dumps(log,indent=2));return log,rows
 except urllib.error.HTTPError as e:
  if e.code==429:STOP.set()
  log={'source_id':f'TARFULL-{pid}-p{page}','url':u,'status':'failed','error':str(e),'http_status':e.code,'retrieved_at_utc':now}
 except Exception as e:log={'source_id':f'TARFULL-{pid}-p{page}','url':u,'status':'failed','error':type(e).__name__+': '+str(e),'retrieved_at_utc':now}
 lp.write_text(json.dumps(log,indent=2));return log,[]

def main():
 (B/'clean'/'pages').mkdir(exist_ok=True)
 targets=json.loads((B/'targets.json').read_text());tasks=[(t,p) for t in targets for p in range(1,math.ceil(t['displayed_review_count']/5)+1)]
 rows=[];logs=[];done=0
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  fut=[pool.submit(fetch,t) for t in tasks]
  for f in concurrent.futures.as_completed(fut):
   l,r=f.result();logs.append(l);rows.extend(r);done+=1
   if done%25==0:print(json.dumps({'pages_done':done,'pages_total':len(tasks),'records_so_far':len(rows),'stop429':STOP.is_set()}),flush=True)
 out=list({r['record_id']:r for r in rows}.values());out.sort(key=lambda x:(x['product_id'],int(x['record_id'].split('-')[-1],16) if False else x['record_id']))
 (B/'clean'/'tryandreview_reviews.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 with (B/'clean'/'tryandreview_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
 (B/'source_register.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
 oldids={r['record_id'] for r in json.loads((OLD/'clean'/'tryandreview_reviews.json').read_text())}
 summary={'requested_pages':len(tasks),'successful_pages':sum(x['status']=='success' for x in logs),'raw_record_occurrences':len(rows),'unique_records':len(out),'baseline_overlap_records':sum(r['record_id'] in oldids for r in out),'net_new_record_ids':sum(r['record_id'] not in oldids for r in out),'stopped429':STOP.is_set(),'target_count':len(targets),'target_displayed_total':sum(t['displayed_review_count'] for t in targets)}
 (B/'quality_report.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
