from pathlib import Path
import urllib.request,json,concurrent.futures,datetime,hashlib
root=Path(__file__).resolve().parents[1]
urls={
'indomaret_20250626.pdf':'https://www.indomaret.co.id/wp-content/uploads/2025/06/PDF-SH-26-Juni-2025-JawaBaliLombok-Compressed.pdfFF_.pdf',
'century_mandiri_202411.pdf':'https://www.bankmandiri.co.id/documents/20143/175704414/FAQ%2BDaftar%2BProduk%2BCentury%2BAnniversary.pdf/6ca1b5bc-bb75-072e-c8db-9e0fcd250bde?t=1758859152400&version=1.0',
'ski_factsheet.pdf':'https://repository.badankebijakan.kemkes.go.id/5534/1/04%20factsheet%20Gilut_bahasa.pdf',
'bps_variable.html':'https://sirusa.bps.go.id/metadata/variabel/3bf88b6a-eaa5-5ada-82e6-8ab10e95fe5a',
'halodoc_terms.html':'https://www.tanyapepsodent.com/pepsodent-halodoc-terms-conditions.html',
'fifa_terms.html':'https://www.tanyapepsodent.com/promo-fifa-unjukgigi-terms-conditions.html',
'google_trends_explore.json':'https://trends.google.com/trends/api/explore?hl=en-US&tz=-420&req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22pepsodent%22%2C%22geo%22%3A%22ID%22%2C%22time%22%3A%222022-01-01%202026-06-30%22%7D%5D%2C%22category%22%3A0%2C%22property%22%3A%22%22%7D',
}
def get(k,u):
 d={'file':k,'url':u,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (compatible; academic research)'})
  with urllib.request.urlopen(req,timeout=20) as r: b=r.read();d.update(status=r.status,content_type=r.headers.get('Content-Type'),bytes=len(b))
  (root/'raw'/k).write_bytes(b);d['sha256']=hashlib.sha256(b).hexdigest();d['outcome']='downloaded'
 except Exception as e:d.update(outcome='failed',error=str(e))
 return d
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(lambda kv:get(*kv),urls.items()))
(root/'raw'/'http_download_log.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps(results,indent=2))
