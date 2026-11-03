import urllib.request,urllib.parse,json,datetime,concurrent.futures,hashlib
from pathlib import Path
b=Path(__file__).resolve().parents[1];raw=b/'raw';raw.mkdir(parents=True,exist_ok=True)
jobs=[]
for p in ['praw','asyncpraw','twscrape','ntscraper','snscrape','crawl4ai','scrapling']:jobs.append(('pypi_'+p,'https://pypi.org/pypi/'+p+'/json','.json'))
urls={
 'twscrape_readme':'https://raw.githubusercontent.com/vladkens/twscrape/main/README.md',
 'twscrape_pyproject':'https://raw.githubusercontent.com/vladkens/twscrape/main/pyproject.toml',
 'ntscraper_readme':'https://raw.githubusercontent.com/bocchilorenzo/ntscraper/main/README.md',
 'ntscraper_requirements':'https://raw.githubusercontent.com/bocchilorenzo/ntscraper/main/requirements.txt',
 'snscrape_readme':'https://raw.githubusercontent.com/JustAnotherArchivist/snscrape/master/README.md',
 'snscrape_twitter':'https://raw.githubusercontent.com/JustAnotherArchivist/snscrape/master/snscrape/modules/twitter.py',
 'scrapling_pyproject':'https://raw.githubusercontent.com/D4Vinci/Scrapling/main/pyproject.toml',
 'crawl4ai_pyproject':'https://raw.githubusercontent.com/unclecode/crawl4ai/main/pyproject.toml',
 'praw_docs':'https://praw.readthedocs.io/en/stable/getting_started/authentication.html',
 'asyncpraw_docs':'https://asyncpraw.readthedocs.io/en/stable/getting_started/authentication.html'}
for n,u in urls.items():jobs.append((n,u,'.txt' if 'raw.github' in u else '.html'))
def get(t):
 n,u,e=t;stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'PepsodentResearch/1.0 public capability assessment'}),timeout=20) as r:d=r.read();status=r.status;ct=r.headers.get('Content-Type','')
  p=raw/(n+e);p.write_bytes(d)
  return {'name':n,'url':u,'status':status,'content_type':ct,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'raw_file':str(p.relative_to(b)),'retrieved_at':stamp}
 except Exception as x:return {'name':n,'url':u,'status':'failed','error':str(x),'retrieved_at':stamp}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:out=list(p.map(get,jobs))
(raw/'tool_inspection_log.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
