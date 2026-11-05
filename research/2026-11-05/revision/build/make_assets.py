from pathlib import Path
import json, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
import numpy as np
R=Path(__file__).resolve().parents[1]; A=R/'assets'; A.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':240})
navy='#234B63';red='#B52B40';grey='#B8C0C6';pale='#EDF2F4'
def save(fig,name):
 fig.savefig(A/name,bbox_inches='tight',facecolor='white');plt.close(fig)
f,a=plt.subplots(figsize=(7.2,2.55));names=['Harga sesuai uang','Kebiasaan','Kenyamanan','Promo atau pack hemat','Manfaat tertentu'];v=[31,28,23,16,15]
a.barh(names,v,color=[red,navy,navy,grey,grey]);a.invert_yaxis();a.set_xlim(0,37);a.set_xlabel('Jumlah pemilih dari 50 responden • maksimal tiga alasan')
for i,n in enumerate(v):a.text(n+.4,i,f'{n} ({n*2}%)',va='center',fontsize=9)
save(f,'reasons.png')
f,a=plt.subplots(figsize=(7.2,2.8));left=np.zeros(3)
for v,c,l in [([31,6,32],red,'Sendiri'),([19,42,17],navy,'Keluarga'),([0,2,1],grey,'Tidak tahu')]:
 a.barh(range(3),v,left=left,color=c,height=.52,label=l)
 for i,n in enumerate(v):
  if n>=2:a.text(left[i]+n/2,i,str(n),ha='center',va='center',color='white' if c!=grey else 'black')
 left+=v
a.set_yticks(range(3),['Memilih','Membiayai','Membeli']);a.invert_yaxis();a.set_xlabel('Jumlah responden dari 50');a.legend(ncol=3,frameon=False,loc='upper center',bbox_to_anchor=(.5,1.23));save(f,'roles.png')
f,a=plt.subplots(figsize=(7.2,2.7));v=[24100/190*100,23500,41900]
a.bar(['Basic 190 g\nharga setara','Premium 100 g\npromo contoh kasus','Premium 100 g\nreguler contoh kasus'],v,color=[navy,grey,red],width=.55)
a.set_ylabel('Rupiah per 100 g');a.set_ylim(0,49000);a.ticklabel_format(style='plain',axis='y')
for i,n in enumerate(v):a.text(i,n+1100,f'Rp{n:,.0f}'.replace(',','.'),ha='center')
save(f,'prices.png')
f,a=plt.subplots(figsize=(7.4,4.6));a.set_xlim(0,10);a.set_ylim(0,7);a.axis('off')
def box(x,y,w,h,t,col=pale):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.04,rounding_size=.03',facecolor=col,edgecolor=navy));a.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=9)
def arrow(x,y,u,v,label=None):
 a.add_patch(FancyArrowPatch((x,y),(u,v),arrowstyle='->',mutation_scale=10,color=navy))
 if label:
  if abs(y-v)<.1:a.text((x+u)/2,y+.55,label,fontsize=8,ha='center',va='bottom')
  else:a.text((x+u)/2+.05,(y+v)/2,label,fontsize=8,va='center')
box(.1,5.5,2.9,1,'Riwayat dan kebutuhan\nWeb merek + pengguna')
box(3.6,5.5,2.8,1,'Manfaat relevan?\nPengguna memilih')
box(7,5.5,2.8,1,'Basic memadai\nEdukasi tetap ada')
arrow(3,6,3.6,6);arrow(6.4,6,7,6,'Tidak')
box(3.6,3.65,2.8,1,'Simpan SKU dan harga\nPilih rute belanja')
arrow(5,5.5,5,4.65,'Ya')
box(.1,1.8,2.9,1,'Tidak cocok / keluhan\nHentikan atau rujuk')
box(3.6,1.8,2.8,1,'Beli lalu nilai\nRitel + bukti')
box(7,1.8,2.8,1,'Harga / stok belum pasti\nKonfirmasi dulu')
arrow(5,3.65,5,2.8);arrow(6.4,4.15,8.4,2.8);arrow(7,2.3,6.4,2.3);arrow(3.6,2.3,3,2.3)
box(3.6,.05,2.8,1,'Cek sisa sesuai izin\nBeli / tunda / berhenti')
arrow(5,1.8,5,1.05,'Cocok');save(f,'flow.png')
f,a=plt.subplots(figsize=(7.4,2.55));tasks=[('Persetujuan dan penyiapan',0,1),('Kelayakan dan perbaikan',0,2),('Pembanding dan kohort matang',1,3),('Layanan dan audit berulang',2,10),('Replikasi bersyarat',4,8)]
for i,(n,start,dur) in enumerate(tasks):a.barh(i,dur,left=start,color=navy if i<3 else grey,height=.55)
a.set_yticks(range(5),[x[0] for x in tasks]);a.invert_yaxis();a.set_xticks(np.arange(12)+.5,[f'{i//4+1}Q{i%4+1}' for i in range(12)],fontsize=8);a.set_xlim(0,12);a.set_xlabel('Tahun dan kuartal sejak mulai program');a.grid(axis='x',alpha=.15);save(f,'roadmap.png')
F=json.loads((R/'finance/finance.json').read_text())
f,a=plt.subplots(figsize=(7.4,2.2));
for key,col,label in [('downside',grey,'Bawah'),('base',navy,'Dasar'),('upside',red,'Atas')]:
 rows=F['cases'][key]['quarterly'];v=[-F['cases'][key]['assumptions']['launch_cost']/1e6]+[r['cumulative_program_cash']/1e6 for r in rows]
 a.plot(range(13),v,color=col,label=label,lw=1.7)
a.axhline(0,color='black',lw=.6);a.set_xticks(range(13),['T0']+[r['period'] for r in rows],rotation=45,fontsize=8);a.set_ylabel('Kas kumulatif • juta Rp');a.legend(frameon=False,ncol=3);a.grid(axis='y',alpha=.12);save(f,'cash.png')
f,a=plt.subplots(figsize=(7.4,1.9));d=[x for x in F['sensitivity'] if x['driver']=='screen_cost'];a.plot([x['value'] for x in d],[x['npv']/1e6 for x in d],'-o',color=navy);a.axhline(0,color=red,lw=.8);a.axvline(F['thresholds_zero_npv']['max_screen_cost_idr'],color=grey,ls='--');a.set_xlabel('Biaya per orang disaring • Rp');a.set_ylabel('NPV tiga tahun • juta Rp');a.grid(alpha=.12);save(f,'sensitivity.png')
print('Charts generated')
