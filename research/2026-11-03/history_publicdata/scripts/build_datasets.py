"""Build tables from manually verified source observations. No imputation or crawling."""
from pathlib import Path
import csv,json,hashlib
root=Path(__file__).resolve().parents[1]
D='2026-11-03'
sources=[
 {'source_id':'HP01','url':'https://www.indomaret.co.id/wp-content/uploads/2025/06/PDF-SH-26-Juni-2025-JawaBaliLombok-Compressed.pdfFF_.pdf','title':'Indomaret Super Hemat 26 June–9 July 2025','file':'raw/indomaret_20250626.pdf','access':'downloaded; PDF page18 visually verified','scope':'Java/Bali/Lombok flyer; not branch stock'},
 {'source_id':'HP02','url':'https://www.indomaret.co.id/wp-content/uploads/2025/07/PDF-SH-24-Juli-2025-JawaBaliLombok-Com.pdf','title':'Indomaret Super Hemat 24 July–6 August 2025','file':'raw/indomaret_20250724.pdf','access':'downloaded; PDF pages15–16 visually verified','scope':'Java/Bali/Lombok; excludes Indomaret Point'},
 {'source_id':'HP03','url':'https://www.bankmandiri.co.id/documents/20143/175704414/FAQ%2BDaftar%2BProduk%2BCentury%2BAnniversary.pdf/6ca1b5bc-bb75-072e-c8db-9e0fcd250bde?t=1758859152400&version=1.0','title':'Century Anniversary QRIS Livin Mandiri promo product list','file':'raw/century_mandiri_202411.pdf','access':'downloaded; PDF page9 rows355,358,359 visually verified','scope':'6–30 November2024; campaign payment context'},
 {'source_id':'HP04','url':'https://blog.klikindomaret.com/wp-content/uploads/2024/09/PDF-SH-5-September-2024-Dengan-Link.pdf','title':'Indomaret Super Hemat5–18 September2024','file':'raw/open05.json','access':'web PDF open+screenshots; direct HTTP403; PDFpage14 visually verified','scope':'flyer; no branch stock'},
 {'source_id':'HP05','url':'https://www.tanyapepsodent.com/pepsodent-halodoc-terms-conditions.html','title':'Pepsodent×Halodoc terms','file':'raw/halodoc_terms.txt','access':'downloaded; web lines138–158','scope':'August2024–July2025; special-marked packs'},
 {'source_id':'HP06','url':'https://www.tanyapepsodent.com/promo-fifa-unjukgigi-terms-conditions.html','title':'Pepsodent FIFA Unjuk Gigi terms','file':'raw/fifa_terms.txt','access':'downloaded; web lines138–159','scope':'16May–30June2024; campaign title refers FIFA2026'},
 {'source_id':'HP07','url':'https://repository.badankebijakan.kemkes.go.id/5534/1/04%20factsheet%20Gilut_bahasa.pdf','title':'Kesehatan Gigi dan Mulut di Indonesia—SKI2023 factsheet','file':'raw/ski_factsheet.pdf','access':'downloaded; PDFpage2 visually verified','scope':'national≥3years;2018/2023; reported interview behavior'},
 {'source_id':'HP08','url':'https://sirusa.bps.go.id/metadata/variabel/3bf88b6a-eaa5-5ada-82e6-8ab10e95fe5a','title':'BPS Pengeluaran Aneka Barang dan Jasa variable metadata','file':'raw/bps_variable.txt','access':'direct HTTP200; web page403; saved HTML/text','scope':'related activity Susenas2025; variableR268; value code269 groups personal care'},
 {'source_id':'HP09','url':'https://www.unilever.co.id/news/press-releases/2026/kinerja-semester-i-2026-unvr-penjualan-bersih-rp169-triliun-fundamental-semakin-kuat-dan-pertumbuhan-berkelanjutan/','title':'Unilever Indonesia H1 2026 performance release','file':'raw/search02.json','access':'official search full-text retrieval; release date28July2026 verified investor page','scope':'continuing company operations excluding SariWangi, not brand-tier'},
 {'source_id':'HP10','url':'https://www.unilever.co.id/investor/lihat-hasil-dan-presentasi-perusahaan/ikhtisar-perusahaan-fy-2025/','title':'Unilever Indonesia FY2025 overview','file':'raw/search01.json','access':'official search retrieval','scope':'company continuing operations, not Pepsodent Premium'},
]
lookup={s['source_id']:s for s in sources}
rows=[]
def offer(id,src,start,end,retailer,product,grams,normal,promo,locator,conditions='',notes=''):
 s=lookup[src];rows.append(dict(event_id=id,source_id=src,event_type='displayed_price_promotion',start_date=start,end_date=end,retailer=retailer,product_raw=product,grams_nominal=grams,reference_price_idr=normal,offer_price_idr=promo,discount_percent_calculated=(round((normal-promo)/normal*100,4) if normal and promo else None),cashback_or_service_voucher_idr=None,source_url=s['url'],retrieved_date=D,source_locator=locator,conditions=conditions,notes=notes,interpretation='advertised offer; not transaction, sales, or in-stock observation'))
