from pathlib import Path
import json
ns={'__file__':str(Path(__file__).with_name('collect.py'))};exec(Path(__file__).with_name('collect.py').read_text().split('with concurrent.futures.ThreadPoolExecutor')[0],ns)
base='https://www.tanyapepsodent.com/p/'
urls=[base+x for x in ['pasta-gigi-pepsodent-gum-expert-whitening.html/08999999598808','sensitif-sensitive-mineral-expert-fresh.html/08999999035563','sensitif-sensitive-mineral-expert-original.html/08999999008505','sensitif-sensitive-mineral-expert-whitening.html/08999999032890','ultra-white-gentle-radiance.html/08999999616335','complete-8-multi-protection.html/08999999564421']]
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(ns['fetch'],urls))
(ns['ROOT']/'source_register_canonical_retry.json').write_text(json.dumps(rows,indent=2));print([(r['url'],r['status']) for r in rows])
