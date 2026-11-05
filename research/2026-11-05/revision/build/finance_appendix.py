F=json.loads((ROOT/'finance/finance.json').read_text());base=F['cases']['base'];s=base['summary'];q=base['quarterly'];ass=base['assumptions'];th=F['thresholds_zero_npv']
app('E1','Investasi diarahkan pada layanan ringan yang dapat digunakan ulang','core_finance')
p('Layanan memakai kanal yang ada selama tiga tahun dan percobaan melalui pembelian berbayar. Biaya awal menyiapkan web, materi, pengukuran dan pelatihan. Pekerjaan rutin serta penggunaan aset merek tetap mendapat alokasi biaya.')
table(['Parameter estimasi tim','Skenario dasar','Dasar keputusan'],[
 ['Unit dan jangkauan','285.000 unit baru disaring selama 12 kuartal','Unit pembelian independen; 10 → 60 titik kontak ekuivalen ×500 skrining baru/kuartal. Rencana kapasitas, bukan lalu lintas terukur atau mitra yang sudah disepakati.'],
 ['Kelayakan sasaran','40% dari yang disaring','Riwayat Premium/Basic cukup spesifik dan kebutuhan relevan; bukan hasil survei. Gerbang SKU terstruktur, bukti bila tersedia dan audit riwayat terbatas.'],
 ['Pembelian pertama','35% intervensi; 25% praktik biasa','Perbedaan 10 poin merupakan estimasi tim yang diuji; tidak diambil dari studi luar atau sampel 50.'],
 ['Kelanjutan kuartalan','70% intervensi; 60% praktik biasa','Kohort berlanjut secara geometris; tanpa reaktivasi atau nilai pelanggan terminal.'],
 ['Frekuensi','Satu ekuivalen 100 g per unit aktif per kuartal','Asumsi volume; aktual menggunakan gramasi. Tidak menetapkan jadwal habis atau pengingat 90 hari.'],
 ['Tambahan kontribusi portofolio','Rp6.000 per tambahan 100 g','Kontribusi Premium Rp8.500 dikurangi Basic setara gram Rp2.500. Jembatan seluruhnya estimasi tim.'],
 ['Modal kerja dan diskonto','Rp2.500/tambahan 100 g; 12% riil/tahun','Cadangan bersih piutang/persediaan/utang, bukan DSO perusahaan; tingkat imbal hasil merupakan kriteria tim.'],
 ],[4,4.3,7.7])
h('Kontribusi dihitung setelah penjualan Basic yang tergantikan',level=2)
table(['Jembatan kontribusi estimasi tim','Premium 100 g','Basic 190 g'],[
 ['Realisasi bersih produsen','Rp20.000','Rp12.000'],['Biaya produksi','Rp10.500','Rp6.750'],['Biaya dagang dan logistik normal','Rp1.000','Rp500'],['Kontribusi normal','Rp8.500','Rp4.750'],['Kontribusi per 100 g','Rp8.500','Rp2.500'],
 ],[8,4,4])
note('Semua nilai SKU adalah estimasi tim. Harga rak × margin kasus tidak dipakai sebagai realisasi produsen. Margin kotor konsolidasi FY2025 sebesar 46,9% (PT Unilever Indonesia Tbk, 2026) hanya pembanding kewajaran umum, bukan margin SKU. Penggantian Basic sudah dikurangkan sekali; perpindahan merek sendiri lain perlu ditaksir ulang.')

app('E2','Setiap kuartal menanggung biaya dan kontribusinya sendiri','core_finance')
note('Juta rupiah konstan 2026, kecuali kolom unit. Pembulatan tampilan dapat menyebabkan selisih kecil; perhitungan memakai angka penuh. T0 memuat pengeluaran awal Rp20 juta. Q1–Q4 adalah kuartal relatif sejak program dimulai.')
table(['Waktu','Skrining','Δ 100 g','Kontrib.','Biaya','Surplus','Δ MK','Kas','Kas total'],[
 [r['period'],f"{r['screened']:,.0f}".replace(',','.'),f"{r['incremental_paid_100g']:,.0f}".replace(',','.'),money(r['incremental_portfolio_contribution'],2),money(r['program_cost'],2),money(r['operating_surplus'],2),money(r['change_working_capital'],2),money(r['program_cash_flow'],2),money(r['cumulative_program_cash'],2)] for r in q
 ],[1.4,1.8,1.8,1.8,1.8,1.8,1.8,1.8,1.8])
table(['Ringkasan tahunan','Tahun 1','Tahun 2','Tahun 3'],[
 [label]+[money(a[key],2) for a in base['annual']] for label,key in [('Kontribusi tambahan','incremental_portfolio_contribution'),('Biaya program rutin','program_cost'),('Surplus operasi','operating_surplus'),('Tambahan modal kerja','change_working_capital'),('Kas operasi program','program_cash_flow'),('Kas kumulatif setelah T0','cumulative_program_cash')]
 ],[6.4,3.2,3.2,3.2])
