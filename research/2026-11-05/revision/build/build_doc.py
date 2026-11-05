from pathlib import Path
import json, math, re
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION_START

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'documents/Pepsodent_Executive_Summary_Revised.docx'
AS=ROOT/'assets'
NAVY='234B63'; RED='B52B40'; BORDER='D9D9D9'
doc=Document()
sec=doc.sections[0]
sec.page_width=Cm(21); sec.page_height=Cm(29.7)
for k in ['top_margin','bottom_margin','left_margin','right_margin']: setattr(sec,k,Cm(2.5))
sec.header_distance=Cm(1.05);sec.footer_distance=Cm(1.1)
for name,size,bold in [('Normal',12,False),('Title',16,True),('Heading 1',14,True),('Heading 2',12,True),('Caption',10.5,False)]:
 s=doc.styles[name];s.font.name='Times New Roman';s.font.size=Pt(size);s.font.bold=bold;s.font.color.rgb=RGBColor(0,0,0)
 s.paragraph_format.line_spacing=1.15;s.paragraph_format.space_after=Pt(5)
 s.paragraph_format.space_before=Pt(0)
 if name.startswith('Heading'):s.paragraph_format.keep_with_next=True
doc.styles['Normal'].paragraph_format.widow_control=True
for st in doc.styles:
 for el in list(st.element.iter()):
  if el.tag==qn('w:rFonts'):
   for k in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme','csTheme']:
    el.attrib.pop(qn('w:'+k),None)
   el.set(qn('w:ascii'),'Times New Roman');el.set(qn('w:hAnsi'),'Times New Roman')
  if el.tag==qn('w:pBdr'):el.getparent().remove(el)

counter=1
def bookmark(p,name):
 global counter
 a=OxmlElement('w:bookmarkStart');a.set(qn('w:id'),str(counter));a.set(qn('w:name'),name)
 b=OxmlElement('w:bookmarkEnd');b.set(qn('w:id'),str(counter));counter+=1
 p._p.insert(0,a);p._p.append(b)
def link(p,label,target):
 h=OxmlElement('w:hyperlink');h.set(qn('w:anchor'),target)
 r=OxmlElement('w:r');pr=OxmlElement('w:rPr')
 for tag,val in [('color','000000'),('u','single')]:
  x=OxmlElement('w:'+tag);x.set(qn('w:val'),val);pr.append(x)
 r.append(pr);t=OxmlElement('w:t');t.text=label;r.append(t);h.append(r);p._p.append(h)
def p(text='',style=None,bold=None,size=None):
 x=doc.add_paragraph(style=style)
 x.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY if not style else WD_ALIGN_PARAGRAPH.LEFT
 # Inline references use [[label|bookmark]].
 for i,s in enumerate(re.split(r'(\[\[.*?\|.*?\]\])',text)):
  if s.startswith('[['):
   label,target=s[2:-2].split('|',1);link(x,label,target)
  else:
   r=x.add_run(s)
   if bold is not None:r.bold=bold
   if size:r.font.size=Pt(size)
 return x
def h(text,id=None,level=1):
 x=p(text,'Heading '+str(level))
 if id:bookmark(x,id)
 return x
def note(text):
 x=p(text,size=10);x.paragraph_format.line_spacing=1.05
 return x
def page():doc.add_page_break()
def table(headers,rows,widths=None):
 t=doc.add_table(rows=1,cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 if widths:
  for c,w in zip(t.columns,widths):c.width=Cm(w)
 for j,x in enumerate(headers):t.rows[0].cells[j].text=str(x)
 for row in rows:
  cells=t.add_row().cells
  for j,v in enumerate(row):cells[j].text=str(v)
 for ri,row in enumerate(t.rows):
  pr=row._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
  if ri==0:pr.append(OxmlElement('w:tblHeader'))
  for j,c in enumerate(row.cells):
   c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   if widths:c.width=Cm(widths[j])
   tcPr=c._tc.get_or_add_tcPr();b=OxmlElement('w:tcBorders')
   for side in ['top','left','bottom','right']:
    e=OxmlElement('w:'+side);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),BORDER);b.append(e)
   tcPr.append(b)
   mar=OxmlElement('w:tcMar')
   for side in ['top','left','bottom','right']:
    e=OxmlElement('w:'+side);e.set(qn('w:w'),'85');e.set(qn('w:type'),'dxa');mar.append(e)
   tcPr.append(mar)
   if ri==0:
    s=OxmlElement('w:shd');s.set(qn('w:fill'),'E8EEF1');tcPr.append(s)
   for par in c.paragraphs:
    par.paragraph_format.space_after=Pt(1);par.paragraph_format.space_before=Pt(0);par.paragraph_format.line_spacing=1.05
    for r in par.runs:r.font.name='Times New Roman';r.font.size=Pt(10);r.bold=ri==0
 doc.add_paragraph().paragraph_format.space_after=Pt(1)
 return t
