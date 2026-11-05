from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
import numpy as np
import textwrap
P=Path(__file__).resolve().parents[1]/'figures';P.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'normal','figure.dpi':160,'savefig.dpi':220})
RED='#BE283F';NAVY='#234B63';GRAY='#B6BFC5';PALE='#F1F3F4';GREEN='#426C64'
def save(fig,name):
 fig.savefig(P/(name+'.png'),bbox_inches='tight',facecolor='white');fig.savefig(P/(name+'.svg'),bbox_inches='tight',facecolor='white');plt.close(fig)
f,a=plt.subplots(figsize=(7.1,3.05));ys=np.arange(3);left=np.zeros(3)
for vals,col,label in [([30,6,31],RED,'Responden sendiri'),([19,41,17],NAVY,'Keluarga'),([0,2,1],GRAY,'Tidak tahu')]:
 a.barh(ys,vals,left=left,color=col,label=label,height=.52)
 for y,v,l in zip(ys,vals,left):
  if v>=2:a.text(l+v/2,y,str(v),ha='center',va='center',color='white' if col!=GRAY else 'black',fontsize=11)
 left+=vals
a.set(yticks=ys,yticklabels=['Memilih','Membiayai','Membeli'],xlim=(0,49),xlabel='Jumlah responden dari 49');a.invert_yaxis();a.legend(ncol=3,loc='upper center',bbox_to_anchor=(.5,1.23),frameon=False,fontsize=9);save(f,'roles')
f,a=plt.subplots(figsize=(6.9,3.4));names=['Uang tersedia','Kebiasaan memakai','Rasa atau kenyamanan','Manfaat tertentu','Promo atau paket hemat','Pilihan pembeli / penyedia','Stok rumah','Produk lama tidak sesuai'];vals=[30,28,23,15,15,6,5,3]
a.barh(names,vals,color=[RED,RED,NAVY,NAVY,GRAY,GRAY,GRAY,GRAY],height=.62);a.invert_yaxis();a.set(xlim=(0,35),xlabel='Dipilih responden dari 49  •  Maksimal tiga jawaban')
for i,v in enumerate(vals):a.text(v+.4,i,f'{v} ({v/49:.1%})',va='center',fontsize=9)
save(f,'drivers')
f,a=plt.subplots(figsize=(6.5,3.6));m=np.array([[2,6],[3,10]]);a.imshow(m,cmap='Blues',vmin=0,vmax=12)
for i in range(2):
 for j in range(2):a.text(j,i,str(m[i,j]),ha='center',va='center',fontsize=22,color='white' if m[i,j]>7 else 'black')
a.set_xticks([0,1],['Tidak','Ya']);a.set_yticks([0,1],['Tidak','Ya']);a.set_xlabel('Kategori perawatan diri lain');a.set_ylabel('Pasta gigi');a.text(.5,1.19,'21 pasangan yang memenuhi syarat  |  Selisih 14,3 poin persentase',transform=a.transAxes,ha='center',fontsize=10);save(f,'paired')
f,a=plt.subplots(figsize=(6.6,2.8));a.barh([0,1],[31,34],color=GRAY,height=.45);a.barh([0,1],[22,22],color=NAVY,height=.45);a.set(yticks=[0,1],yticklabels=['Tidak ada pilihan khusus','Mengaku mendapat yang diinginkan'],xlim=(0,39),xlabel='Jumlah responden');a.invert_yaxis();
for y,total in enumerate([31,34]):a.text(total+.5,y,str(total),va='center')
a.text(11,.5,'22 orang berada\npada kedua kelompok',ha='center',va='center',fontsize=10);save(f,'preference')
f,a=plt.subplots(figsize=(6.5,3.1));labels=['Basic 190 g\nHarga unit setara','Premium 100 g\nContoh promo','Premium 100 g\nHarga reguler'];v=[24100/190*100,23500,41900];a.bar(labels,v,color=[NAVY,GRAY,RED],width=.58);a.set_ylabel('Rupiah per 100 g');a.set_ylim(0,48000);a.set_yticks([0,10000,20000,30000,40000],['0','10.000','20.000','30.000','40.000'])
for i,n in enumerate(v):a.text(i,n+1000,f'Rp{n:,.0f}'.replace(',','.'),ha='center')
save(f,'case_prices')
def process(name,labels,sub):
 f,a=plt.subplots(figsize=(7.2,2.2));a.set_xlim(0,10);a.set_ylim(0,2.6);a.axis('off');xs=[.1,3.55,7.0]
 for i,(x,label,s) in enumerate(zip(xs,labels,sub)):
  a.add_patch(Rectangle((x,1.15),2.85,.95,edgecolor=NAVY,facecolor=PALE,lw=1));a.text(x+1.425,1.63,'\n'.join(textwrap.wrap(label,18)),ha='center',va='center',fontsize=10);a.text(x+1.425,.65,s,ha='center',va='center',fontsize=9)
  if i<2:a.add_patch(FancyArrowPatch((x+2.9,1.63),(xs[i+1]-.05,1.63),arrowstyle='->',mutation_scale=13,color=NAVY))
 save(f,name)
