from pathlib import Path
from collections import Counter
import json,hashlib,datetime,re
import openpyxl,pandas as pd
from scipy.stats import binomtest
base=Path(__file__).parent
src=Path('/workspace/scratch/22ed72ffe415/upload/Data survei pasta gigi — E-Fest (1).xlsx')
w=openpyxl.load_workbook(src,data_only=True)
rows=list(w['CLEAN'].values);d=[dict(zip(rows[0],r)) for r in rows[1:]]
raw=list(w['Form responses 1'].values)[1:]
eligible=[r for r in d if r['included_main'] is True]
# Raw/CLEAN alignment stays private; only mismatch counts are exported.
mapping={1:'consent',2:'age',3:'scope',4:'living',5:'activity',6:'city',7:'current_product',8:'acquired_month',9:'pack',10:'chooser',11:'payer',12:'shopper',13:'users',14:'channel',15:'paid_price',16:'price_certainty',17:'promo',18:'tooth_deliberation',19:'expected_benefit',20:'previous_product',21:'previous_status',22:'previous_experience',23:'desired_product',24:'reason_open',25:'reasons',26:'availability',27:'comparison_gate',28:'other_category',29:'other_product',30:'other_chooser',31:'other_deliberation',32:'other_expected',33:'other_reason',34:'recall',35:'note'}
def norm(v):return '' if v is None else str(v).strip()
mismatches=Counter()
for rr,cc in zip(raw,d):
 for i,k in mapping.items():
  a,b=rr[i],cc[k]
  if k=='acquired_month' and a:
   month,year=map(int,str(a).split('/')); a=datetime.datetime(year,month,1)
  if k=='reasons':
   a=set(x.strip() for x in (a or '').split(',')); b=set(x.strip() for x in (b or '').split('|'))
   if a!=b:mismatches[k]+=1
  elif norm(a)!=norm(b):mismatches[k]+=1
 recomputed=(rr[1]=='Ya, saya bersedia' and rr[2] in ['18–20 tahun','21–24 tahun','25–27 tahun','28–30 tahun'] and rr[3]=='Ya' and bool(rr[34]) and cc['collection_phase']=='MAIN')
 if recomputed!=cc['included_main']:mismatches['inclusion_gate']+=1
SELF='Saya sendiri';FAM='Orang tua atau keluarga'
def n(f):return sum(f(r) for r in eligible)
def pref(v):
 s=str(v or '').strip().lower()
 if s in ['', '-', '.','none']:return 'Unclear or nonanswer'
 if any(x in s for x in ['tidak ada','tidak punya','khushs']):return 'No specific product preference'
 if any(x in s for x in ['peps','colgate','sensodent','close','darlie']):return 'Named product preference'
 return 'Functional requirement' if any(x in s for x in ['selama bisa','dapat membersihkan']) else 'Vague response'
for r in eligible:r['preference_code_manual']=pref(r['desired_product'])
flags=[r for r in eligible if r['quality_flags']]
high=[r for r in eligible if r['recall']=='Cukup yakin dengan sebagian besar jawaban']
unflag=[r for r in eligible if not r['quality_flags']]
def preference_counts(group):
 no=[r for r in group if r['preference_code_manual']=='No specific product preference']
 return dict(n=len(group),no_specific_preference=len(no),no_preference_and_got_wanted=sum(r['availability']=='Saya mendapat produk yang saya inginkan' for r in no))
def paired(group):
 p=[r for r in group if r['comparison_eligible']]
 cells=Counter((r['tooth_compared'],r['other_compared']) for r in p)
 b,c=cells[(False,True)],cells[(True,False)]
 return dict(n=len(p),neither=cells[(False,False)],other_only=b,tooth_only=c,both=cells[(True,True)],exact_mcnemar_p=binomtest(min(b,c),b+c,.5).pvalue if b+c else 1)
