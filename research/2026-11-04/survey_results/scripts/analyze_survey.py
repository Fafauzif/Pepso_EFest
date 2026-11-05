import json,re,collections,hashlib,math,sys
from pathlib import Path
import openpyxl,numpy as np,pandas as pd
from scipy.stats import binomtest,fisher_exact
root=Path(__file__).resolve().parent
inp=Path(sys.argv[1]) if len(sys.argv)>1 else root.parent/'upload/Data survei pasta gigi — E-Fest.xlsx'
out=Path(sys.argv[2]) if len(sys.argv)>2 else root/'derived';out.mkdir(parents=True,exist_ok=True)
w=openpyxl.load_workbook(inp,data_only=True);rows=list(w['CLEAN'].values);df=pd.DataFrame(rows[1:],columns=rows[0]);d=df[df.included_main.eq(True)].copy();d['row_key']=['E%02d'%i for i in range(1,len(d)+1)]
SELF='Saya sendiri';FAM='Orang tua atau keluarga';YES='Saya membandingkan beberapa produk sebelum memilih';NO='Saya memilih tanpa membandingkan dengan produk lain'
for x in ['chooser','payer','shopper','living','previous_experience','previous_status','availability','tooth_deliberation','other_deliberation','price_certainty','promo','channel','recall']:
 d[x]=d[x].fillna('MISSING')
counts={k:dict(collections.Counter(d[k])) for k in ['age','activity','living','chooser','payer','shopper','users','channel','price_certainty','promo','previous_experience','previous_status','availability','tooth_deliberation','comparison_gate','other_category','other_deliberation','recall']}
reasons=collections.Counter(x.strip() for v in d.reasons.fillna('') for x in v.split('|') if x.strip());counts['reasons']=dict(reasons)
reasons_list=list(reasons); co=[]
for a in reasons_list:
 for b in reasons_list:
  if a<b:co.append({'a':a,'b':b,'n':sum(a in str(v).split(' | ') and b in str(v).split(' | ') for v in d.reasons)})
co=sorted(co,key=lambda x:-x['n'])
ct={name:pd.crosstab(d[a],d[b]).to_dict() for name,a,b in [('chooser_payer','chooser','payer'),('chooser_shopper','chooser','shopper'),('living_chooser','living','chooser'),('living_payer','living','payer'),('prior_benefit_deliberation','previous_experience','tooth_deliberation'),('prior_benefit_status','previous_experience','previous_status'),('availability_chooser','availability','chooser'),('channel_chooser','channel','chooser'),('living_channel','living','channel')]}
pair=d[d.comparison_eligible.eq(True)]
pairct=pd.crosstab(pair.tooth_compared,pair.other_compared).reindex(index=[False,True],columns=[False,True],fill_value=0)
b=int(pairct.loc[False,True]);c=int(pairct.loc[True,False]); paired={'n':len(pair),'neither':int(pairct.loc[False,False]),'other_only':b,'tooth_only':c,'both':int(pairct.loc[True,True]),'tooth_compared_n':int(pair.tooth_compared.sum()),'other_compared_n':int(pair.other_compared.sum()),'difference_pp':100*(b-c)/len(pair),'exact_mcnemar_p':binomtest(min(b,c),b+c,.5).pvalue}
# A broader sensitivity: valid deliberation responses in both modules, whether chooser field agrees or not.
valid=d[d.tooth_deliberation.isin([YES,NO])&d.other_deliberation.isin([YES,NO])]
paired['valid_deliberation_only_n']=len(valid);paired['valid_deliberation_other_only_n']=int(((valid.tooth_deliberation==NO)&(valid.other_deliberation==YES)).sum());paired['valid_deliberation_tooth_only_n']=int(((valid.tooth_deliberation==YES)&(valid.other_deliberation==NO)).sum())
def brand(v):
 s=str(v or '').lower().strip()
 if s in ['none','-','lupa','tidak tahu']:return 'Unknown'
 if s=='sama':return 'Same as current'
 if any(a in s for a in ['pepsod','pepsident','pepsoden','pepsodeng']):return 'Pepsodent mentioned' if any(a in s for a in [',','/','coolant','coolgate']) else 'Pepsodent'
 if any(a in s for a in ['close','wicked']):return 'Closeup'
 if any(a in s for a in ['colgate','coolgate','collgate']):return 'Colgate'
 if 'sensodyne' in s:return 'Sensodyne mentioned' if '/' in s else 'Sensodyne'
 if 'ciptadent' in s:return 'Ciptadent'
 if 'formula' in s:return 'Formula'
 if 'darlie' in s:return 'Darlie mentioned' if '/' in s else 'Darlie'
 if any(a in s for a in ['usmile','u smile']):return 'USmile'
 if 'marvis' in s:return 'Marvis'
 return 'Unresolved'
