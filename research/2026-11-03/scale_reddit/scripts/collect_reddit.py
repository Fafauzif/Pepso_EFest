"""Bounded, resumable public ArcticShift thread collector. No credentials or sessions.
Only known dental/consumer threads are read. Existing successful snapshots are reused.
429 stops the run; HTTP failures aren't absence. No bulk unrelated subreddit dump.
"""
import argparse,csv,datetime,hashlib,json,time,urllib.request,urllib.parse,urllib.error,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE='https://arctic-shift.photon-reddit.com'
THREADS=[('1414a8a','go-to toothpaste','dental'),('yaky59','whitening toothpaste','dental'),('1qdisen','effective whitening toothpaste','dental'),('1cylnd9','hygiene routines','mixed_context'),('1q6zrz6','rinsing after brushing','dental'),('pflmqa','dentist recommendations meme','meme_context'),('1t5cxhe','dentist recommendations meme2026','meme_context'),('1215fxx','generic brand words','mixed_context')]
THREADS += [('1k7l3ug','scaling dental visit experiences','dental'),('p61bms','oral hygiene habits poll2021','dental'),('1jntjak','Jakarta toothpaste availability','dental')]
TERMS=['odol','pasta gigi','toothpaste','pepsodent','sensodyne','enzim','ciptadent','close up','colgate','darlie','systema','zact','gigi','brushing']
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def readjson(p,default):
 try:return json.loads(p.read_text())
 except:return default

def fetch(qid,path,params,delay):
 u=BASE+path+'?'+urllib.parse.urlencode(params);p=ROOT/'raw'/(qid+'.json');lp=ROOT/'raw'/(qid+'.log.json')
 if p.exists() and lp.exists():return readjson(p,{}),readjson(lp,{})
 d={'query_id':qid,'url':u,'collected_at':now(),'params':params}
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Pepsodent-EFest-public-research/1.0'})
  with urllib.request.urlopen(req,timeout=25) as x:b=x.read();d.update(status=x.status,bytes=len(b))
  j=json.loads(b);p.write_bytes(b);d.update(outcome='retrieved',sha256=hashlib.sha256(b).hexdigest())
 except urllib.error.HTTPError as e:
  b=e.read();(ROOT/'raw'/(qid+'_error.txt')).write_bytes(b);j={};d.update(status=e.code,outcome='failed',error=b.decode(errors='replace')[:500])
 except Exception as e:j={};d.update(outcome='failed',error=str(e))
 lp.write_text(json.dumps(d,indent=2));time.sleep(delay);return j,d

def nodes(o):
 if isinstance(o,list):
  for x in o:yield from nodes(x)
 elif isinstance(o,dict):
  if o.get('kind')=='t1' and isinstance(o.get('data'),dict):
   yield o['data']
   for k in ['replies','children']:yield from nodes(o['data'].get(k,[]))
  elif 'children' in o:yield from nodes(o['children'])
  elif 'data' in o:yield from nodes(o['data'])

