#!/usr/bin/env python3
"""Collect public scholarly metadata with original payloads and an access log. No credentials."""
import urllib.request,urllib.parse,json,concurrent.futures,hashlib,datetime,time
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];RAW=BASE/'raw';CLEAN=BASE/'clean'
for d in (RAW,CLEAN):d.mkdir(exist_ok=True,parents=True)
queries={
'sensory':'TITLE_ABS:(toothpaste AND (sensory OR taste OR mouthfeel OR foaming))',
'sls':'TITLE_ABS:(dentifrice AND sodium lauryl AND randomized)',
'hypersensitivity':'TITLE_ABS:(desensitizing toothpastes AND (meta-analysis OR scoping review))',
'preference':'TITLE_ABS:(toothpaste AND (preference OR preferences OR acceptance))',
'adherence':'TITLE_ABS:(dentin hypersensitivity AND (adherence OR discontinuation OR recurrence))',
'family':'TITLE_ABS:(toothpaste AND (household OR family OR parents))',
'packaging':'TITLE_ABS:(toothpaste AND (packaging OR portion OR amount))'}
crqueries={
'family':'Family influence on young adult brand evaluation parent children consumer packaged goods',
'unit_price':'unit price package size consumer perception small packages',
'packs':'Consumer Response to Package Downsizing Evidence Chicago Ice Cream Market',
'promo':'Long Run Effects Promotion Depth New Established Customers Three Field Studies',
'choice':'choice overload conceptual review meta analysis',
'reference':'Consumer Price and Promotion Expectations Experimental Study',
'household':'consumer competence young adults newly formed households',
'habit':'habit discontinuity context change consumer habits purchasing'}
dois=['10.1086/651235','10.1016/j.jcps.2014.08.002','10.1177/002224378802500402','10.1287/mksc.4.2.147','10.1287/mksc.1030.0040','10.1177/002224379202900108','10.1080/09593960802113752','10.1002/cb.1946','10.1007/s00784-015-1535-z','10.1177/002224379002700301','10.1016/j.jretai.2013.06.002']
jobs=[]
for key,q in queries.items():jobs.append(('epmc_'+key,'https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q+' AND FIRST_PDATE:[1900-01-01 TO 2026-11-03]','format':'json','pageSize':20,'resultType':'core'})))
for key,q in crqueries.items():jobs.append(('crossref_search_'+key,'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':q,'rows':5,'filter':'until-pub-date:2026-11-03'})))
for i,doi in enumerate(dois):jobs.append((f'crossref_doi_{i:02d}','https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')))
jobs.append(('pmc_sls_fulltext','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4799265/fullTextXML'))
log=[]; candidates=[]
def fetch(job):
 key,url=job;stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.time()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'PepsodentResearch/1.0 (academic literature review)'})
  with urllib.request.urlopen(req,timeout=35) as r:b=r.read();status=r.status;ct=r.headers.get('Content-Type','')
  ext='.json' if 'json' in ct else '.xml';p=RAW/(key+ext);p.write_bytes(b)
  return {'key':key,'url':url,'retrieved_at':stamp,'status':status,'content_type':ct,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'raw_file':str(p.relative_to(BASE)),'elapsed_seconds':round(time.time()-start,2)},b
 except Exception as e:return {'key':key,'url':url,'retrieved_at':stamp,'status':'failed','error':str(e),'elapsed_seconds':round(time.time()-start,2)},None
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for entry,b in pool.map(fetch,jobs):
  log.append(entry)
  if b and entry['raw_file'].endswith('.json'):
   data=json.loads(b)
   if entry['key'].startswith('epmc'):
    for i,x in enumerate(data.get('resultList',{}).get('result',[])):
     candidates.append({'source_query':entry['key'],'record_locator':f'resultList.result[{i}]','raw_file':entry['raw_file'],'provider':'EuropePMC','id':x.get('id'),'pmcid':x.get('pmcid'),'doi':x.get('doi'),'title':x.get('title'),'year':x.get('pubYear'),'abstract_available':bool(x.get('abstractText')),'abstract':x.get('abstractText'),'firstPublicationDate':x.get('firstPublicationDate'),'authors':x.get('authorString'),'journal':x.get('journalInfo',{}).get('journal',{}).get('title'),'isOpenAccess':x.get('isOpenAccess')})
   elif entry['key'].startswith('crossref'):
    msg=data['message'];items=msg.get('items',[]) if entry['key'].startswith('crossref_search') else [msg]
    for i,x in enumerate(items):
     dp=x.get('published',x.get('issued',{})).get('date-parts',[[]])[0]
     candidates.append({'source_query':entry['key'],'record_locator':f'message.items[{i}]' if 'search' in entry['key'] else 'message','raw_file':entry['raw_file'],'provider':'Crossref','id':x.get('DOI'),'doi':x.get('DOI'),'title':' '.join(x.get('title',[])),'year':dp[0] if dp else None,'abstract_available':bool(x.get('abstract')),'abstract':x.get('abstract'),'firstPublicationDate':'-'.join(map(str,dp)),'authors':'; '.join((a.get('given','')+' '+a.get('family','')).strip() for a in x.get('author',[])),'journal':' '.join(x.get('container-title',[])),'isOpenAccess':None})
(RAW/'access_log.json').write_text(json.dumps(log,indent=2,ensure_ascii=False))
(CLEAN/'candidate_records.json').write_text(json.dumps(candidates,indent=2,ensure_ascii=False))
unique={}
for x in candidates:
 k=(x.get('doi') or x['title']).lower();unique.setdefault(k,x)
(CLEAN/'candidates_unique.json').write_text(json.dumps(list(unique.values()),indent=2,ensure_ascii=False))
print(json.dumps({'requests':len(log),'successes':sum(x['status']==200 for x in log),'candidate_occurrences':len(candidates),'unique_candidates':len(unique),'abstracts_available':sum(x['abstract_available'] for x in unique.values())},indent=2))
