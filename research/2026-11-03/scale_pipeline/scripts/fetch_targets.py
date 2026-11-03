#!/usr/bin/env python3
"""Bounded public-URL fetch queue. No discovery, authentication or paid endpoints.
GET-only targets JSONL: {"target_id":"...","url":"https://..."}.
Stops a host on 401/403/429. Default retries only transient 5xx/network failures.
"""
import argparse,concurrent.futures,hashlib,json,pathlib,threading,time,urllib.request,urllib.error,urllib.parse,datetime
class AllowlistRedirect(urllib.request.HTTPRedirectHandler):
 def __init__(self,hosts):self.hosts=set(hosts)
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  parsed=urllib.parse.urlsplit(newurl)
  if parsed.scheme!='https' or parsed.hostname not in self.hosts:
   raise urllib.error.HTTPError(newurl,470,'Redirect outside explicit HTTPS host allowlist',headers,fp)
  return super().redirect_request(req,fp,code,msg,headers,newurl)
class FetchQueue:
 def __init__(self,output,hosts,max_requests=20,interval=1.0,retries=1,timeout=20,max_bytes=8000000):
  self.output=pathlib.Path(output);self.output.mkdir(parents=True,exist_ok=True);self.hosts=set(hosts);self.max_requests=max_requests;self.interval=interval;self.retries=retries;self.timeout=timeout;self.max_bytes=max_bytes;self.lock=threading.Lock();self.last={};self.stopped=set();self.requests=0;self.log=self.output/'fetch_log.jsonl';self.done=set();self.opener=urllib.request.build_opener(AllowlistRedirect(self.hosts))
  if self.log.exists():
   for line in self.log.read_text().splitlines():
    try:
     r=json.loads(line)
     if r.get('status')=='ok':self.done.add(r['target_key'])
    except ValueError:pass
 def record(self,r):
  with self.lock:
   with self.log.open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
  return r
 def claim(self,host):
  with self.lock:
   if host in self.stopped:return 'host_stopped'
   if self.requests>=self.max_requests:return 'request_cap'
   wait=max(0,self.interval-(time.monotonic()-self.last.get(host,0)));self.last[host]=time.monotonic()+wait;self.requests+=1
  if wait:time.sleep(wait)
  return None
 def fetch(self,t):
  url=t['url'];u=urllib.parse.urlsplit(url);host=u.hostname or '';key=hashlib.sha256(url.encode()).hexdigest();r={'target_id':t.get('target_id'),'url':url,'target_key':key,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attempts':0}
  if key in self.done:return {**r,'status':'checkpoint_already_complete'}
  querykeys={x.casefold()for x,_ in urllib.parse.parse_qsl(u.query)}
  if u.scheme!='https' or host not in self.hosts or u.username or querykeys&{'token','api_key','apikey','access_token'}:
   safe_url=urllib.parse.urlunsplit((u.scheme,host,u.path,'[REDACTED]',''))
   return self.record({**r,'url':safe_url,'status':'rejected_url'})
  for attempt in range(self.retries+1):
   stop=self.claim(host)
   if stop:return self.record({**r,'status':stop})
   r['attempts']=attempt+1
   try:
    req=urllib.request.Request(url,headers={'User-Agent':'PepsodentCaseResearch/1.0 public research (bounded GET)'})
    with self.opener.open(req,timeout=self.timeout) as response:
     final=urllib.parse.urlsplit(response.url)
     if final.hostname not in self.hosts:return self.record({**r,'status':'redirect_outside_allowlist'})
     data=response.read(self.max_bytes+1)
     if len(data)>self.max_bytes:return self.record({**r,'status':'response_size_cap'})
     fn=key+'.body';(self.output/fn).write_bytes(data)
     return self.record({**r,'status':'ok','http_status':response.status,'raw_file':fn,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'content_type':response.headers.get('Content-Type')})
   except urllib.error.HTTPError as e:
    r['http_status']=e.code
    if e.code in (401,403,429):
     with self.lock:self.stopped.add(host)
     return self.record({**r,'status':'host_stopped_access_or_rate_limit','retry_after':e.headers.get('Retry-After') if e.headers else None})
    if e.code<500:return self.record({**r,'status':'http_error'})
    r['error']=str(e)
   except (TimeoutError,OSError,urllib.error.URLError) as e:r['error']=str(e)
   if attempt<self.retries:time.sleep(min(15,2**attempt))
  return self.record({**r,'status':'failed_after_bounded_retries'})
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('targets',type=pathlib.Path);ap.add_argument('--allow-host',action='append',required=True);ap.add_argument('--out',type=pathlib.Path,required=True);ap.add_argument('--max-requests',type=int,default=20);ap.add_argument('--workers',type=int,default=2);ap.add_argument('--interval',type=float,default=1);ap.add_argument('--retries',type=int,default=1);args=ap.parse_args()
 if not 1<=args.workers<=4 or args.max_requests<1 or args.interval<.5 or not 0<=args.retries<=2:ap.error('workers1–4, maxrequests>=1, interval>=.5seconds, retries0–2')
 q=FetchQueue(args.out,args.allow_host,args.max_requests,args.interval,args.retries)
 # Bounded submission: executor.map input is batched so target files can be large.
 with args.targets.open() as f,concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
  batch=[]
  for line in f:
   if not line.strip():continue
   batch.append(json.loads(line))
   if len(batch)>=args.workers*2:
    for r in pool.map(q.fetch,batch):print(json.dumps(r,ensure_ascii=False))
    batch=[]
    if q.requests>=q.max_requests:break
  for r in pool.map(q.fetch,batch):print(json.dumps(r,ensure_ascii=False))
 print(json.dumps({'network_requests_attempted':q.requests,'stopped_hosts':sorted(q.stopped),'note':'Target completion log is resumable; stopped hosts require diagnosis, not access bypass.'}))
if __name__=='__main__':main()
