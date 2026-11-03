import subprocess,json,datetime
from pathlib import Path
b=Path(__file__).resolve().parents[1];py='/workspace/scratch/70458c8119f6/tooltests_venv/bin/python'
commands=[('snscrape_cli',['/workspace/scratch/70458c8119f6/tooltests_venv/bin/snscrape','--max-results','3','twitter-search','pepsodent']),('ntscraper_public',[py,'-c',"import json;from ntscraper import Nitter;s=Nitter(instances=['https://nitter.net'],skip_instance_check=True,log_level=0);print(json.dumps(s.get_tweets('pepsodent',mode='term',number=3,instance='https://nitter.net')))"])]
out=[]
for name,args in commands:
 stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  p=subprocess.run(args,capture_output=True,text=True,timeout=28);r={'test':name,'command':args,'status':'completed','exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'retrieved_at':stamp}
 except subprocess.TimeoutExpired as e:r={'test':name,'command':args,'status':'timeout_28seconds','stdout':(e.stdout or b'').decode() if isinstance(e.stdout,bytes) else e.stdout,'stderr':(e.stderr or b'').decode() if isinstance(e.stderr,bytes) else e.stderr,'retrieved_at':stamp}
 out.append(r);print(json.dumps(r,indent=2))
(b/'raw/client_runtime_tests.json').write_text(json.dumps(out,indent=2))
p=subprocess.run([py,'-m','pip','freeze'],capture_output=True,text=True,timeout=15);(b/'raw/test_environment_freeze.txt').write_text(p.stdout)
