from pathlib import Path
import urllib.request, json, concurrent.futures, hashlib, datetime, re, html
ROOT=Path(__file__).resolve().parents[1]; (ROOT/'raw/http').mkdir(parents=True,exist_ok=True)
urls=[
'https://www.tanyapepsodent.com/home.html',
'https://www.tanyapepsodent.com/pepsodent-expert.html',
'https://www.tanyapepsodent.com/sensitive-expert.html',
'https://www.tanyapepsodent.com/rangkaian-produk/ultra-white.html',
'https://www.tanyapepsodent.com/pepsodent-halodoc-terms-conditions.html',
'https://www.tanyapepsodent.com/misi-kami/baik-untuk-masyarakat/pepsodent-halodoc/faq.html',
'https://www.tanyapepsodent.com/sitemap.xml',
'https://enzim.com/', 'https://enzim.com/faq/', 'https://enzim.com/products-dr-enzim/',
'https://www.sensodyne.co.id/Portfolio.html',
'https://www.sensodyne.co.id/Portfolio/pasta-gigi/Repair-Protect.html',
'https://www.jakartafashionweek.co.id/events/be-the-brightest-of-them-all/',
'https://www.jakartafashionweek.co.id/jfw-2026/the-brightest-of-them-all-demi-couture-dalam-balutan-senyuman/',
'https://www.unilever.co.id/news/press-releases/2024/ai-dentascan-lengkapi-layanan-konsultasi-gigi-online-tanya-dokter-gigi-by-pepsodent/'
]
def fetch(u):
 k=hashlib.sha256(u.encode()).hexdigest()[:12]; stamp=datetime.datetime.now(datetime.timezone.utc).isoformat(); row=dict(url=u,collected_at_utc=stamp,id='BC-'+k)
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (research source collection)'})
  with urllib.request.urlopen(req,timeout=15) as f: b=f.read(8_000_000); row.update(status=f.status,content_type=f.headers.get('Content-Type'),final_url=f.url)
  p=ROOT/'raw/http'/f'{k}.html'; p.write_bytes(b); row.update(raw_file=str(p.relative_to(ROOT)),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
  text=b.decode('utf-8','replace'); text=re.sub(r'<(script|style)\b[^>]*>.*?</\1>',' ',text,flags=re.S|re.I); text=re.sub('<[^>]+>',' ',text); text=html.unescape(re.sub(r'\s+',' ',text)); (ROOT/'raw/http'/f'{k}.txt').write_text(text)
 except Exception as e: row.update(status='failed',error=str(e))
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: records=list(ex.map(fetch,urls))
(ROOT/'source_register_http.json').write_text(json.dumps(records,indent=2))
print(json.dumps(records,indent=2))
