"""Bounded unauthenticated public-page tests. No private/session/cookie import or bypass."""
import urllib.request,urllib.parse,json,datetime,concurrent.futures,hashlib
from pathlib import Path
b=Path(__file__).resolve().parents[1]
jobs=[
('x_search','https://x.com/search?q=pepsodent&src=typed_query&f=live'),
('x_brand','https://x.com/tanyapepsodent'),
('x_brand_alternate_name','https://x.com/PepsodentID'),
('syndication_profile','https://syndication.twitter.com/srv/timeline-profile/screen-name/tanyapepsodent'),
('nitter_search','https://nitter.net/search?f=tweets&q=pepsodent'),
('xcancel_search','https://xcancel.com/search?f=tweets&q=pepsodent'),
('twscrape_login_source','https://raw.githubusercontent.com/vladkens/twscrape/main/twscrape/login.py'),
('ntscraper_source','https://raw.githubusercontent.com/bocchilorenzo/ntscraper/main/ntscraper/nitter.py')]
def get(t):
 n,u=t;stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'PepsodentResearch/1.0 public research contact via project owner'}),timeout=18) as r:d=r.read();status=r.status;ct=r.headers.get('Content-Type','');final=r.url
 except urllib.error.HTTPError as e:d=e.read();status=e.code;ct=e.headers.get('Content-Type','');final=e.url
 except Exception as e:return {'test':n,'url':u,'status':'failed','error':str(e),'retrieved_at':stamp,'usable_records':0}
 p=b/'raw'/(n+'.txt');p.write_bytes(d);text=d.decode('utf-8','replace')
 flags=[x for x in ['Just a moment','Access Denied','Something went wrong','Rate limit','not found','Enable JavaScript','robots.txt','403 Forbidden'] if x.lower() in text.lower()]
 # Manual inspection decides whether any records exist; do not equateHTTP200 with content.
 return {'test':n,'url':u,'final_url':final,'status':status,'content_type':ct,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'raw_file':str(p.relative_to(b)),'retrieved_at':stamp,'block_or_shell_flags':flags,'usable_records':None if status==200 else 0,'inspection_required':True}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:out=list(p.map(get,jobs))
(b/'raw/public_route_tests.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
