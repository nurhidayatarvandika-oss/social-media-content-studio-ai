# Pekerjaan tertunda dan integrasi yang dibutuhkan

## Belum berfungsi (butuh tindakan owner atau integrasi)
| Item | Status | Yang dibutuhkan |
|---|---|---|
| Unggah dan penjadwalan otomatis YouTube | Belum ada | API resmi YouTube Data, OAuth dengan izin minimum, uji dengan draf |
| Unggah dan penjadwalan Facebook | Belum ada | Meta Graph API/Business Suite dan peninjauan aplikasi |
| Unggah TikTok | Belum ada | TikTok Content Posting API dan persetujuan aplikasi |
| Analitik otomatis | Belum ada | Konektor resmi per platform; sementara input manual ke `templates/analytics-log.csv` |
| Eksekusi agen persisten | Bergantung host | Claude Code atau platform agen yang mendukung agen Markdown |
| Pembuatan visual dan suara | Di luar repositori | Alat pembuat gambar/video/suara pilihan owner |

## Keputusan owner yang masih diperlukan
- Nama brand/channel (sengaja belum diisi).
- Data audiens nyata untuk mengganti persona berstatus ASUMSI.
- Kadensi final (default `long_form_per_week: 1`, `short_form_per_week: 4` adalah asumsi).

## Saran perbaikan lanjutan
- Isi `examples/` dengan satu paket sejarah yang diverifikasi penuh setelah Gerbang A-D pertama selesai.
- Tambah template storyboard dan shot list berformat CSV jika editor membutuhkannya.
- Tambah pemeriksaan otomatis tambahan di `tools/validate.py` seiring pertumbuhan repositori.
