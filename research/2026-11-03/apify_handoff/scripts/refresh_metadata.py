"""Public GET-only Apify actor metadata/schema refresh. Never starts actors."""
import json,pathlib,urllib.request,datetime
b=pathlib.Path(__file__).resolve().parents[1]
actors={'xquik':'xquik~x-tweet-scraper','scrapewise':'scrapewise~shopee-reviews-scraper','clockworks':'clockworks~tiktok-comments-scraper'}
log=[]
for name,actor in actors.items():
 for part,endpoint in [('actor',''),('build','/builds/default')]:
  u=f'https://api.apify.com/v2/acts/{actor}{endpoint}'
  try:
   r=urllib.request.urlopen(u,timeout=25);raw=r.read();(b/'raw'/f'{name}_{part}_refreshed.json').write_bytes(raw);d=json.loads(raw)['data'];s=d.get('inputSchema')
   if s:(b/'schemas'/f'{name}_input_schema_refreshed.json').write_text(json.dumps(json.loads(s) if isinstance(s,str) else s,indent=2))
   log.append({'name':name,'part':part,'url':u,'status':r.status,'bytes':len(raw),'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actor_executed':False})
  except Exception as e:log.append({'name':name,'url':u,'error':str(e),'actor_executed':False})
(b/'refresh_log.json').write_text(json.dumps(log,indent=2))
print('Public metadata GET requests completed; no paid job started.')