h('Arus kas mempertahankan modal kerja yang masih terikat',level=2)
note(f"Tambahan {s['incremental_paid_100g']:,.0f} ekuivalen 100 g; kontribusi Rp{money(s['contribution_before_program'],2)} juta; biaya awal dan rutin Rp{money(s['total_program_cost'],2)} juta. Surplus Rp{money(s['operating_surplus_after_launch'],2)} juta dikurangi modal kerja akhir Rp{money(s['ending_working_capital'],2)} juta menyisakan kas Rp{money(s['cumulative_cash_after_launch'],2)} juta. Satuan kontribusi, biaya, surplus, Δ MK, kas dan kumulatif dalam juta rupiah. Δ MK ialah perubahan modal kerja; kumulatif sudah mengurangi T0. Proksi kas sebelum pajak; tanpa nilai terminal atau pelepasan modal kerja pada Q12.".replace('41,527','41.527'))


app('E3','Pengembalian bergantung pada volume tambahan dan disiplin biaya','core_finance')
fig('cash.png','Gambar E1  Kas kumulatif mengungkap kebutuhan pendanaan dan risiko tiga skenario')
table(['Skenario','Surplus setelah biaya awal','Kas setelah modal kerja','NPV riil 12%','Pengembalian kas'],[
 [label,money(F['cases'][key]['summary']['operating_surplus_after_launch'],2),money(F['cases'][key]['summary']['cumulative_cash_after_launch'],2),money(F['cases'][key]['summary']['npv'],2),('Tidak tercapai' if F['cases'][key]['summary']['payback_quarter'] is None else f"T{(F['cases'][key]['summary']['payback_quarter']-1)//4+1}Q{(F['cases'][key]['summary']['payback_quarter']-1)%4+1}")] for key,label in [('downside','Bawah'),('base','Dasar'),('upside','Atas')]
 ],[2.2,3.8,3.8,3.1,3.1])
note('Satuan juta rupiah. Skenario bawah: jangkauan 75% dasar, pembelian awal 30%, kelanjutan 65%, kontribusi Rp4.500, skrining Rp400, layanan Rp450 dan pesan Rp400 per kejadian. Skenario atas: jangkauan 125%, pembelian awal 40%, kelanjutan 75%, kontribusi Rp7.500, skrining Rp180. Kontrol tetap 25% awal dan 60% kelanjutan. Semua merupakan estimasi tim, bukan peluang statistik.')
fig('sensitivity.png','Gambar E2  Kenaikan biaya per skrining cepat menghabiskan ruang pengembalian')
n0=lambda x:f'{x:,.0f}'.replace(',','.')
n2=lambda x:f'{x:.2f}'.replace('.',',')
note(f"Dengan input lain tetap, NPV nol pada biaya skrining sekitar Rp{n0(th['max_screen_cost_idr'])}, kontribusi Rp{n0(th['min_contribution_per_incremental_100g_idr'])} per tambahan 100 g, konversi awal {n2(th['min_first_paid_treatment']*100)}%, atau kelanjutan {n2(th['min_quarterly_continuation_treatment']*100)}%. Ambang dihitung satu per satu; tidak menjamin kelayakan bila beberapa input memburuk bersamaan.")


app('E4','Asumsi terbuka menentukan batas keputusan investasi','core_finance')
table(['Alokasi estimasi tim','Nilai','Dasar dan batas pembanding'],[
 ['Biaya awal','Rp20 juta pada T0','CMS Rp5 juta; katalog/izin/data Rp3 juta; pendidikan dan tinjauan profesional Rp3 juta; QR/pelatihan Rp3 juta; pembanding/riset/QA Rp6 juta.'],
 ['Skrining dan akses kanal','Rp200/unit baru','Rp100 materi/QR +Rp100 alokasi kanal milik merek. Bukan CAC berbayar yang terukur; akses murah merupakan syarat utama.'],
 ['Pemeriksaan riwayat','Rp40/unit layak','Gerbang SKU otomatis dan audit: 2% ×2 menit +1% pengecualian ×1 menit =0,05 menit/unit; sekitar Rp33,7 tenaga +Rp6,3 pemrosesan.'],
 ['Layanan dan bukti','Rp350/kejadian berbayar intervensi','5% audit struk ×2 menit +10% dukungan ×3 menit =0,4 menit/kejadian; sekitar Rp270 tenaga +Rp80 pemrosesan.'],
 ['Pesan','Rp300/kejadian berbayar intervensi','20% opt in ×2 pesan ×Rp750 cadangan menyeluruh. Rp750 adalah estimasi tim; tarif Twilio US$0,005/pesan ditambah biaya kategori Meta hanya jangkar struktur biaya.'],
 ['Operasi tetap','Rp6 juta/kuartal','Koordinasi Rp4,2 juta; konten/profesional Rp0,6 juta; hosting/keamanan Rp0,6 juta; analitik Rp0,6 juta.'],
 ['Tenaga kerja','Rp7 juta/bulan terbebani','Estimasi di atas jangkar UMP Jakarta 2026 Rp5.729.876. Asumsi 173 jam/bulan, sekitar Rp40.500/jam. Bukan penawaran tenaga kerja.'],
 ['Infrastruktur','Dalam Rp0,6 juta/kuartal','Cloudflare Workers minimum berbayar US$5/bulan hanya jangkar biaya masuk; integrasi, keamanan dan SLA tetap harus dicakup penawaran aktual.'],
 ],[3.6,4,8.4])
