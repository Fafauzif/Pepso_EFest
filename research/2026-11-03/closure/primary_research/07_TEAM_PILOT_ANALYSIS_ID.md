# Kerja tim, pilot, dan analisis

## Tiga peran yang bergantian

| Peran | Saat wawancara | Sesudah wawancara |
|---|---|---|
| A: pewawancara | Menjaga alur, netral, satu pertanyaan setiap kali, minta klarifikasi | Menulis memo singkat tentang dugaan awal dan hal yang mengejutkan |
| B: pencatat | Menangkap timeline, kutipan/timestamp, peran rumah, unknown | Membersihkan catatan tanpa mengubah arti; menandai kutipan verbatim versus parafrasa |
| C: reviewer/logistik | Menjaga izin, versi instrumen, dan cakupan rekrutmen; bila hadir jangan ikut menumpuk pertanyaan | Memeriksa klaim terhadap sumber, mencari penjelasan alternatif, memperbarui gap |

Dua orang cukup untuk satu wawancara jika orang ketiga mengurus jadwal dan review berikutnya. Kehadiran tiga peneliti bisa membuat peserta merasa diuji; jelaskan peran dan kurangi jumlah yang hadir bila lebih nyaman. Rotasi peran agar satu orang tidak menjadi satu-satunya penafsir semua data.

## Dua pilot sebelum gelombang awal

Pilih dua peserta dengan situasi berbeda bila memungkinkan: misalnya satu pembeli sendiri dan satu pengguna yang dibelikan orang lain. Tujuan pilot adalah menguji pertanyaan dan pencatatan, bukan mencari dua kutipan yang mendukung ide.

Setelah masing-masing pilot, cek:

1. Apakah peserta dapat menceritakan satu event nyata tanpa tim menambahkan urutannya?
2. Apakah nama varian/ukuran cukup jelas? Apa yang tidak bisa diklasifikasikan?
3. Apakah payer/chooser/user terpisah? Apakah ada harga yang ditebak karena pertanyaan tim?
4. Apakah “beli lagi”, “pakai terus”, “ganti”, dan “cocok” dipahami sama?
5. Pertanyaan mana terasa mengarahkan atau memunculkan jawaban yang tidak diketahui peserta?
6. Apakah wawancara selesai pada durasi yang dijanjikan? Bagian apa perlu dipindah/dihapus?
7. Apakah proses izin, note taking, bukti opsional, dan de-identifikasi berjalan?

Catat perubahan di `pilot_changes.csv`: pertanyaan lama, masalah yang diamati, revisi, alasan, dan versi berlaku. Jangan menimpa catatan pilot dengan versi pertanyaan baru. Simpan keputusan apakah pilot masuk analisis substantif dan alasannya.

## Siklus analisis setelah tiap 3–4 wawancara

### Langkah 1: ringkas tiap kasus, belum hitung tema

Tulis satu halaman per participant_id: konteks yang relevan, timeline, siapa mengendalikan keputusan, manfaat yang diharapkan/dirasakan, kejadian penggantian, penjelasan peserta, penjelasan alternatif, dan hal yang belum diketahui. Pisahkan produk saat ini dari riwayat yang berlaku pada periode kasus.

### Langkah 2: kode bukti, bukan orangnya

Satu kutipan dapat memiliki beberapa kode; satu peserta bisa menunjukkan mekanisme berbeda pada event berbeda. Gunakan `evidence_coding.csv` untuk menghubungkan kode dengan event_id dan locator. Tambahkan kode baru bila data tidak cocok dengan dugaan tim. Jangan memaksa semua jawaban menjadi masalah harga, household, atau edukasi.

Kode awal yang dapat direvisi:

- `household_authority`, `payer_transition`, `shared_tube`, `personal_specialist_tube`.
- `cash_outlay`, `unit_value`, `promo_trial`, `promo_repeat_claim`, `normal_price_repeat_unknown`.
- `variant_unavailable_reported`, `alternative_available`, `temporary_substitution`, `choice_uncertainty`.
- `benefit_expected`, `benefit_noticed`, `benefit_not_noticed`, `need_resolved_reported`, `basic_sufficient`.
- `taste_aftertaste`, `freshness_clean_feeling`, `foam`, `dryness_discomfort`.
- `completed_repurchase`, `continued_use_only`, `intended_repurchase`, `parallel_use`, `switch_sequence_reported`.
- `counterexample`, `ambiguous`, `missing_information`, `third_party_account`.

Kata “murah” sendiri belum menjelaskan cash constraint; “diskon” sendiri belum membuktikan promo trial; “cocok” sendiri belum membuktikan manfaat klinis. Kutipan harus dibaca bersama event.

### Langkah 3: reviewer kedua memeriksa subset

Reviewer kedua membaca sumber untuk beberapa bukti dari tiap kelompok, termasuk kasus yang mendukung dan melemahkan hipotesis. Catat disagreement di tabel sebelum diskusi. Pertahankan kode asli, revisi, serta alasan. Kesepakatan antar anggota tim adalah pemeriksaan konsistensi, bukan jaminan bahwa cerita peserta benar atau sampel mewakili populasi.

### Langkah 4: bandingkan kontras yang informatif

Bandingkan, misalnya, dua orang dengan kebutuhan serupa tetapi payer berbeda; dua orang yang sama-sama mendapat diskon tetapi hanya satu membeli ulang; pengguna yang stok varian lamanya tersedia versus yang tidak; retained Premium yang sudah merasa membaik versus switcher yang juga merasa membaik. Jangan menganggap mereka “sama persis” di faktor lain.

### Langkah 5: perbarui hipotesis dan gap

Gunakan `hypothesis_updates.csv` dan decision table. Untuk setiap hipotesis tulis: prediksi sebelum membaca kasus, bukti baru, bukti yang menentang, penjelasan rival, keyakinan tentang mekanisme, keyakinan penerapan pada target, pertanyaan berikutnya. Hindari skor numerik yang tampak presisi tanpa dasar.

## Kapan menambah atau berhenti

Tambahkan peserta untuk **gap tertentu**, misalnya belum ada pembeli mandiri, switcher yang benar-benar terkonfirmasi, atau retained Premium. Jangan memperpanjang hanya supaya jumlah kutipan besar. Berhenti gelombang awal ketika tim dapat menjelaskan apa yang didukung, apa yang dibantah, kelompok mana yang belum terjangkau, dan bukti berikutnya yang paling bernilai. Ini keputusan praktis tentang gelombang riset, bukan klaim saturasi universal.

Jika switcher target tidak berhasil direkrut, tulis itu sebagai hasil rekrutmen. Analisis kelompok pembanding tetap berguna, tetapi tidak boleh diberi judul “penyebab Premium ke Basic pada target”. Jika jawaban bertentangan, pertahankan heterogenitas daripada memilih versi yang paling cocok dengan solusi.

## Cara melaporkan

- Gunakan n peserta dan n event dengan label berbeda. Jika 3 dari 8 peserta dalam sampel ini menyebut sesuatu, tulis sebagai deskripsi sampel kecil, bukan “37,5% konsumen Indonesia”.
- Kutipan harus memiliki participant_id, event_id bila relevan, jenis sumber, dan status izin; laporan eksternal memakai kode anonim.
- Laporkan cara rekrutmen, periode, kota umum, komposisi konteks, panduan/versi, keterbatasan recall, serta missing data.
- Sebut hasil survei convenience dan tugas SKU sebagai eksploratif bila desainnya demikian.
- Tulis arah strategi sebagai “jika mekanisme ini terbukti pada situasi X, uji Y dengan ukuran keberhasilan Z”, bukan janji uplift.