known=[r['acquired_month'] for r in eligible if r['acquired_month']]
audit={
 'source':{'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'submitted':len(d),'eligible':len(eligible),'excluded_under18':1,'collection_start_wib':str(min(r['submitted_at_wib'] for r in d)),'collection_end_wib':str(max(r['submitted_at_wib'] for r in d))},
 'reconciliation':{'compared_rows':len(d),'compared_substantive_columns':len(mapping),'raw_clean_mismatches':dict(mismatches),'eligibility_recomputed_from_raw':True,'collection_phase_check':'51 MAIN flags retained from export; source launch timestamp not independently available in workbook','review_adjudications':w['REVIEW'].max_row-1,'summary_count_cells_misformatted_as_dates':sum(cell.data_type=='d' for row in list(w['RINGKASAN'].rows)[:-1] for cell in row)},
 'headlines':{'self_choose':n(lambda r:r['chooser']==SELF),'self_shop':n(lambda r:r['shopper']==SELF),'family_payer':n(lambda r:r['payer']==FAM),'self_choose_and_shop_family_pay':n(lambda r:r['chooser']==SELF and r['shopper']==SELF and r['payer']==FAM),'self_choose_family_pay':n(lambda r:r['chooser']==SELF and r['payer']==FAM),'self_shop_family_pay':n(lambda r:r['shopper']==SELF and r['payer']==FAM),'self_choose_and_shop':n(lambda r:r['chooser']==SELF and r['shopper']==SELF),'all_roles_self':n(lambda r:r['chooser']==SELF and r['shopper']==SELF and r['payer']==SELF),'solo_living':n(lambda r:r['living']=='Sendiri, termasuk di kos'),'solo_living_family_pay':n(lambda r:r['living']=='Sendiri, termasuk di kos' and r['payer']==FAM),'modern_offline':n(lambda r:r['channel'] in ['Minimarket','Supermarket / hypermarket']),'all_known_offline':n(lambda r:r['channel'] in ['Minimarket','Supermarket / hypermarket','Warung atau toko kelontong']),'no_specific_preference':n(lambda r:r['preference_code_manual']=='No specific product preference'),'prior_valued_benefit':n(lambda r:r['previous_experience']=='Ada manfaat yang terasa dan penting bagi saya'),'depleted':n(lambda r:r['previous_status']=='Sudah habis / hampir habis'),'failed_search':n(lambda r:r['availability']=='Saya mencari, tetapi tidak menemukannya'),'family_chooser':n(lambda r:r['chooser']==FAM),'family_chooser_family_shopper':n(lambda r:r['chooser']==FAM and r['shopper']==FAM),'specific_benefit_reason':n(lambda r:'Saya membutuhkan manfaat tertentu' in (r['reasons'] or '')),'specific_benefit_without_comparing':n(lambda r:'Saya membutuhkan manfaat tertentu' in (r['reasons'] or '') and r['tooth_deliberation']=='Saya memilih tanpa membandingkan dengan produk lain')},
 'dates':{'known_acquisition_month':len(known),'missing_acquisition_month':len(eligible)-len(known),'post_h1_2026':sum(v>datetime.datetime(2026,6,30) for v in known),'august2025':sum(v==datetime.datetime(2025,8,1) for v in known),'first_of_month_is_representation_only':True},
 'quality':{'flagged_records':len(flags),'high_recall_records':len(high),'price_zero':n(lambda r:r['paid_price']==0),'price_190':n(lambda r:r['paid_price']==190),'price_remembered_or_proof':n(lambda r:r['price_certainty']=='Saya ingat harganya / punya bukti pembelian'),'verified_premium_to_basic_histories':0,'history_scope':'No manually adjudicated or independently verified histories; zero here does not mean nobody switched','self_reported_validated_history_available':False},
 'sensitivity':{'unflagged':preference_counts(unflag),'high_recall':preference_counts(high),'paired_unflagged':paired(unflag),'paired_high_recall':paired(high)},
 'persona_design_basis':[
 {'name':'Pengguna mandiri dengan dana keluarga','observed_intersection':24,'denominator':50,'basis':'chooser=SELF AND shopper=SELF AND payer=FAMILY','job':'Mempertahankan pilihan pribadi dengan biaya total dan biaya ulang yang jelas','response':'Alur belanja sendiri; kartu varian dan harga; berbagi hanya bila perlu','not_proven':'Veto orang tua, pendapatan, kesediaan membayar Premium'},
 {'name':'Pengguna yang sudah menemukan kecocokan','observed_intersection':20,'denominator':50,'basis':'previous_experience=valued important benefit','job':'Mempertahankan manfaat yang sudah dihargai saat produk habis','response':'Lewati trial yang tidak perlu; simpan SKU dan waktu penggantian sukarela','not_proven':'20 bekas pengguna Premium atau efek pengingat'},
 {'name':'Pengguna dengan pilihan keluarga','observed_intersection':19,'denominator':50,'basis':'chooser=FAMILY;16 dari19 juga family_shopper','job':'Menyelaraskan produk yang dipakai bersama dengan pemilih/pembeli sebenarnya','response':'Kartu pilihan opsional untuk pembeli; tidak wajib konversi seluruh keluarga','not_proven':'Keluarga menolak Premium; kebutuhan satu tabung perorang'}
 ],
 'stp':{'segmentation':'Kebutuhan manfaat yang berlanjut; riwayat SKU; peran pemilih-pembeli-pembiaya; kanal; keadaan stok. Dimensi bisa beririsan.','primary_target':'Usia18–30 dengan riwayat Pepsodent Premium lalu Basic yang dikonfirmasi secukupnya dan kebutuhan tambahan yang masih relevan.','initial_recruitment':'Mahasiswa sebagai kelompok awal yang dapat diakses; bukan proksi seluruh target18–30. Sertakan25–30 dan nonmahasiswa sebelum generalisasi.','secondary_target':'Pengguna baru berkebutuhan relevan dilaporkan sebagai kohort eksploratif terpisah.','exclusion':'Kebutuhan dasar sudah terpenuhi; tidak ada kebutuhan relevan; pengguna tidak ingin dihubungi; keluhan yang memerlukan layanan profesional.','positioning':'Pilihan Premium yang sesuai kebutuhan, jelas biaya ulangnya, mudah dibeli melalui kanal biasa, dan dipertahankan hanya bila bernilai.','market_size_claim':'Tidak ada estimasi ukuran pasar, pangsa segmen, CAC, qualification40%, conversion, retention, atau WTP dari survei ini.'}
}
old=json.loads(Path('Pepso_EFest/research/2026-11-04/survey_results/data/aggregates/counts.json').read_text())
new=json.loads((base/'counts.json').read_text())
changes=[]
for key in ['age','chooser','payer','shopper','channel','preference_code','previous_experience','previous_status','reasons']:
 for label,val in new[key].items():
  ov=old.get(key,{}).get(label,0)
  if val!=ov:changes.append(dict(field=key,label=label,old=ov,new=val))
audit['changed_counts_vs_prior49']=changes
(base/'audit_and_targeting.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
print(json.dumps({k:audit[k] for k in ['reconciliation','headlines','dates','quality','sensitivity','changed_counts_vs_prior49']},ensure_ascii=False,indent=2))