def fig(name,caption,width=15.8):
 x=doc.add_paragraph();x.paragraph_format.keep_with_next=True;x.paragraph_format.space_after=Pt(2)
 x.add_run().add_picture(str(AS/name),width=Cm(width))
 x.alignment=WD_ALIGN_PARAGRAPH.CENTER
 p(caption,'Caption')
def app(id,title,back='core_solution',newpage=True):
 heading=h('Lampiran '+id+'  '+title,'app_'+id)
 if newpage:heading.paragraph_format.page_break_before=True
 x=p();link(x,'Kembali ke ringkasan',back);x.add_run('  ·  ');link(x,'Indeks lampiran','appendix_index')
 for r in x.runs:r.font.size=Pt(10)
def money(v,dec=1):return f'{v/1e6:,.{dec}f}'.replace(',','X').replace('.',',').replace('X','.')

# Reserved identity fields are intentional owner completion items.
sp=p('');sp.paragraph_format.space_after=Pt(110)
p('Mengembalikan nilai Pepsodent Premium pada pembelian berikutnya','Title')
p('Pepsodent Sesuai Saya','Heading 1')
p('Economics Festival 2026',bold=True)
p('[Nama tim]');p('[Nama ketua dan anggota tim]')
p('[Tempat logo resmi Economics Festival 2026 dan Unilever]',size=11)
sec=doc.add_section(WD_SECTION_START.NEW_PAGE)
sec.header.is_linked_to_previous=False;sec.footer.is_linked_to_previous=False
head=sec.header.paragraphs[0];head.alignment=WD_ALIGN_PARAGRAPH.RIGHT
rr=head.add_run('[Logo resmi Economics Festival 2026 dan Unilever]');rr.font.name='Times New Roman';rr.font.size=Pt(8)
foot=sec.footer.paragraphs[0];foot.alignment=WD_ALIGN_PARAGRAPH.RIGHT
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');foot._p.append(fld)
pg=OxmlElement('w:pgNumType');pg.set(qn('w:start'),'1');sec._sectPr.append(pg)

main=json.loads((ROOT/'build/main.json').read_text())
for idx,blocks in enumerate(main):
 if idx:page()
 for b in blocks:
  if b['type']=='h':h(b['text'],b.get('id'),b.get('level',1))
  else:p(b['text'])

page();h('Daftar pustaka','references')
refs=json.loads((ROOT/'build/references.json').read_text())
for text in sorted(refs,key=str.casefold):
 x=p(text);x.alignment=WD_ALIGN_PARAGRAPH.LEFT;x.paragraph_format.left_indent=Cm(.7);x.paragraph_format.first_line_indent=Cm(-.7)
 for r in x.runs:r.font.size=Pt(11)

page();h('Bukti dan rancangan dapat ditelusuri per keputusan','appendix_index')
p('Lampiran menghubungkan temuan, pilihan strategi, pengalaman pengguna, pelaksanaan, dan kelayakan investasi. Angka survei bersifat deskriptif; target serta proyeksi menggunakan estimasi tim.')
index=[('A1','Kasus dan survei menjawab pertanyaan yang berbeda'),('A2','Pilihan pribadi tetap bergantung pada konteks pembelian'),('A3','Kebutuhan dan riwayat produk menentukan sasaran'),('B1','Pengalaman relevan menjadi inti di antara tiga alternatif'),('B2','Kebaruan terletak pada kelanjutan setelah pemilihan'),('C1','Satu catatan mengikuti keputusan pengguna sampai pembelian ulang'),('C2','Pengalaman sehari hari memperlihatkan peran setiap pilar'),('C3','Antarmuka menjaga pilihan dan kendali pengguna'),('D1','Pelaksanaan bertahap menyiapkan layanan yang berulang'),('D2','Keberhasilan sosial dan komersial memakai ukuran berbeda'),('D3','Risiko ditangani oleh pemilik keputusan yang jelas'),('E1','Investasi diarahkan pada layanan ringan yang dapat digunakan ulang'),('E2','Setiap kuartal menanggung biaya dan kontribusinya sendiri'),('E3','Pengembalian bergantung pada volume tambahan dan disiplin biaya'),('E4','Asumsi terbuka menentukan batas keputusan investasi'),('E5','Rumus dan kapasitas memperjelas batas pendanaan')]
for id,title in index:
 x=p();link(x,id+'  '+title,'app_'+id)

