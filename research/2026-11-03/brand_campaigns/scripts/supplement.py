from pathlib import Path
import json
ns={'__file__':str(Path(__file__).with_name('collect.py'))};exec(Path(__file__).with_name('collect.py').read_text().split('with concurrent.futures.ThreadPoolExecutor')[0],ns)
urls=['https://oresa.id/produk-sampel/206/1053/pepsodent-ultra-white','https://linktr.ee/TanyaPepsodent','https://www.tanyapepsodent.com/shadescanai.html','https://www.tanyapepsodent.com/misi-kami.html','https://www.close-up.com/id/p/closeup-white-now-purple-stain-corrector.html/08999999609467','https://www.sensodyne.co.id/about-sensodyne.html']
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(ns['fetch'],urls))
(ns['ROOT']/'source_register_supplement.json').write_text(json.dumps(rows,indent=2)); print([(r['url'],r['status']) for r in rows])