offer('HP-E01','HP04','2024-09-05','2024-09-18','Indomaret','Pepsodent Sensitive Expert100g all variants',100,None,23900,'PDFpage14(zero13),top-left','See flyer terms; no branch selected','Reference price not confidently readable; left null')
offer('HP-E02','HP03','2024-11-06','2024-11-30','Century','PEPSODENT SNSTV EX WHTNING100',100,38500,31000,'PDFpage9,row355','Document headed QRIS Livin by Mandiri; check payment qualification','Displayed price; not historical paid price')
offer('HP-E03','HP03','2024-11-06','2024-11-30','Century','PEPSODENT SENSITIVE EXPERT100',100,37800,31000,'PDFpage9,row358','Document headed QRIS Livin by Mandiri; check payment qualification','Variant name unspecified in original row')
offer('HP-E04','HP03','2024-11-06','2024-11-30','Century','PEPSODENT SSTV EXPRT FRESH100G',100,37600,31000,'PDFpage9,row359','Document headed QRIS Livin by Mandiri; check payment qualification')
offer('HP-E05','HP01','2025-06-26','2025-07-09','Indomaret','Pepsodent Sensitive Expert Original/Whitening100g',100,39900,19900,'PDFpage18(zero17),printed16,top-left','Java/Bali/Lombok flyer; plus500poinku','Grouped variants are one offer, not two independent observations')
offer('HP-E06','HP01','2025-06-26','2025-07-09','Indomaret','Pepsodent Action123 Complete190g',190,28500,21500,'PDFpage18(zero17),printed16,second top','Java/Bali/Lombok flyer; plus500poinku')
offer('HP-E07','HP02','2025-07-24','2025-08-06','Indomaret','Pepsodent Sensitive Expert Whitening/Original100g',100,39900,19900,'PDFpage15(zero14),third top','Java/Bali/Lombok;not IndomaretPoint;plus500poinku','Grouped variants one offer')
offer('HP-E08','HP02','2025-07-24','2025-08-06','Indomaret','Pepsodent Strong190g',190,14900,10500,'PDFpage15(zero14),fourth top','Java/Bali/Lombok;not IndomaretPoint;plus500poinku','Pack image advertises bonus; do not use nominal grams for consumption model without checking exact total')
offer('HP-E09','HP02','2025-07-24','2025-08-06','Indomaret','Pepsodent Action123 Complete190g',190,28500,21500,'PDFpage16(zero15),top-left','Java/Bali/Lombok;plus500poinku')
offer('HP-E10','HP02','2025-07-24','2025-08-06','Indomaret','Pepsodent White120+30g',150,12700,10900,'PDFpage16(zero15),second top','Java/Bali/Lombok;plus500poinku','Explicit total150g includes bonus')
for id,src,start,end,amount,kind,prod,conditions,loc in [
 ('HP-E11','HP05','2024-08','2025-07',25000,'dental_consultation_voucher','Special-marked Complete8,Action123Complete,Kids,SensitiveExpert,GumExpert','Up to25000 consultation discount;2000 service fee outside voucher;limited quotas;not stackable','web lines138–158;terms clauses1–9'),
 ('HP-E12','HP06','2024-05-16','2024-06-30',5000,'conditional_gopay_cashback','Pepsodent toothpaste190g/2x190g/225g/2x225g or toothbrush purchase≥10000','Valid receipt;limited first500000 e-vouchers;max5 per participant;not an unconditional shelf discount','web lines138–159;period+reward sections')]:
 s=lookup[src];rows.append(dict(event_id=id,source_id=src,event_type=kind,start_date=start,end_date=end,retailer='multiple/brand program',product_raw=prod,grams_nominal=None,reference_price_idr=None,offer_price_idr=None,discount_percent_calculated=None,cashback_or_service_voucher_idr=amount,source_url=s['url'],retrieved_date=D,source_locator=loc,conditions=conditions,notes='Month-only program bounds preserved where no day supplied',interpretation='program terms; participation and outcomes unknown'))