def main():
 a=argparse.ArgumentParser();a.add_argument('--thread-limit',type=int,default=1000);a.add_argument('--max-records',type=int,default=5000);a.add_argument('--delay',type=float,default=1.5);args=a.parse_args()
 logs=[];records={};excluded=[];threadrows=[]
 ids=','.join(x[0] for x in THREADS)
 posts,log=fetch('posts_by_ids_'+hashlib.sha256(ids.encode()).hexdigest()[:10],'/api/posts/ids',{'ids':ids,'fields':'id,title,selftext,created_utc,subreddit,num_comments'},args.delay);logs.append(log)
 postlookup={x['id']:x for x in posts.get('data',[]) if isinstance(x,dict)}
 for pid,label,context in THREADS:
  qid='tree_'+pid
  tree,log=fetch(qid,'/api/comments/tree',{'link_id':pid,'limit':min(args.thread_limit,25000),'start_breadth':100,'start_depth':30},args.delay);logs.append(log)
  if log.get('status')==429:break
  count=0;matches=0
  for i,d in enumerate(nodes(tree)):
   count+=1;body=d.get('body','');meta=d.get('_meta') or {}
   if body in ['[deleted]','[removed]',''] or d.get('author') in ['[deleted]','AutoModerator','QualityVote'] or meta.get('was_deleted_later'):
    excluded.append({'id':d.get('id'),'thread_id':pid,'reason':'deleted_removed_empty_or_moderation_bot'});continue
   terms=[t for t in TERMS if t in body.lower()]
   # Retain dental-thread context; mixed/meme threads require explicit dental keywords.
   if context!='dental' and not terms:
    excluded.append({'id':d.get('id'),'thread_id':pid,'reason':'no_dental_keyword_in_mixed_thread'});continue
   matches+=bool(terms)
   stamp=d.get('created_utc');date=datetime.datetime.fromtimestamp(stamp,datetime.timezone.utc).isoformat() if isinstance(stamp,(int,float)) else None
   scope='case_historical' if date and '2022-01-01'<=date<'2026-07-01' else 'current_context' if date and '2026-07-01'<=date<'2026-11-04' else 'outside_case'
   ident='reddit:comment:'+d['id'];post=postlookup.get(pid,{})
   records[ident]={'record_id':ident,'platform':'reddit','record_type':'comment','source_url':'https://www.reddit.com'+d.get('permalink',f'/r/indonesia/comments/{pid}/_/{d["id"]}/'),'parent_post_id':pid,'parent_id':d.get('parent_id'),'subreddit':d.get('subreddit'),'text_original':body,'title_original':post.get('title',label),'created_utc':stamp,'created_at':date,'archive_retrieved_on':d.get('retrieved_on'),'collected_at':log.get('collected_at'),'source_api_url':log.get('url'),'query_id':qid,'raw_file':'raw/'+qid+'.json','raw_record_index':i,'matched_terms':terms,'scope':scope,'context_type':context,'relevance_status':'keyword_candidate' if terms else 'dental_thread_context','live_visibility_status':'not_rechecked','age_verified':False,'premium_basic_switch_verified':False}
   if len(records)>=args.max_records:break
  more=[]
  def findmore(o):
   if isinstance(o,list):
    for x in o:findmore(x)
   elif isinstance(o,dict):
    if o.get('kind')=='more':more.append(o)
    for v in o.values():
     if isinstance(v,(dict,list)):findmore(v)
  findmore(tree)
  threadrows.append({'post_id':pid,'label':label,'context_type':context,'source_url':'https://www.reddit.com/r/indonesia/comments/'+pid,'title_original':postlookup.get(pid,{}).get('title'),'post_created_utc':postlookup.get(pid,{}).get('created_utc'),'api_comment_nodes':count,'retained_matching_count':matches,'collapsed_more_nodes':len(more),'outcome':log['outcome'],'status':log.get('status')})
  # Checkpoints survive interruption and support later resumption.
  (ROOT/'reddit_records.json').write_text(json.dumps(list(records.values()),ensure_ascii=False,indent=2));(ROOT/'collection_log.json').write_text(json.dumps(logs,indent=2));(ROOT/'threads.json').write_text(json.dumps(threadrows,ensure_ascii=False,indent=2))
  if len(records)>=args.max_records:break
 out=list(records.values());fields=list(out[0]) if out else ['record_id','platform','source_url','text_original']
 with (ROOT/'reddit_records.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for x in out:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in x.items()})
 (ROOT/'excluded.json').write_text(json.dumps(excluded,indent=2));(ROOT/'collection_summary.json').write_text(json.dumps({'thread_targets':len(THREADS),'threads_attempted':len(threadrows),'records_retained':len(out),'keyword_candidate_records':sum(x['relevance_status']=='keyword_candidate' for x in out),'context_only_records':sum(x['relevance_status']=='dental_thread_context' for x in out),'excluded_comment_nodes':len(excluded),'max_records_cap':args.max_records,'paid_spend_usd':0,'representative':False},indent=2))
 print((ROOT/'collection_summary.json').read_text())
if __name__=='__main__':main()