process('architecture',['Manfaat\nrelevan','Pembelian\nterlaksana','Penggantian\nterencana'],['Kebutuhan, kecocokan,\nekspektasi yang wajar','Varian, gramasi, harga,\npembeli dan pembiaya','Waktu pilihan pengguna,\nharga nyata, bukti pembelian'])
process('pillar1',['Nyatakan kebutuhan','Coba bila sesuai','Nilai pengalaman'],['Pilihan Basic tetap tersedia','Gunakan produk tersegel\ndan klaim yang disetujui','Nyaman bukan bukti klinis;\nlanjut hanya bila bernilai'])
process('pillar2',['Simpan pilihan tepat','Pilih cara berbelanja','Konfirmasi yang dibeli'],['Nama dan foto varian,\ngramasi, harga total\ndan per 100 g','Belanja sendiri atau bagikan\nke pembeli bila diperlukan','Struk atau kemasan;\ncatat varian pengganti'])
process('pillar3',['Tentukan waktu sendiri','Cek pilihan dan harga','Beli atau berhenti'],['Sisa produk dan pemakai\nbukan jadwal seragam','Stok perlu dikonfirmasi;\npilihan dapat diubah','Tanpa subsidi ulang program;\nsimpan hasil dan alasannya'])
f,a=plt.subplots(figsize=(6.5,3.2));x=np.arange(2);a.plot(x,[1600,960],'-o',color=RED,label='Intervensi');a.plot(x,[1000,450],'-o',color=NAVY,label='Pembanding');a.set_xticks(x,['Pembelian berbayar pertama','Pembelian berbayar kedua']);a.set(ylabel='Orang pada skenario',ylim=(0,1900));a.legend(frameon=False)
for x,y in [(0,1600),(1,960),(0,1000),(1,450)]:a.annotate(str(y),(x,y),xytext=(0,9),textcoords='offset points',ha='center')
save(f,'model_funnel')
f,a=plt.subplots(figsize=(6.5,3.1));labels=['Kontribusi tambahan','Biaya program','Hasil bersih'];v=[6.66,-40,-33.34];a.barh(labels,v,color=[NAVY,GRAY,RED],height=.5);a.axvline(0,color='black',lw=.7);a.invert_yaxis();a.set(xlabel='Juta rupiah  •  Skenario dasar 180 hari',xlim=(-48,14))
for i,n in enumerate(v):a.text(n+(.8 if n>=0 else -.8),i,str(n).replace('.',','),ha='left' if n>=0 else 'right',va='center')
save(f,'contribution')
f,a=plt.subplots(figsize=(6.5,3));x=np.linspace(3500,9000,100);a.plot(x,.111*x,color=NAVY,lw=2);a.axhline(1000,color=GRAY,ls='--',label='Contoh biaya variabel Rp1.000 per kontak');a.scatter([6000],[666],color=RED,zorder=3);a.annotate('Skenario dasar Rp666',(6000,666),xytext=(5000,450),arrowprops={'arrowstyle':'->','color':RED},fontsize=9);a.set(xlabel='Kontribusi bersih per ekuivalen 100 g  •  Rupiah',ylabel='Batas biaya per kontak  •  Rupiah',ylim=(0,1200));a.legend(frameon=False,fontsize=8);save(f,'breakeven')
print('Figures built',len(list(P.glob('*.png'))))