app('A1','Kasus dan survei menjawab pertanyaan yang berbeda','core_problem')
p('Kasus menempatkan penurunan porsi Premium sebagai masalah bisnis. Survei tim menambahkan konteks keputusan pembelian, sehingga keduanya dipakai bersama tanpa mencampurkan populasi atau periode.')
table(['Dasar bukti','Temuan','Penggunaan dalam proposal'],[
 ['Kasus penyelenggara','Porsi Premium 27% (2022) menjadi 20% (H1 2026)','Diagnosis bisnis; perubahan tujuh poin persentase, bukan kerugian laba absolut'],
 ['Survei ilustratif kasus','1.200 usia 18–30; alasan pengalih dari 540 orang, jawaban ganda','Kesetaraan manfaat 44%, selisih harga 39%, hasil tidak terasa dalam dua minggu 31%, promo Basic 28%, bingung varian 24%'],
 ['Survei eksploratif tim','51 respons; 50 disertakan; seluruhnya usia 18–24 dan masih pendidikan','Perancangan pengalaman, jalur belanja, dan pengukuran; tidak mengestimasi pangsa nasional'],
 ['Riwayat produk','Belum ada perpindahan Premium ke Basic yang terverifikasi','Rekrut kohort sasaran melalui identitas SKU dan riwayat pembelian'],
 ],[3.1,5.2,7.7])
fig('reasons.png','Gambar A1  Harga kebiasaan dan kenyamanan beririsan dalam alasan pilihan')
note('Sumber: Economics Festival (2026a); Tim Pepsodent E Fest (2026). Pertanyaan alasan tim dibatasi maksimal tiga pilihan. Persentase kasus bukan hasil survei tim. Sampel kemudahan tidak mewakili seluruh dewasa muda.')
table(['Pemeriksaan mutu','Hasil dan konsekuensi'],[
 ['Kelayakan','Satu respons di bawah 18 tahun dikeluarkan; 50 respons memenuhi gerbang persetujuan, usia, lingkup, dan kelengkapan.'],
 ['Kesesuaian sumber','35 kolom substantif raw dan CLEAN sesuai; hitungan dihitung ulang dari baris. Sepuluh sel ringkasan salah berformat tanggal.'],
 ['Harga dan ingatan','Lima respons berflag diperiksa lewat sensitivitas. Harga Rp190 dan isian harga tak pasti tidak diperbaiki secara diam diam.'],
 ['Batas waktu','Sebagian besar episode dengan bulan terisi terjadi setelah H1 2026; episode itu membantu desain saat ini.'],
 ],[3.4,12.6])

app('A2','Pilihan pribadi tetap bergantung pada konteks pembelian','core_problem')
fig('roles.png','Gambar A2  Memilih membeli dan membiayai adalah peran yang berbeda')
table(['Temuan dari 50 respons','Makna bagi desain','Batas interpretasi'],[
 ['24 memilih dan berbelanja sendiri dengan dana keluarga','Utamakan item tersimpan untuk pembeli mandiri','Pendanaan keluarga tidak menunjukkan veto atau pendapatan'],
 ['32 tidak memiliki pilihan khusus; 22 di antaranya merasa mendapat yang diinginkan','Tanyakan kebutuhan sebelum menawarkan manfaat tambahan','Kepuasan terhadap pilihan standar dapat rasional'],
 ['39 berbelanja di minimarket atau supermarket','Kartu varian dapat dibawa ke rak; daring tetap tersedia','Tidak mengukur ketersediaan SKU tiap toko'],
 ['38 mengganti produk habis atau hampir habis','Tanyakan sisa produk dan kapan bantuan berguna','Habis tidak sama dengan lupa atau kehilangan loyalitas'],
 ['Dua melaporkan pencarian gagal','Tangani sebagai pengecualian','Tidak menempatkan stok kosong sebagai akar masalah utama'],
 ],[5,6.4,4.6])
