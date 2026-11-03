import unittest,tempfile,pathlib,json,sys,urllib.error,gzip
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
import corpus_store as c
from fetch_targets import FetchQueue
class StoreTests(unittest.TestCase):
 def test_identity_provenance_conflicts_checkpoint(self):
  with tempfile.TemporaryDirectory() as td:
   p=pathlib.Path(td);f=p/'oresa.jsonl';rows=[{'record_id':'ORESA-1','review_text':'Feels fresh','source_url':'https://oresa.id/x','incentive_status':'cashback'},{'record_id':'ORESA-2','review_text':'Feels fresh','source_url':'https://oresa.id/x','incentive_status':'cashback'},{'record_id':'ORESA-1','review_text':'Updated experience','source_url':'https://oresa.id/x'},{'record_id':'bad','text':'[removed]'}];f.write_text('\n'.join(json.dumps(r)for r in rows))
   dbp=p/'test.sqlite';db=c.dbopen(dbp)
   self.assertEqual(c.ingest(db,[f],2,1)[0]['status'],'checkpointed_at_cap')
   self.assertEqual(c.ingest(db,[f],10,1)[0]['new_observations'],1)
   self.assertEqual(c.ingest(db,[f],10,1)[0]['status'],'already_complete')
   s=c.stats(db,dbp);self.assertEqual(s['unique_platform_records'],2);self.assertEqual(s['source_observations'],3);self.assertEqual(s['observations_with_payload_difference'],1);self.assertEqual(s['possible_copied_text_groups'],1);self.assertEqual(s['ingestion_errors'],0);self.assertEqual(s['excluded_removed_text_rows'],1)
   self.assertEqual(c.export(db,p/'out'),2);self.assertEqual(len(gzip.open(p/'out/records.jsonl.gz','rt').read().splitlines()),2);db.close()
 def test_gzip_and_crosscategory_collector_identity(self):
  with tempfile.TemporaryDirectory() as td:
   p=pathlib.Path(td)/'reviews.jsonl.gz';r={'record_id':'AMZ-HPC-'+'a'*24,'review_text':'A review','platform':'Amazon historical research dataset','scope':'non_Indonesia_historical_context'}
   with gzip.open(p,'wt') as f:f.write(json.dumps(r)+'\n')
   rows=list(c.iter_rows(p));self.assertEqual(len(rows),1)
   one=c.normalize(rows[0][1],str(p));r['record_id']='AMZ-HH-'+'a'*24;two=c.normalize(r,str(p))
   self.assertEqual(one['record_key'],two['record_key']);self.assertEqual(one['scope'],'non_Indonesia_historical_context');self.assertIn('candidate',one['relevance_status'])
 def test_dates_and_no_age_inference(self):
  r=c.normalize({'record_id':'TAR-ID-1','review_text':'Good','published_raw':'2 months ago','self_reported_age':23},'tryandreview_reviews.json')
  self.assertEqual(r['platform'],'tryandreview');self.assertEqual(r['scope'],'unknown_date');self.assertIsNone(r['content_date'])
  r=c.normalize({'id':'x','text':'Fine','created_at':'2026-06-30T23:00:00Z','platform':'reddit'},'a.jsonl');self.assertEqual(r['scope'],'case_historical')
 def test_429_stops_host_and_credentials_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   q=FetchQueue(td,['example.org'],max_requests=4,interval=0,retries=0)
   with patch.object(q.opener,'open',side_effect=urllib.error.HTTPError('https://example.org/a',429,'rate',{},None)) as m:
    self.assertEqual(q.fetch({'url':'https://example.org/a'})['status'],'host_stopped_access_or_rate_limit')
    self.assertEqual(q.fetch({'url':'https://example.org/b'})['status'],'host_stopped');self.assertEqual(m.call_count,1)
   self.assertEqual(q.fetch({'url':'https://example.org/a?token=secret'})['status'],'rejected_url')
if __name__=='__main__':unittest.main()
