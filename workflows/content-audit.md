# Workflow: Audit konten

**Tujuan:** Menilai konten yang sudah ada atau draf terhadap rubrik mutu dan kepatuhan.
**Pemakaian:** Dipakai oleh /content-audit.

| No | Agen | Aksi | Keluaran | Gerbang |
|---|---|---|---|---|
| 1 | fact-checker | Periksa klaim dan anakronisme | Tabel fakta | - |
| 2 | brand-editor | Periksa bahasa, nada, konsistensi nama | Catatan suntingan | - |
| 3 | copyright-policy-reviewer | Periksa hak aset dan kebijakan | Tabel hak | - |
| 4 | quality-controller | Nilai dengan rubrik dan klasifikasikan temuan | Laporan QC | - |

## Aturan
- Langkah berurutan kecuali agen yang independen (boleh paralel).
- Berhenti di setiap gerbang dan minta persetujuan eksplisit untuk gerbang itu saja.
- Temuan KRITIS dari QC mengembalikan alur ke langkah penyebabnya.
- Tidak ada aksi publikasi, penghapusan, pengeluaran dana, atau perubahan akun tanpa persetujuan Gerbang D.

## Selesai bila
- Semua keluaran tabel di atas ada dan temuan terbuka tercatat.
- Status gerbang tercatat di templates/approval-record.md.
