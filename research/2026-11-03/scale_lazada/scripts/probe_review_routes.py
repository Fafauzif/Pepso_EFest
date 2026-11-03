#!/usr/bin/env python3
import urllib.request,urllib.parse,json,re,hashlib,datetime
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
R=Path(__file__).resolve().parents[1]
URLS={
'lazada_public_reviewlist':'https://www.lazada.co.id/pdp/review/getReviewList?itemId=1473424890&pageSize=100&filter=0&sort=0&pageNo=2',
'lazada_public_reviewlist_www':'https://my.lazada.co.id/pdp/review/getReviewList?itemId=1473424890&pageSize=100&filter=0&sort=0&pageNo=2',
'lazada_seo_page2':'https://www.lazada.co.id/product-reviews/?item_id=1473424890&page=2',
'watsons_reviews_20231':'https://api.watsons.co.id/api/v2/wtcid/products/20231/reviews?fields=FULL&lang=id&curr=IDR&pageSize=100&currentPage=0',
'watsons_reviews_BP20231':'https://api.watsons.co.id/api/v2/wtcid/products/BP_20231/reviews?fields=FULL&lang=id&curr=IDR&pageSize=100&currentPage=0'
}
def get(t):
 key,u=t;now=datetime.datetime.now(datetime.timezone.utc).isoformat();log=dict(source_id=key,url=u,retrieved_at=now)
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (public review research)'})
  with urllib.request.urlopen(req,timeout=22) as r:b=r.read(10*1024*1024);status=r.status;content_type=r.headers.get('Content-Type')
  p=R/'raw'/f'{key}.body';p.write_bytes(b);s=b.decode('utf-8','replace');log.update(status=status,content_type=content_type,bytes=len(b),raw_file=str(p.relative_to(R)),sha256=hashlib.sha256(b).hexdigest(),body_preview=s[:300])
  if 'window.__FIRST_SCREEN_DATA=' in s:
   d=json.JSONDecoder().raw_decode(s.split('window.__FIRST_SCREEN_DATA=',1)[1])[0]
   for v in d.get('data',{}).values():
    if isinstance(v,dict) and 'reviewPage' in v:
     rr=v['reviewPage']['reviewZone']['reviews'];log['review_count']=len(rr);log['review_ids']=[x.get('reviewId') for x in rr]
 except Exception as e:log.update(error=repr(e))
 return log
x=list(ThreadPoolExecutor(3).map(get,URLS.items()));(R/'route_probe.json').write_text(json.dumps(x,ensure_ascii=False,indent=2));print(json.dumps(x,ensure_ascii=False,indent=2))
