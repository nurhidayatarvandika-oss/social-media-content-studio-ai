---
description: "Tampilkan dan perbarui papan produksi dan kalender."
argument-hint: "[ID konten] [status baru]"
workflow: campaign-planning
skills: [daily-content-planning]
---

# /production-board

Tampilkan dan perbarui papan produksi dan kalender.

## Masukan
- Argumen: `$ARGUMENTS`
- Daftar konten yang sedang berjalan (tempel dari owner).
- Selalu baca `config/studio.yaml` (niche, audiens, gaya, bahasa) dan `STUDIO_DIRECTOR.md` terlebih dahulu.
- Nama brand belum ditentukan: pakai `[NAMA BRAND]`, jangan mengarang.

## Prosedur
Jalankan `workflows/campaign-planning.md` langkah demi langkah. Agen yang terlibat: content-strategist, trend-researcher, audience-researcher, competitor-analyst, youtube-strategist, facebook-strategist, tiktok-strategist, project-manager, analytics-analyst, experimentation-strategist.
Terapkan skill: `skills/daily-content-planning`.

**Lingkup:** Jalankan hanya langkah penjadwalan (project-manager); hasilnya berupa papan produksi, bukan kampanye baru.

**Lingkup:** Jalankan hanya langkah penjadwalan (project-manager); hasilnya berupa papan produksi, bukan kampanye baru.

## Keluaran
- Papan produksi, blocker, jadwal mundur.
- Struktur respons: 1 Brief dan asumsi, 2 Strategi, 3 Deliverables, 4 Riset dan sumber, 5 Checklist produksi, 6 Risiko dan hasil QC, 7 Persetujuan owner yang dibutuhkan.

## Gerbang
- Berhenti di tiap gerbang pada workflow dan minta persetujuan eksplisit. Jangan lanjut ke gerbang berikutnya tanpa persetujuan.
- Jangan mengklaim sesuatu sudah diunggah, dijadwalkan, atau dianalisis kecuali alat terhubung mengonfirmasi.
