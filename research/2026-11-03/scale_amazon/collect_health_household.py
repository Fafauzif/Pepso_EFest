"""Stream original public McAuley dataset; retain title-identified toothpaste only.
No source totals are relabeled retained toothpaste reviews. No Indonesia inference.
"""
from pathlib import Path
from datetime import datetime,timezone
import urllib.request,json,re,time,hashlib,csv,gzip
ROOT=Path(__file__).parent/'health_household'; ROOT.mkdir(exist_ok=True); (ROOT/'clean').mkdir(exist_ok=True); (ROOT/'raw').mkdir(exist_ok=True)
BASE='https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023/resolve/main/raw/'
meta_url=BASE+'meta_categories/meta_Health_and_Household.jsonl'
rev_url=BASE+'review_categories/Health_and_Household.jsonl'
START=datetime.now(timezone.utc).isoformat(); logs=[];products={}
pattern=re.compile(r'\b(tooth\s?paste|dentifrice|sensodyne|pepsodent)\b',re.I)
def consume(url,kind,callback,cap):
 n=0;b=0;h=hashlib.sha256();t=time.monotonic()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'AcademicOralCareResearch/1.0 public dataset analysis'})
  with urllib.request.urlopen(req,timeout=25) as response:
   for line in response:
    h.update(line);b+=len(line);n+=1
    try: obj=json.loads(line)
    except Exception: continue
    callback(obj,n)
    if n%50000==0: print(kind,'scanned',n,'retained_products',len(products),flush=True)
    if n>=cap:break
  logs.append(dict(url=url,kind=kind,scanned_rows=n,bytes_read=b,sha256_of_read_bytes=h.hexdigest(),elapsed_seconds=time.monotonic()-t,cap=cap,status='complete' if n<cap else 'cap_reached',retrieved_at_utc=START))
 except Exception as e:
  logs.append(dict(url=url,kind=kind,scanned_rows=n,bytes_read=b,status='error',error=str(e),elapsed_seconds=time.monotonic()-t,retrieved_at_utc=START))
 (ROOT/'access_log.json').write_text(json.dumps(logs,indent=2))
with (ROOT/'raw/toothpaste_metadata.jsonl').open('w') as out:
 def meta(o,n):
  if pattern.search(o.get('title','')):
   key=o.get('parent_asin');products[key]=o; out.write(json.dumps({'source_line':n,'data':o},ensure_ascii=False)+'\n')
 consume(meta_url,'metadata',meta,1000000)
(ROOT/'clean/products.json').write_text(json.dumps(products,indent=2,ensure_ascii=False))
count=0
with gzip.open(ROOT/'raw/toothpaste_reviews.jsonl.gz','wt',encoding='utf-8') as raw,gzip.open(ROOT/'clean/reviews.jsonl.gz','wt',encoding='utf-8') as out:
 def review(o,n):
  global count
  p=products.get(o.get('parent_asin'))
  if not p:return
  count+=1;raw.write(json.dumps({'source_line':n,'data':o},ensure_ascii=False)+'\n')
  stamp=o.get('timestamp');date=datetime.fromtimestamp(stamp/1000,timezone.utc).isoformat() if stamp else None
  v=dict(record_id='AMZ-HH-'+hashlib.sha256((str(o.get('user_id'))+'|'+str(o.get('parent_asin'))+'|'+str(stamp)+'|'+o.get('text','')).encode()).hexdigest()[:24],source_id='MCAULEY-AMAZON2023-HH',source_url=rev_url,platform='Amazon historical research dataset',product_id=o.get('parent_asin'),product_name=p.get('title'),review_text=o.get('text'),review_title=o.get('title'),rating=o.get('rating'),published_at_utc=date,retrieved_at_utc=START,source_line=n,raw_file='raw/toothpaste_reviews.jsonl.gz',scope='non_Indonesia_historical_context',age_verified=False,premium_to_basic_verified=False,incentive_status='unknown',original_verified_purchase=o.get('verified_purchase'),country_evidence='Amazon source; country not verified; not Indonesia consumer evidence')
  out.write(json.dumps(v,ensure_ascii=False)+'\n')
 consume(rev_url,'reviews',review,30000000)
(ROOT/'summary.json').write_text(json.dumps(dict(source='McAuley-Lab/Amazon-Reviews-2023',category='Health_and_Household',products_retained=len(products),reviews_retained=count,logs=logs,scope='separate international historical comparator; no Indonesia/Pepsodent-switcher inference',cost_usd=0),indent=2))
print('FINISHED',len(products),'products',count,'reviews',flush=True)
