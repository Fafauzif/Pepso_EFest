from pathlib import Path
from html.parser import HTMLParser
import json, urllib.parse
ns={'__file__':str(Path(__file__).with_name('collect.py'))}; exec(Path(__file__).with_name('collect.py').read_text().split('with concurrent.futures.ThreadPoolExecutor')[0],ns)
ROOT=ns['ROOT']; links=set()
class P(HTMLParser):
 def __init__(self,base): super().__init__(); self.base=base
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='a' and d.get('href'):
   u=urllib.parse.urljoin(self.base,d['href'])
   if any(x in u for x in ['/p/','/Portfolio/pasta-gigi','/ultra-white/discover']):links.add(u)
rows=json.loads((ROOT/'source_register_http.json').read_text())
for r in rows:
 if r.get('status')==200 and any(x in r['url'] for x in ['tanyapepsodent','sensodyne']):P(r['url']).feed((ROOT/r['raw_file']).read_text())
links.update([
'https://www.tanyapepsodent.com/ultra-white.html',
'https://www.close-up.com/id/semua-produk.html',
'https://www.close-up.com/id/p/closeup-kaolin-mineral-whitener-stain-eraser.html/08999999609474',
'https://www.unilever.com/brands/personal-care/pepsodent/',
'https://www.unilever.co.id/news/press-releases/2024/kinerja-unvr-q1-2024-unilever-indonesia-catatkan-laba-bersih-14-triliun-ekspansi-margin-kotor-dan-peningkatan-volume/',
'https://www.unilever.co.id/news/press-releases/2023/perawatan-gigi-gratis-di-seluruh-indonesia-kembali-hadir-di-bulan-kesehatan-gigi-nasional-2023/',
'https://enzim.com/products-bck/'
])
links-=set(x['url'] for x in rows)
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as ex: records=list(ex.map(ns['fetch'],sorted(links)))
(ROOT/'source_register_http_expanded.json').write_text(json.dumps(records,indent=2))
print('Requests',len(records),'success',sum(r.get('status')==200 for r in records))
for r in records: print(r['url'],r['status'])
