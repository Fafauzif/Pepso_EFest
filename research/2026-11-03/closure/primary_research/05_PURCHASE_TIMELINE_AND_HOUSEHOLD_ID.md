# Rekonstruksi pembelian dan keputusan rumah tangga

Gunakan `templates/purchase_events.csv` bersama catatan wawancara. Satu baris = **satu kejadian pembelian/penggantian**, bukan satu orang atau satu pendapat. Pembelian dua tabung sekaligus tetap satu kejadian dengan jumlah tabung yang dicatat. Tiga kejadian dari satu peserta bukan tiga responden independen.

## Urutan pengisian

1. Mulai dari kejadian terbaru yang benar-benar terjadi. Tulis nama produk sebagaimana diucapkan peserta, jangan langsung memperbaiki ejaan.
2. Rekam merek/varian/ukuran/jumlah secara terpisah bila diketahui. Kemudian buat versi normalisasi analis, dengan sumber klasifikasi tier dan status belum pasti bila perlu.
3. Tanyakan kejadian sebelumnya. Beri event_id stabil, lalu `sequence_order` untuk urutan kronologis yang dapat diperbaiki tanpa mengganti bukti asli.
4. Simpan tanggal perkiraan sebagai rentang/label mentah dan tingkat ketepatan; tanggal tidak diketahui tidak menjadi tanggal wawancara.
5. Kaitkan penjelasan dengan momen: sebelum membeli, di tempat belanja, setelah menggunakan, atau saat penggantian berikutnya.

## Pertanyaan per kejadian

| Bagian | Pertanyaan netral | Hal yang sering keliru |
|---|---|---|
| Pemicu | “Kenapa saat itu perlu membeli/mengganti?” | Promo dapat memajukan stok tanpa menandakan kebutuhan baru |
| Pengetahuan | “Ini Anda lihat/lakukan sendiri atau diberi tahu?” | Pengguna tidak otomatis tahu harga/pilihan yang dibayar orang tua |
| Peran | “Siapa menyadari habis, memilih, membeli, membayar, memakai?” | Payer bukan selalu chooser; orang yang checkout belum tentu sumber uang |
| Produk | “Nama varian, gram, jumlah tabung, dan masih ada produk lain?” | Bundle berbeda dari tabung satuan; pemakaian paralel bukan switching penuh |
| Outlet | “Di mana membeli dan apa yang tersedia waktu itu?” | Tidak melihat produk tidak sama dengan memverifikasi stok kosong |
| Harga | “Berapa dibayar untuk pembelian ini; perkiraan atau ada catatan?” | Harga coret/online sekarang bukan harga transaksi sebelumnya |
| Alternatif | “Apa yang benar-benar dilihat/dipertimbangkan?” | Jangan mengisi alternatif dari daftar merek yang diberikan tim |
| Hasil | “Setelah dipakai, apa yang terjadi?” | Review sebelum pakai bukan outcome manfaat |
| Berikutnya | “Sudah ada penggantian berikutnya? Memilih apa?” | Niat beli bukan observed repeat |

## Harga dan biaya penggunaan

Catat harga produk yang dibayar, potongan, ongkir, bundle, hadiah, dan alokasi yang tidak diketahui. Jika total struk mencampur barang lain, jangan menganggap seluruhnya harga pasta gigi. Jangan memaksa alokasi voucher bersama bila peserta tidak mengetahui rinciannya.

Harga per 100 g boleh dihitung hanya bila harga produk dan total gram jelas: `paid_product_price_idr / total_grams * 100`. Untuk multipack, total gram = jumlah tabung × gram per tabung bila isinya sama. Jika hadiah, ukuran campuran, cairan ml, atau harga belum jelas, beri flag; jangan menganggap ml sama dengan g. Harga per hari memerlukan asumsi pemakaian yang dinyatakan, bukan fakta transaksi. Jangan meminta peserta menakar pasta saat menyikat untuk membenarkan hitungan.

## Modul household bila relevan

- “Kalau Anda dan anggota rumah menginginkan produk berbeda, bagaimana biasanya diputuskan?”
- “Ada satu tabung untuk semua atau orang tertentu punya tabung sendiri? Apa alasan pembagiannya?”
- “Bagaimana Anda menyampaikan ingin produk tertentu? Apa yang terjadi pada permintaan terakhir?”
- “Pernah pola pembelian berubah ketika pindah kos/rumah, mulai kerja, atau mulai membayar sendiri? Ceritakan pembelian yang menunjukkan perubahan itu.”
- “Siapa yang memiliki informasi harga dan siapa yang paling merasakan manfaat produk?”
- “Kalau anggota rumah lain tidak punya kebutuhan yang sama, apa yang terjadi pada tabung bersama?”

Jika ingin mewawancarai payer/co-user, minta izin peserta **dan** persetujuan informan itu sendiri. Jangan menghubungi orang tua/teman serumah otomatis dari cerita peserta. Wawancara terpisah lebih baik untuk mendapat versi masing-masing; perbedaan cerita dicatat, bukan dipaksa disepakati. Wawancara bersama dapat memberi konteks negosiasi tetapi juga menekan perbedaan pendapat; beri label metode.

## Pelabelan jenis tindakan

- `completed_repurchase`: peserta menceritakan pembelian berikutnya yang sudah terjadi; sumber/self-report tetap dicatat.
- `continued_use_only`: masih menggunakan, tetapi belum ada pembelian baru yang diketahui.
- `intended_repurchase`: menyatakan akan membeli, belum terjadi.
- `temporary_substitution`: menggunakan pengganti sementara/kehabisan, belum menunjukkan pergantian menetap.
- `parallel_use`: dua atau lebih produk dipakai bersamaan sesuai situasi.
- `switch_sequence_reported`: urutan produk berbeda dilaporkan; arah/tier diverifikasi terpisah.
- `unknown`: tidak cukup informasi. Jangan mengisi kategori yang paling cocok dengan hipotesis.

Foto/struk dapat membantu mengingat produk dan harga, bukan otomatis menjelaskan motivasi. Simpan referensi bukti yang sudah direduksi identitasnya, bukan nomor pesanan atau alamat.