h('Perbandingan kategori memberi petunjuk yang terbatas',level=2)
p('Dalam 21 pasangan yang memenuhi syarat, sepuluh membandingkan kedua kategori, enam hanya kategori lain, tiga hanya pasta gigi, dan dua tidak membandingkan keduanya. Selisih 14,3 poin persentase dengan uji eksak p = 0,508 tidak menetapkan pola populasi. Temuan ini digunakan untuk menguji relevansi konten, bukan menyimpulkan bahwa pembeli skincare mampu atau bersedia membayar Premium.')
note('Sumber: Tim Pepsodent E Fest (2026), perhitungan ulang ekspor terbaru. Penyebut pada tabel adalah 50 kecuali disebut lain; jawaban ganda dan konstruk antarpertanyaan tidak dijumlahkan.')

app('A3','Kebutuhan dan riwayat produk menentukan sasaran','core_solution')
h('STP memusatkan investasi pada kebutuhan yang masih bernilai',level=2)
table(['Tahap','Keputusan strategis','Aturan pelaksanaan'],[
 ['Segmentasi','Riwayat Premium/Basic × kebutuhan tambahan × kendali belanja × rute dan pemakaian bersama','Usia dan tempat tinggal menjadi konteks, bukan proksi ketergantungan atau kemampuan membayar'],
 ['Target utama','Usia 18–30 yang pernah menggunakan Premium, kini Basic, dan masih memiliki kebutuhan relevan','Riwayat SKU dikonfirmasi dengan foto/struk bila tersedia atau penelusuran terstruktur; kasus ambigu dilaporkan terpisah'],
 ['Target peluncuran','Mahasiswa yang memenuhi kriteria utama dan dapat dijangkau melalui kanal yang diizinkan','Ini pilihan akses, bukan estimasi ukuran pasar; usia 25–30 dan nonmahasiswa direkrut sebelum generalisasi'],
 ['Target sekunder','Pengguna berkebutuhan relevan tanpa riwayat perpindahan yang cukup','Pelayanan dapat tersedia; hasil kohort dipisah dari pengembalian pengguna Premium'],
 ['Positioning','Pilihan manfaat yang sesuai dan layak dipertahankan pada pembelian berikutnya','Basic tetap pilihan; harga total dan harga unit terlihat sebelum komitmen'],
 ],[2.6,6.7,6.7])
h('Tiga persona situasional mengubah bantuan yang diberikan',level=2)
table(['Persona situasional','Bukti dan pekerjaan pengguna','Respons layanan'],[
 ['Pemilih mandiri dengan dana keluarga','24/50 memilih sekaligus berbelanja sendiri dengan dana keluarga. Perlu pilihan yang cocok dengan dana akuisisi.','Simpan SKU, gramasi, total harga, dan harga unit; berbagi hanya bila dibutuhkan.'],
 ['Pengguna yang menerima pilihan standar','32/50 tanpa pilihan khusus; 22/32 merasa mendapat produk yang diinginkan. Perlu alasan tambahan yang benar benar relevan.','Jelaskan kebutuhan dan pembanding; tidak ada dorongan upgrade bila Basic memadai.'],
 ['Pengguna yang sudah menghargai manfaat','20/50 melaporkan manfaat produk sebelumnya terasa dan penting. Perlu melanjutkan pilihan bila masih sesuai.','Lewati percobaan yang tidak perlu, cek sisa, harga dan pembelian berikutnya.'],
 ],[3.8,6.4,5.8])
note('Sumber: Tim Pepsodent E Fest (2026); STP dan persona merupakan sintesis desain tim. Persona dapat beririsan, bukan klaster statistik, dan tidak memverifikasi bahwa anggota sampel adalah mantan pengguna Premium. Tidak dibuat nama, pendapatan, atau kutipan fiktif.')

app('B1','Pengalaman relevan menjadi inti di antara tiga alternatif','core_solution')
p('Ketiga alternatif dinilai terhadap pembelian Premium tambahan yang sesuai kebutuhan, biaya layanan, relevansi kanal, serta manfaat pendidikan. Perbandingan ini merupakan penilaian desain tim; belum ada eksperimen yang menetapkan pemenang.')
table(['Alternatif','Kekuatan','Keterbatasan dan keputusan'],[
 ['Pilihan Tepat — layanan daftar varian','Murah dan membantu menyampaikan SKU ke pembeli','Banyak pengguna sudah memilih dan berbelanja sendiri; alat ini tidak menciptakan alasan menghargai manfaat. Dipertahankan sebagai fungsi pendukung.'],
 ['Sesuai Saya — pengalaman manfaat relevan','Menghubungkan kebutuhan, ekspektasi, biaya, pengalaman dan kelanjutan','Dipilih sebagai inti; trial selektif dan pembelian normal mengendalikan biaya.'],
 ['Lanjutkan Pilihan — bantuan penggantian','Mendukung niat yang sudah ada saat produk menipis','Kelupaan dan kegagalan pasokan belum dominan dalam data; digunakan setelah kebutuhan dan kecocokan jelas.'],
 ],[4.2,5.3,6.5])
