from pathlib import Path
import urllib.request,json,hashlib,datetime,concurrent.futures
B=Path(__file__).resolve().parents[1]
urls=[('oresa_index','https://oresa.id/produk-sampel/perawatan-pribadi'),('oresa_siwak','https://www.oresa.id/produk-sampel/147/998/pepsodent-siwak-habbatussauda'),('mendeley_large','https://data.mendeley.com/datasets/74xrbd4vxy/1'),('mendeley_prdect','https://data.mendeley.com/datasets/574v66hf2v/1'),('mendeley_large_api','https://data.mendeley.com/public-api/datasets/74xrbd4vxy/versions/1'),('mendeley_prdect_api','https://data.mendeley.com/public-api/datasets/574v66hf2v/versions/1')]
def get(x):
 name,u=x;now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20) as r:b=r.read(15_000_000);ctype=r.headers.get('Content-Type');status=r.status
  p=B/'raw'/f'{name}.txt';p.write_bytes(b)
  return {'source_id':name,'url':u,'status':status,'content_type':ctype,'retrieved_at_utc':now,'raw_file':str(p.relative_to(B)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 except Exception as e:return {'source_id':name,'url':u,'status':'failed','error':str(e),'retrieved_at_utc':now}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(get,urls))
(B/'source_register_probes.json').write_text(json.dumps(rows,indent=2));print(rows)