def write(name,data):
 (root/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 with (root/(name+'.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
write('promotion_events',rows)
ind=[]
for year,source,measure,value,denom,loc in [
 (2018,'Riskesdas2018','dental_oral_problem_reported',57.6,'population age≥3;as displayed in SKI comparison','PDFpage2,figure3'),
 (2023,'SKI2023','dental_oral_problem_reported',56.9,'population age≥3','PDFpage2,figure3'),
 (2018,'Riskesdas2018','received_dental_healthcare',10.2,'factsheet comparison;consult original survey for precise eligible base','PDFpage2,figure3'),
 (2023,'SKI2023','received_dental_healthcare',11.2,'narrative:among those reporting dental/oral problems;verify detailed table before recombining','PDFpage2,figure3'),
 (2018,'Riskesdas2018','daily_brushing_reported',94.7,'population age≥3;interview','PDFpage2,figure5'),
 (2023,'SKI2023','daily_brushing_reported',95.6,'population age≥3;interview','PDFpage2,figure5'),
 (2018,'Riskesdas2018','correct_brushing_timing_reported',2.8,'population age≥3;reported timing,not observed technique','PDFpage2,figure5'),
 (2023,'SKI2023','correct_brushing_timing_reported',6.2,'population age≥3;reported timing,not observed technique','PDFpage2,figure5')]:
 ind.append(dict(indicator_id='HP-I'+str(len(ind)+1).zfill(2),source_id='HP07',year=year,survey=source,measure=measure,value=value,unit='percent',geography='Indonesia',population_or_denominator=denom,source_url=lookup['HP07']['url'],source_locator=loc,retrieved_date=D,caveat='Not18–30specific,brand-specific,switching,or causal evidence;figures reproduced from comparative factsheet'))
write('public_health_indicators',ind)
(root/'source_register.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2))
meta=[dict(source_id='HP08',variable_id='309465',alias='R268',activity='Susenas dan Modul Konsumsi Pengeluaran',activity_year=2025,reference_period='last month and last year',group_code='269',group_label='Sabun mandi, pasta gigi, sikat gigi, dan sampo',unit='rupiah',supports='household grouped expenditure context',does_not_identify='toothpaste-only spend, brand/tier, buyer/payer, age18–30switching',source_url=lookup['HP08']['url'],source_locator='raw/bps_variable.txt lines40–73 and162–166')]
write('public_data_metadata',meta)
summary={'promotion_event_count':len(rows),'price_offer_rows':sum(r['event_type']=='displayed_price_promotion' for r in rows),'health_indicator_rows':len(ind),'metadata_rows':len(meta),'sources':len(sources),'google_trends_series_obtained':False,'google_trends_failure':'HTTP429 on first direct explore request; no retries','paid_spend_usd':0}
(root/'collection_summary.json').write_text(json.dumps(summary,indent=2));print(summary)