h('Enam P membedakan pilihan strategi secara operasional',level=2)
table(['6P','Pilihan Tepat','Sesuai Saya','Lanjutkan Pilihan'],[
 ['Product','Informasi SKU dan padanan','Manfaat sesuai kebutuhan dan evaluasi pengalaman','Kelanjutan pilihan yang sudah bernilai'],
 ['Price','Harga total dan per 100 g','Harga trial serta biaya beli ulang terlihat; pembelian normal menjadi standar','Harga baru dikonfirmasi sebelum penggantian'],
 ['Place','Kartu untuk rak atau tautan toko','Mobile web merek, WhatsApp berizin, ritel yang tersedia','Rute ritel pilihan pengguna'],
 ['Promotion','Kejelasan pilihan dan berbagi','Konten kebutuhan serta ekspektasi yang disetujui','Pengingat relevan tanpa voucher berulang'],
 ['Positioning','Varian yang dimaksud terbeli','Tambahan manfaat layak dipertahankan','Pilihan tepat tetap berlanjut'],
 ['Pack','Foto dan berat pack yang ada','Kemasan produsen yang ada dan tersegel; tanpa pack baru','Sisa produk dan jumlah pemakai menentukan waktu'],
 ],[2.3,4.3,5,4.4])
note('Sumber: Economics Festival (2026a); Tim Pepsodent E Fest (2026); rancangan tim. Semua alternatif menggunakan kanal digital; tidak memerlukan aplikasi baru atau asumsi kontrak ritel yang sudah ditandatangani.')

app('B2','Kebaruan terletak pada kelanjutan setelah pemilihan','core_solution')
table(['Pembanding yang terdokumentasi','Pelajaran yang dapat dipakai','Kontribusi konfigurasi usulan'],[
 ['Pepsodent AI Denta Scan dan konsultasi daring','Kapabilitas pengenalan kebutuhan dan akses profesional telah diumumkan pada 2024','Tidak membangun pemindai baru; menyambungkan pilihan nonklinis ke harga aktual, belanja, pengalaman dan penggantian'],
 ['Sensodyne Indonesia Online Check Up','Profil dapat disimpan; halaman menjelaskan informasi produk serta sampel/kupon','Menghindari klaim kuis sebagai kebaruan; outcome usulan adalah pembelian berbayar tambahan'],
 ['AnyList Create and share lists','Item dan foto dapat membantu komunikasi daftar belanja','Berbagi menjadi opsi untuk pembeli lain; pembelian sendiri tetap rute utama'],
 ['WhatsApp Business Platform','Percakapan dan pesan bertemplat dapat mendukung tindak lanjut berizin','Biaya, kategori pesan dan opt out dihitung; pengingat bukan langganan atau debit otomatis'],
 ],[4.5,5.5,6])
p('Nilai usulan terletak pada satu catatan kebutuhan dan SKU yang tetap berguna saat harga berubah, orang lain berbelanja, atau produk menipis. Integrasi tersebut memberi titik ukur pembelian, sehingga keberhasilan tidak berhenti pada kuis, tayangan, atau klaim sampel. Keberadaan komponen pembanding mendukung kelayakan fungsi; tidak menjadi bukti kenaikan penjualan program.')
note('Sumber: Unilever Indonesia (2024); Haleon (n.d.); AnyList (n.d.); Twilio (n.d.). Pembanding ditinjau 5 November 2026; keberadaan halaman bukan konfirmasi kontrak atau integrasi yang aktif untuk program ini.')
h('Harga percobaan tidak menghapus selisih biaya pemakaian',level=2)
fig('prices.png','Gambar B1  Harga unit tetap berbeda walaupun harga satu tabung promo lebih rendah')
note('Sumber: Economics Festival (2026a). Basic Rp24.100/190 g = Rp12.684 per 100 g; Premium promo Rp23.500/100 g dan reguler Rp41.900/100 g. Harga contoh kasus, bukan janji harga ritel saat pelaksanaan.')

