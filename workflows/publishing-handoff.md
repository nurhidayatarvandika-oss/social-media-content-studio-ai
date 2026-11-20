# Workflow: Handoff publikasi

**Tujuan:** Menyiapkan serah terima ke owner untuk unggah manual atau lewat konektor resmi.
**Pemakaian:** Hanya berjalan setelah gerbang A, B, dan C disetujui.

| No | Agen | Aksi | Keluaran | Gerbang |
|---|---|---|---|---|
| 1 | quality-controller | Pastikan laporan QC berstatus LOLOS dan tidak ada temuan KRITIS terbuka | Konfirmasi QC | - |
| 2 | project-manager | Susun jadwal final per platform (tanggal, jam, zona waktu Asia/Jakarta) | Jadwal usulan | - |
| 3 | youtube-metadata-specialist, facebook-community-manager, tiktok-search-specialist | Siapkan teks siap salin per platform | Paket siap unggah | - |
| 4 | studio-director | Isi templates/publishing-checklist.md dan templates/approval-record.md; minta persetujuan aksi persis (akun, platform, tanggal, jam) | Checklist dan rekam persetujuan | Gerbang D |

## Aturan
- Langkah berurutan kecuali agen yang independen (boleh paralel).
- Berhenti di setiap gerbang dan minta persetujuan eksplisit untuk gerbang itu saja.
- Temuan KRITIS dari QC mengembalikan alur ke langkah penyebabnya.
- Tidak ada aksi publikasi, penghapusan, pengeluaran dana, atau perubahan akun tanpa persetujuan Gerbang D.

## Selesai bila
- Semua keluaran tabel di atas ada dan temuan terbuka tercatat.
- Status gerbang tercatat di templates/approval-record.md.
