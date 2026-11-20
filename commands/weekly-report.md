---
description: "Susun laporan mingguan studio dari data yang diberikan owner."
argument-hint: "<tempel data analitik atau analytics-log.csv>"
workflow: analytics-review
skills: [analytics-learning]
---

# /weekly-report

Susun laporan mingguan studio dari data yang diberikan owner.

## Masukan
- Argumen: `$ARGUMENTS`
- Data nyata dari owner. Tanpa data, laporan hanya berisi rencana pengumpulan data.
- Selalu baca `config/studio.yaml` (niche, audiens, gaya, bahasa) dan `STUDIO_DIRECTOR.md` terlebih dahulu.
- Nama brand belum ditentukan: pakai `[NAMA BRAND]`, jangan mengarang.

## Prosedur
Jalankan `workflows/analytics-review.md` langkah demi langkah. Agen yang terlibat: analytics-analyst, experimentation-strategist, monetization-strategist, studio-director.
Terapkan skill: `skills/analytics-learning`.

**Lingkup:** Tanpa data owner, hanya keluarkan rencana pengumpulan data; jangan mengisi metrik.

**Lingkup:** Tanpa data owner, hanya keluarkan rencana pengumpulan data; jangan mengisi metrik.

## Keluaran
- Ringkasan produksi, analisis, eksperimen, 3 prioritas minggu depan.
- Struktur respons: 1 Brief dan asumsi, 2 Strategi, 3 Deliverables, 4 Riset dan sumber, 5 Checklist produksi, 6 Risiko dan hasil QC, 7 Persetujuan owner yang dibutuhkan.

## Gerbang
- Berhenti di tiap gerbang pada workflow dan minta persetujuan eksplisit. Jangan lanjut ke gerbang berikutnya tanpa persetujuan.
- Jangan mengklaim sesuatu sudah diunggah, dijadwalkan, atau dianalisis kecuali alat terhubung mengonfirmasi.