app('C1','Satu catatan mengikuti keputusan pengguna sampai pembelian ulang','core_solution')
fig('flow.png','Gambar C1  Alur layanan menyertakan pilihan lanjut berhenti dan penanganan pengecualian')
table(['Titik keputusan','Data minimum','Pelaksana dan respons'],[
 ['Masuk dan memenuhi sasaran','Usia, riwayat produk, tujuan; izin analisis terpisah dari izin pesan','Web/staf menyaring; nonkohort tetap dapat mengakses pendidikan'],
 ['Kebutuhan dan pilihan','Manfaat yang dicari, varian, ukuran, batas ekspektasi','Pengguna memilih; materi merek disetujui regulatori; keluhan diarahkan ke layanan profesional'],
 ['Pembelian pertama','SKU, gramasi, harga bertanggal, struk/foto kemasan','Ritel menjual seperti biasa; verifikasi otomatis dan audit sampel menangani bukti'],
 ['Pengalaman dan sisa','Kenyamanan, relevansi, jumlah pemakai, waktu yang diinginkan','Tidak cocok: hentikan penawaran; sudah cocok: lewati trial tambahan'],
 ['Pembelian berikutnya','Transaksi terpisah, harga dan subsidi program','Dedup per transaksi/tabung; pengguna dapat menunda atau berhenti'],
 ],[3.7,5.6,6.7])
note('Sumber: rancangan tim. Garis proses menunjukkan layanan yang diusulkan; tidak menyatakan bahwa perangkat lunak, mitra, atau akses harga sudah beroperasi.')

app('C2','Pengalaman sehari hari memperlihatkan peran setiap pilar','core_solution')
fig('lifestyle.png','Gambar C2  Konsep pengalaman kebutuhan belanja dan penggantian',15.8)
p('Pilar pertama dimulai pada rutinitas pengguna: kebutuhan dinyatakan dan produk yang sudah dipakai dibandingkan dengan manfaat tambahan. Percobaan dilakukan melalui pembelian berbayar bila diperlukan, menggunakan kemasan produsen yang disetujui. Pengguna yang sudah mengenal manfaat dapat melanjutkan tanpa trial.')
p('Pilar kedua membawa informasi ke tempat transaksi berlangsung. Kartu pilihan memuat identitas SKU, foto resmi, ukuran, harga total dan harga per 100 gram yang diperiksa pada kanal belanja. Kartu dapat disimpan sebagai gambar atau dibagikan kepada pembeli lain.')
p('Pilar ketiga kembali ke keadaan produk yang sungguh dipakai. Pengguna menentukan waktu pemeriksaan sisa dan dapat menolak pesan. Harga penggantian dikonfirmasi sebelum pembelian; pengalaman yang mengecewakan menutup penawaran ulang dan membuka dukungan yang sesuai.')
note('Visualisasi konsep. Adegan dan kemasan pada gambar merupakan ilustrasi usulan, bukan dokumentasi peserta, materi kemasan resmi, pelaksanaan program, atau bukti hasil. Kemasan aktual dan seluruh materi promosi harus memakai aset merek yang disetujui.')
table(['Yang dibuat terlihat','Yang dipertahankan dalam layanan'],[
 ['Pengguna mengendalikan tindakan','Tidak wajib membeli Premium untuk memperoleh pendidikan dasar'],
 ['Belanja berlangsung pada rute biasa','Tidak ada perpindahan paksa ke kanal daring atau kewajiban keluarga membeli paket'],
 ['Penggantian mengikuti kebutuhan','Tidak ada janji satu tabung habis dalam 30 hari atau penagihan otomatis'],
 ],[6,10])

app('C3','Antarmuka menjaga pilihan dan kendali pengguna','core_solution')
fig('ui.png','Gambar C3  Konsep mobile web untuk kebutuhan item tersimpan dan pengingat',15.8)
note('Visualisasi konsep antarmuka; bukan tangkapan aplikasi yang telah diimplementasikan. Tampilan mengilustrasikan fungsi, sedangkan tabel di bawah menetapkan perilaku dan data yang harus tersedia.')
table(['Layar','Isi dan aturan','Kondisi keluar'],[
 ['Kenali kebutuhan','Tujuan pengguna dan pilihan mempertahankan rutinitas; tidak mendiagnosis melalui foto','Basic memadai: simpan rutinitas dan pendidikan; keluhan: layanan profesional'],
 ['Pilihan tersimpan','Tambahkan foto resmi SKU, gramasi, sumber dan tanggal harga, harga total serta per 100 g','Harga belum diketahui: tampilkan belum dikonfirmasi; tidak mengarang harga atau stok'],
 ['Cek sisa produk','Jadwal pilihan pengguna; tautan web tetap berfungsi tanpa WhatsApp','Tidak ada izin pesan: tanpa pesan; opt out: hentikan sesuai SLA'],
 ['Konfirmasi pembelian','Unggah bukti secara sukarela; data pembelian dipisah dari kontak','Bukti belum cukup: status tidak terverifikasi; tidak otomatis dianggap tidak membeli'],
 ],[3.2,7.3,5.5])