d['brand_current']=d.current_product.map(brand);d['brand_previous']=d.previous_product.map(brand)
d.loc[d.brand_previous.eq('Same as current'),'brand_previous']=d.loc[d.brand_previous.eq('Same as current'),'brand_current']
counts['brand_current']=dict(d.brand_current.value_counts());counts['brand_previous']=dict(d.brand_previous.value_counts())
# Conservative case-tier candidate coding, never verified transitions.
def tier(v):
 s=str(v or '').lower()
 if 'peps' not in s:return 'Other or unresolved'
 if any(x in s for x in ['sensitive expert','herbal','siwak','ultra white','whitening']):return 'Named premium candidate'
 if any(x in s for x in ['action 123','123','pencegah gigi berlubang']):return 'Named basic candidate'
 return 'Pepsodent tier unresolved'
d['tier_current']=d.current_product.map(tier);d['tier_previous']=d.previous_product.map(tier)
counts['tier_current_candidates']=dict(d.tier_current.value_counts());counts['tier_previous_candidates']=dict(d.tier_previous.value_counts())
# No-choice code manual rule dictionary, uncertain not forced into no preference.
def preference(v):
 s=str(v or '').lower().strip()
 if s in ['','none','-','.']:return 'Unclear or nonanswer'
 if any(x in s for x in ['tidak ada','tidak punya','khushs']):return 'No specific product preference'
 if any(x in s for x in ['peps','colgate','colgatep','sensodent','close','darlie']):return 'Named product preference'
 return 'Functional requirement' if any(x in s for x in ['selama bisa','dapat membersihkan']) else 'Vague response'
d['preference_code']=d.desired_product.map(preference);counts['preference_code']=dict(d.preference_code.value_counts())
metrics={'submitted':len(df),'eligible':len(d),'excluded':len(df)-len(d),'self_chooser_family_payer':int(((d.chooser==SELF)&(d.payer==FAM)).sum()),'self_shopper_family_payer':int(((d.shopper==SELF)&(d.payer==FAM)).sum()),'solo_living_family_payer':int(((d.living=='Sendiri, termasuk di kos')&(d.payer==FAM)).sum()),'self_chooser_and_shopper':int(((d.chooser==SELF)&(d.shopper==SELF)).sum()),'all_roles_self':int(((d.chooser==SELF)&(d.payer==SELF)&(d.shopper==SELF)).sum()),'habit_price_overlap':sum('Produk itu sudah biasa saya pakai' in str(v) and 'Harganya sesuai uang yang tersedia' in str(v) for v in d.reasons),'habit_benefit_overlap':sum('Produk itu sudah biasa saya pakai' in str(v) and 'Saya membutuhkan manfaat tertentu' in str(v) for v in d.reasons),'price_comfort_overlap':sum('Harganya sesuai uang yang tersedia' in str(v) and 'Rasa atau kenyamanannya cocok' in str(v) for v in d.reasons),'same_resolved_singlebrand':int(((d.brand_current==d.brand_previous)&d.brand_current.isin(['Pepsodent','Colgate','Closeup','Darlie','Sensodyne','USmile','Formula','Ciptadent','Marvis'])).sum())}
price=d[['paid_price','price_certainty','pack']].copy();price['n']=pd.to_numeric(price.paid_price,errors='coerce');metrics['numeric_price_n']=int(price.n.notna().sum());metrics['positive_price_n']=int((price.n>0).sum());metrics['positive_price_median']=float(price.loc[price.n>0,'n'].median());metrics['remembered_positive_price_n']=int(((price.price_certainty=='Saya ingat harganya / punya bukti pembelian')&(price.n>0)).sum())
for key,value in [('metrics',metrics),('counts',counts),('crosstabs',ct),('paired',paired),('reason_overlap',co)]:
 (out/(key+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2,default=lambda x: x.item() if hasattr(x,'item') else str(x)))
# Aggregate workbook quality counts; no identifiers or open text exported.
flags=collections.Counter(x.strip() for v in d.quality_flags.dropna() for x in str(v).split('|'));(out/'quality.json').write_text(json.dumps(dict(flags),indent=2))
(out/'source_fingerprint.json').write_text(json.dumps({'source_name':inp.name,'sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'included':len(d),'sheets':w.sheetnames},indent=2))
def mdtable(t):
 cols=[str(t.index.name or '')]+[str(x) for x in t.columns]
 return '| '+' | '.join(cols)+' |\n| '+' | '.join(['---']*len(cols))+' |\n'+'\n'.join('| '+str(i)+' | '+' | '.join(str(v) for v in row)+' |' for i,row in t.iterrows())
lines=['# Survey calculation output','\n## Main metrics',json.dumps(metrics,indent=2,ensure_ascii=False),'\n## Matched category',json.dumps(paired,indent=2),'\n## Cross tabs']
for name,a,b in [('Roles','chooser','payer'),('Living and payer','living','payer'),('Prior benefit and deliberation','previous_experience','tooth_deliberation'),('Preference and availability','preference_code','availability')]:
 lines.extend(['\n### '+name,mdtable(pd.crosstab(d[a],d[b]))])
lines.extend(['\n## Driver counts',json.dumps(dict(reasons),ensure_ascii=False,indent=2),'\n## Candidate tiers',mdtable(pd.crosstab(d.tier_previous,d.tier_current))])
(out/'results.md').write_text('\n\n'.join(lines))
print((out/'results.md').read_text())
