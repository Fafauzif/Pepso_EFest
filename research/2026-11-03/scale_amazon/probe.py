import urllib.request,json,time
from pathlib import Path
base='https://huggingface.co/api/datasets/McAuley-Lab/Amazon-Reviews-2023/tree/main/'
out=Path(__file__).parent
for path in ['raw','raw/meta_categories','raw/review_categories']:
 try:
  with urllib.request.urlopen(base+path+'?recursive=false&limit=100',timeout=15) as r:d=json.load(r)
  (out/(path.replace('/','_')+'_index.json')).write_text(json.dumps(d,indent=2))
  print(path,[(x['path'],x['size']) for x in d if any(t in x['path'] for t in ['Health','Beauty'])],flush=True)
 except Exception as e: print(path,str(e),flush=True)