app('D1','Pelaksanaan bertahap menyiapkan layanan yang berulang','core_implementation')
table(['Periode relatif','Keluaran dan pemilik','Keputusan sebelum tahap berikutnya'],[
 ['Tahun 1 Q1','Merek/produk/regulatori menyetujui SKU dan klaim; digital menyiapkan web serta izin pesan; keuangan mengunci biaya','Alur awal diuji pada 120 peserta dari kohort kuartal pertama; perbaiki keluhan, bukti dan salah varian sebelum penambahan'],
 ['Tahun 1 Q2','Riset menjalankan pembanding teralokasi dan penelusuran 180 hari; operasi menjalankan pelayanan dan audit','Desain, biaya pembanding dan protokol dibekukan; 25–30 direkrut sebagai strata eksplisit'],
 ['Tahun 1 Q3–Q4','Pemilik kanal menstabilkan layanan; evaluator menyajikan hasil kohort matang','Q3 menstabilkan proses; Q4 dan seterusnya memperluas setelah kohort Q2 matang. Biaya aktual tetap menjadi batas'],
 ['Tahun 2 Q1–Q4','Digital dan operasi memakai ulang aset; perluasan bertahap ke rute atau kelompok yang relevan','Periksa jam layanan, persetujuan mitra, mutu pengalaman dan ekonomi per kohort'],
 ['Tahun 3 Q1–Q4','Merek/keuangan menilai perpanjangan dan replikasi; evaluator memisahkan hasil komersial serta sosial','Replikasi hanya dalam kapasitas; layanan keluhan dan opt out tetap berjalan bila rekrutmen dihentikan'],
 ],[3,7,6])
fig('roadmap.png','Gambar D1  Kapabilitas dibangun sebelum perluasan dan diukur sepanjang tiga tahun')
note('Sumber: rancangan dan estimasi tim. Q1 dimulai setelah persetujuan pelaksanaan, bukan tanggal lomba. Urutan adalah rencana, bukan komitmen perusahaan atau kontrak mitra.')

app('D2','Keberhasilan sosial dan komersial memakai ukuran berbeda','core_implementation')
p('Semua peserta dapat memperoleh materi menyikat dua kali sehari dengan pasta gigi berfluorida selama dua menit, sesuai panduan ADA. Pendidikan teknik dan akses informasi layanan dipisahkan dari promosi produk. Tidak ada dokter sebagai pemeran rekomendasi produk. Pemisahan ini mengikuti batas promosi yang dijelaskan BPOM (American Dental Association, n.d.; BPOM, 2025).')
table(['Hasil','Definisi dan waktu','Target serta keputusan'],[
 ['Pembelian ulang tambahan','Pembelian kedua berbayar / seluruh unit teralokasi; 180 hari, dibanding kontrol','Efek dan interval dilaporkan; subsidi tambahan, promo ritel, stok sisa dan data hilang dipisah'],
 ['Kontribusi portofolio','Kontribusi Premium tambahan dikurangi kontribusi produk sendiri yang tergantikan serta seluruh biaya','Kohort matang menutup biaya berulang; keputusan ekspansi memerlukan arus kas dan beban kerja yang memadai'],
 ['Pemahaman manfaat','Tes fungsi dan batas ekspektasi / seluruh peserta yang dinilai','Estimasi target tim ≥80% benar; semua kehilangan tindak lanjut dilaporkan'],
 ['Pengetahuan kebiasaan','Selisih perubahan skor tes intervensi dan kontrol pada hari ke 30','Target tim +10 poin persentase; tidak disamakan dengan penurunan penyakit'],
 ['Teknik menyikat','Perubahan rubrik pengamatan pada subsampel berizin dan evaluator terlatih','Lima elemen teknik ditetapkan sebelum pengamatan; hasil deskriptif dan pembanding dilaporkan'],
 ['Akses rujukan','Selesai / seluruh peserta yang disarankan profesional; 90 hari','Target tim 50%; status tidak diketahui dan izin tindak lanjut dipisahkan'],
 ['Mutu layanan','Izin pesan, opt out, salah varian, keluhan dan bukti','Target ≥95% opt out selesai satu hari kerja; ≥90% item lengkap; audit bukti dan waktu layanan'],
 ],[3.5,6.5,6])
