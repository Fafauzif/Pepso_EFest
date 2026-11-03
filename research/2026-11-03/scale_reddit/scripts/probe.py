import urllib.request,urllib.parse,json,datetime,concurrent.futures
from pathlib import Path
r=Path(__file__).resolve().parents[1]
urls={
'arctic_posts':'https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=indonesia&query=odol&limit=5&sort=desc',
'arctic_comments':'https://arctic-shift.photon-reddit.com/api/comments/search?subreddit=indonesia&body=pepsodent&limit=5&sort=desc',
'pullpush_comments':'https://api.pullpush.io/reddit/search/comment/?subreddit=indonesia&q=pepsodent&size=5',
'arctic_docs':'https://raw.githubusercontent.com/ArthurHeitmann/arctic_shift/master/api/README.md',
'pullpush_docs':'https://pullpush.io/',
}
def get(k,u):
 d={'probe_id':k,'url':u,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Pepsodent-EFest-public-research/1.0'}),timeout=20) as resp:
   b=resp.read(); d.update(status=resp.status,bytes=len(b),content_type=resp.headers.get('Content-Type'))
  (r/'raw'/(k+'.txt')).write_bytes(b); d['success']=True
  try:d['rows']=len(json.loads(b).get('data',[]))
  except:pass
 except Exception as e:d.update(success=False,error=str(e))
 return d
log=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(lambda x:get(*x),urls.items()))
(r/'probe_log.json').write_text(json.dumps(log,indent=2));print(json.dumps(log,indent=2))
