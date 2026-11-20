---
description: "Audit draf atau konten terbit terhadap rubrik mutu dan kepatuhan."
argument-hint: "<tempel naskah/tautan/deskripsi>"
workflow: content-audit
skills: [quality-control, content-research]
---

# /content-audit

Audit draf atau konten terbit terhadap rubrik mutu dan kepatuhan.

## Masukan
- Argumen: `$ARGUMENTS`
- Konten yang diaudit.
- Selalu baca `config/studio.yaml` (niche, audiens, gaya, bahasa) dan `STUDIO_DIRECTOR.md` terlebih dahulu.
- Nama brand belum ditentukan: pakai `[NAMA BRAND]`, jangan mengarang.

## Prosedur
Jalankan `workflows/content-audit.md` langkah demi langkah. Agen yang terlibat: fact-checker, brand-editor, copyright-policy-reviewer, quality-controller.
Terapkan skill: `skills/quality-control`, `skills/content-research`.

**Lingkup:** Jalankan keempat langkah pada konten yang diberikan; jangan menulis ulang kecuali diminta.

**Lingkup:** Jalankan keempat langkah pada konten yang diberikan; jangan menulis ulang kecuali diminta.

## Keluaran
- Laporan QC dengan temuan berklasifikasi dan keputusan.
- Struktur respons: 1 Brief dan asumsi, 2 Strategi, 3 Deliverables, 4 Riset dan sumber, 5 Checklist produksi, 6 Risiko dan hasil QC, 7 Persetujuan owner yang dibutuhkan.

## Gerbang
- Berhenti di tiap gerbang pada workflow dan minta persetujuan eksplisit. Jangan lanjut ke gerbang berikutnya tanpa persetujuan.
- Jangan mengklaim sesuatu sudah diunggah, dijadwalkan, atau dianalisis kecuali alat terhubung mengonfirmasi.
