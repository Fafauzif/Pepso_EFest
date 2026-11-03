#!/usr/bin/env python3
"""Public paginated reviews form endpoint; preserve incentive and self-reported age labels."""
import concurrent.futures,csv,datetime,hashlib,json,re,urllib.request
from pathlib import Path
from lxml import html
B=Path(__file__).resolve().parents[1]
PRODUCTS={'59741':'Pepsodent Pasta Gigi Pencegah Gigi Berlubang','23607':'Pepsodent Complete 8 Multi Protection'}
def fetch(t):
 pid,page=t;u=f'https://www.tryandreview.com/id/reviews/{pid}?page={page}';p=B/'raw'/f'tar_{pid}_p{page}.html';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  if not p.exists():
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=12) as r:b=r.read()
   p.write_bytes(b)
  b=p.read_bytes();d=html.fromstring(b);out=[]
  for i,e in enumerate(d.xpath('//*[@itemprop="reviewBody"]')):
   card=e
   while card is not None and not (card.tag=='div' and card.get('class')=='card mt-3'):card=card.getparent()
   if card is None:continue
   text=e.text_content().strip();ids=card.xpath('.//a[@data-id]/@data-id');rid=ids[0] if ids else hashlib.sha256(text.encode()).hexdigest()[:16]
   full=' '.join(card.text_content().split());age=re.search(r'Usia\s*:\s*(\d+)\s*tahun',full)
   reviewdate=re.search(r'Diulas:\s*(.*?)(?:Tanggal penggunaan:|[0-5]/5)',full)
   use=re.search(r'Tanggal penggunaan:\s*(.*?)(?:[0-5]/5)',full)
   rating=card.xpath('.//meta[@itemprop="ratingValue"]/@content')
   incentive='received_free_explicit' if 'Menerimanya secara gratis' in full else ('purchased_self_explicit' if any(x in full for x in ['Membelinya sendiri','Membelinya dengan uang sendiri','Dibeli sendiri']) else 'not_established')
   out.append({'record_id':'TAR-'+rid,'source_id':'TAR-'+pid+'-p'+str(page),'source_url':u,'platform':'TryandReview Indonesia','product_name':PRODUCTS[pid],'review_text':text,'rating':rating[0] if rating else None,'published_raw':reviewdate[1].strip() if reviewdate else None,'usage_date_raw':use[1].strip() if use else None,'incentive_status':incentive,'self_reported_age':int(age[1]) if age else None,'age_verified':False,'premium_to_basic_verified':False,'retrieved_at_utc':now,'raw_file':str(p.relative_to(B)),'raw_locator':'reviewBody ordinal '+str(i),'selection_caveat':'first10 pagination pages, newest/default ordering; incentivized where marked; selfreported age is current profile not verified purchase age'})
  return {'url':u,'status':'success','rows':len(out),'retrieved_at_utc':now,'sha256':hashlib.sha256(b).hexdigest(),'raw_file':str(p.relative_to(B))},out
 except Exception as e:return {'url':u,'status':'failed','error':str(e)},[]
rows=[];logs=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for l,r in pool.map(fetch,[(k,p) for k in PRODUCTS for p in range(1,11)]):logs.append(l);rows.extend(r)
out=list({r['record_id']:r for r in rows}.values())
(B/'clean'/'tryandreview_reviews.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
if out:
 with (B/'clean'/'tryandreview_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
(B/'tryandreview_collection_log.json').write_text(json.dumps(logs,indent=2))
print({'raw':len(rows),'unique':len(out),'pages':len(logs),'successful':sum(x['status']=='success' for x in logs)})