note('Sumber jangkar: Twilio (n.d.); Pemerintah Provinsi DKI Jakarta (2025); Cloudflare (n.d.). Tarif dan upah tidak membuktikan harga pengadaan program atau kinerja komersial. Seluruh alokasi rupiah adalah estimasi tim.')
app('E5','Rumus dan kapasitas memperjelas batas pendanaan','core_finance')
h('Kapasitas dan pembanding mempunyai biaya yang dapat diperiksa',level=2)
p('Pada puncak dasar sekitar 13.435 kejadian berbayar intervensi per kuartal, penanganan variabel memerlukan sekitar 90 jam; koordinasi tetap menambah sekitar 104 jam. Audit riwayat pada 12.000 unit layak menambah sekitar 10 jam. Alokasi tenaga variabel dibayar terpisah dari 0,2 ekuivalen staf koordinasi. Perubahan beban keluhan, audit dan tarif memicu penghitungan ulang.')
p('Cadangan riset awal Rp6 juta mencakup satu kohort pembanding pembelajaran yang diusulkan 1.000 unit: rekrutmen 2.500 skrining Rp0,5 juta, hingga 1.000 catatan bukti Rp0,35 juta, 100 jam riset Rp4 juta, dan protokol/QA Rp1,15 juta. Pengukuran rutin intervensi sudah ada dalam biaya kejadian. Trajektori pembanding 12 kuartal adalah normalisasi model, bukan tambahan 285.000 peserta kontrol. Daya uji, klaster, insentif dan akses riwayat menentukan kebutuhan riset aktual sebelum anggaran dilepas.')
p(f"Model 180 hari sebelumnya tetap menunjukkan kerugian. Versi ini mengubah rancangan layanan, biaya awal, pembelian percobaan berbayar, kohort berulang dan horizon secara eksplisit. Pendanaan puncak Rp{money(s['peak_funding_need'],2)} juta berbeda dari total biaya tiga tahun. Anggaran dilepas bertahap; skenario dasar tidak menjustifikasi komitmen tiga tahun sekaligus.")
note('Sumber: estimasi tim. Tarif pajak, pendanaan, depresiasi dan WACC perusahaan tidak diasumsikan telah diketahui. Angka proyeksi perlu diperbarui bila data margin, biaya kanal, audit riwayat, konversi atau kelanjutan aktual mengubah batas investasi.')

h('Kohort berulang direkonsiliasi dengan pembanding',level=2)
table(['Perhitungan per kuartal','Rumus dan satuan'],[
 ['Unit layak','Skrining baru × tingkat kelayakan 40%'],
 ['Aktif intervensi','Unit layak ×35% + aktif intervensi kuartal lalu ×70%'],
 ['Aktif praktik biasa','Unit layak ×25% + aktif praktik biasa kuartal lalu ×60%'],
 ['Tambahan volume','(Aktif intervensi − aktif praktik biasa) ×1 ekuivalen 100 g'],
 ['Kontribusi tambahan','Tambahan volume ×Rp6.000'],
 ['Biaya rutin','Skrining ×Rp200 + unit layak ×Rp40 + kejadian berbayar intervensi ×(Rp350 +Rp300) +Rp6 juta'],
 ['Kas program','Kontribusi − biaya rutin − perubahan modal kerja; modal kerja = tambahan volume ×Rp2.500'],
 ['NPV','−Rp20 juta + jumlah kas kuartal yang didiskontokan pada (1 +12%) pangkat kuartal/4'],
 ],[4.3,11.7])
note('Seluruh persentase dan koefisien merupakan estimasi tim. Satu kohort dihitung hanya sejak masuk sampai akhir jendela; tidak ada penjumlahan dampak tiap pilar. Satuan orang/rumah tangga berbagi tabung dideduplikasi; frekuensi aktual memakai gramasi. Data aktual menggantikan asumsi sebelum keputusan pendanaan berikutnya.')
