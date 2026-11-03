#!/usr/bin/env python3
"""Extract captured public reader lines, preserving source-line bounds. Not an API census."""
import csv,datetime,hashlib,json,re
from pathlib import Path
B=Path(__file__).resolve().parents[1]
lines={}
for fn in ['search_open_01.json','reddit_1414a8a_remaining.json']:
 obj=json.loads((B/'raw'/fn).read_text())
 for c in obj['content']:
  for m in re.finditer(r'^L(\d+): ?(.*)$',c.get('text',''),re.M):lines[int(m[1])]=m[2]
(B/'raw'/'reddit_1414a8a_lines.json').write_text(json.dumps(lines,ensure_ascii=False,indent=2))
headers=[]
for n,t in sorted(lines.items()):
 if n>711:continue
 if re.fullmatch(r'【\d+†3 thn lalu】',t):
  author=None;start=n
  for j in range(n-1,max(-1,n-9),-1):
   u=lines.get(j,'');m=re.fullmatch(r'【\d+†([^】]+)】',u)
   if m and not m[1].startswith(('Image','http')):author=m[1];start=j;break
   if u=='[dihapus]':author='deleted';start=j;break
  if author:headers.append((start,n,author))
rows=[]
for i,(start,n,a) in enumerate(headers):
 end=headers[i+1][0]-1 if i+1<len(headers) else 711
 texts=[];ss=None;ee=None
 for j in range(n+1,end+1):
  t=lines.get(j,'')
  if not t.strip() or t.startswith(('• Diedit','【16†Image:')):continue
  if ss is None:ss=j
  ee=j;texts.append(t)
 text='\n'.join(texts).strip()
 if not text or 'Komentar dihapus oleh moderator' in text:continue
 rows.append({'record_id':'REDDIT-1414a8a-L'+str(ss),'source_id':'REDDIT-1414a8a','platform':'Reddit','source_url':'https://www.reddit.com/r/indonesia/comments/1414a8a','thread_title':'[Very random question] Tell me about your go-to toothpaste(s)','thread_date':'2023-06-05','published_raw':'3 thn lalu','published_at_utc':None,'author_hash':hashlib.sha256(a.encode()).hexdigest()[:12],'review_text':text,'source_line_start':ss,'source_line_end':ee,'raw_file':'raw/reddit_1414a8a_lines.json','age_verified':False,'premium_to_basic_verified':False,'selection_caveat':'one purposively found public thread; displayed selected comments; no probability sample; clinical claims unverified'})
(B/'clean'/'reddit_comments.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (B/'clean'/'reddit_comments.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('comments extracted',len(rows))
