import urllib.request,urllib.parse,json,datetime,concurrent.futures
from pathlib import Path
b=Path(__file__).resolve().parents[1]
jobs=[('episodic_full','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5962890/fullTextXML','.xml'),('scoping_full','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8908863/fullTextXML','.xml'),('jakarta_herbal','https://journal.ipb.ac.id/jabm/article/download/41315/24286','.pdf')]
for k,doi in [('sensory2014','10.1111/joss.12120'),('freshness2004','10.1111/j.1745-459X.2004.tb00143.x'),('jakarta2022','10.17358/jabm.8.3.758')]:jobs.append((k,'https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='/'),'.json'))
def get(t):
 n,u,ext=t
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'PepsodentResearch/1.0'}),timeout=25) as r:d=r.read();ct=r.headers.get('Content-Type')
  (b/'raw'/(n+ext)).write_bytes(d);return {'name':n,'url':u,'status':200,'content_type':ct,'bytes':len(d),'raw_file':'raw/'+n+ext,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as e:return {'name':n,'url':u,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:out=list(p.map(get,jobs))
(b/'raw/targeted_access_log.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
