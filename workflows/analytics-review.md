# Workflow: Tinjauan analitik

**Tujuan:** Mengubah data performa nyata dari owner menjadi pelajaran dan eksperimen.
**Pemakaian:** Dipakai oleh /weekly-report.

| No | Agen | Aksi | Keluaran | Gerbang |
|---|---|---|---|---|
| 1 | analytics-analyst | Catat data di analytics-log.csv dan bandingkan antar konten | Laporan analitik | - |
| 2 | experimentation-strategist | Rumuskan hipotesis dan eksperimen satu variabel | Log eksperimen | - |
| 3 | monetization-strategist | Cek kemajuan terhadap syarat monetisasi (terverifikasi dan bertanggal) | Status monetisasi | - |
| 4 | studio-director | Rekomendasi 3 tindakan prioritas untuk minggu depan | Rencana minggu depan | - |

## Aturan
- Langkah berurutan kecuali agen yang independen (boleh paralel).
- Berhenti di setiap gerbang dan minta persetujuan eksplisit untuk gerbang itu saja.
- Temuan KRITIS dari QC mengembalikan alur ke langkah penyebabnya.
- Tidak ada aksi publikasi, penghapusan, pengeluaran dana, atau perubahan akun tanpa persetujuan Gerbang D.

## Selesai bila
- Semua keluaran tabel di atas ada dan temuan terbuka tercatat.
- Status gerbang tercatat di templates/approval-record.md.