h('Pembanding menjaga klaim tambahan tetap dapat ditafsirkan',level=2)
p('Kontrol memperoleh pendidikan dasar yang sama dan praktik ritel biasa; kelompok intervensi memperoleh layanan tiga pilar. Unit alokasi mengikuti pengguna atau rumah tangga yang berbagi tabung. Riwayat SKU dan kebutuhan diperiksa sebelum alokasi; bukti tersedia serta hasil audit riwayat dibedakan dari laporan sendiri. Satu kohort pembanding pembelajaran sekitar 1.000 unit disediakan dalam cadangan riset awal. Ukuran uji yang diperlukan ditetapkan dari baseline, efek minimum, klaster dan kehilangan tindak lanjut; cadangan tersebut tidak dianggap menjamin daya uji. Semua unit teralokasi tetap masuk penyebut, dengan analisis data hilang dan promosi ritel dicatat terpisah.')
note('Sumber: rancangan tim; ADA (n.d.); BPOM (2025). Pengukuran penyakit tidak dimodelkan. Biaya pengukuran dan pembanding dimasukkan ke rancangan biaya, dengan cakupan aktual dikunci sebelum pelaksanaan.')

app('D3','Risiko ditangani oleh pemilik keputusan yang jelas','core_implementation')
table(['Keputusan atau kegiatan','Penanggung jawab akhir','Pelaksana dan dukungan'],[
 ['SKU klaim dan materi','Pemilik merek','Produk/regulatori; edukator mengelola materi kebiasaan terpisah'],
 ['Harga kanal dan ketersediaan','Pemilik perdagangan','Ritel memberi data yang disepakati; harga tanpa sumber diberi status belum dikonfirmasi'],
 ['Web izin pesan dan data','Pemilik digital','Operator layanan; evaluator menerima data tanpa kontak langsung'],
 ['Evaluasi dan penghentian biaya','Pemilik keuangan','Riset dan analitik menghitung tambahan terhadap kontrol'],
 ['Keluhan dan rujukan','Pemilik layanan','Operator mengarahkan keluhan; profesional memutuskan layanan klinis secara independen'],
 ],[5,4,7])
table(['Risiko material','Pencegahan dan respons','Pemilik'],[
 ['Manfaat tidak relevan atau tidak nyaman','Pertahankan Basic; evaluasi ekspektasi; hentikan promosi ulang bila tidak cocok','Merek/layanan'],
 ['Hanya voucher yang mendorong pembelian','Trial selektif; catat subsidi dan promo ritel; analisis pembelian tanpa subsidi ulang','Keuangan/riset'],
 ['Harga dan SKU salah','Foto resmi, gramasi dan cap waktu; audit; koreksi sebelum pesan berikutnya','Perdagangan'],
 ['Pesan mahal atau mengganggu','Izin eksplisit, kuota frekuensi, kanal web alternatif, opt out cepat; tinjau biaya per kategori','Digital'],
 ['Atribusi atau penghitungan ganda','Satu transaksi dihitung sekali; catat berbagi tabung dan produk sendiri yang tergantikan','Evaluator'],
 ['Jam kerja melampaui kapasitas','Ukur penanganan kasus dan verifikasi; tambah biaya staf atau batasi penerimaan','Operasi'],
 ['Klaim atau testimoni melampaui batas','Regulatori meninjau materi; pendidikan dan layanan profesional dipisahkan dari promosi','Regulatori'],
 ],[4.2,8.8,3])
p('Kontak dan izin pesan disimpan terpisah dari tabel analisis. Data minimum mencakup SKU, gramasi, harga bertanggal, kejadian pembelian dan status izin. Akses dibatasi menurut peran; retensi serta penghapusan ditetapkan sebelum rekrutmen. Bukti belum terkirim tidak otomatis dikodekan sebagai tidak membeli. Tidak ada akses ke akun keuangan keluarga atau pemindahan kontak survei ke materi publik.')

# Financial exhibits are generated from the same quarterly model used in the prose.
exec((ROOT/'build/finance_appendix.py').read_text())

doc.core_properties.title='Pepsodent Sesuai Saya Executive Summary dan Lampiran'
doc.core_properties.author='Tim Pepsodent E Fest'
doc.core_properties.subject='Strategi pengembalian pengguna Premium dan model investasi tiga tahun'
OUT.parent.mkdir(exist_ok=True)
doc.save(OUT)
print(OUT)
