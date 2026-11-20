---
name: quality-control
description: "Rubrik penilaian tetap dan klasifikasi temuan untuk menentukan lolos, revisi, atau tolak."
agents: [quality-controller, fact-checker, brand-editor, copyright-policy-reviewer]
---

# Skill: Kontrol mutu

Rubrik penilaian tetap dan klasifikasi temuan untuk menentukan lolos, revisi, atau tolak.
## Rubrik (skor 1-5 per dimensi)
| Dimensi | Yang dinilai |
|---|---|
| Akurasi | Klaim terverifikasi, tanggal dan nama benar, tidak ada anakronisme |
| Kejujuran | Judul, thumbnail, hook sesuai isi; dramatisasi dan rekonstruksi berlabel |
| Orisinalitas | Sudut dan penulisan sendiri; tidak menjiplak |
| Kejelasan | Mudah dipahami penonton umum; istilah dijelaskan |
| Kepatuhan | Hak aset, musik, pengungkapan AI, kebijakan platform |
| Kesiapan produksi | Aset, durasi, subtitle, spesifikasi ekspor lengkap |

## Keputusan
- **LOLOS:** semua dimensi minimal 4 dan tidak ada temuan KRITIS.
- **LOLOS DENGAN REVISI:** semua dimensi minimal 3, tidak ada KRITIS, dan semua MAYOR punya rencana perbaikan.
- **DITOLAK:** ada dimensi di bawah 3 atau ada temuan KRITIS terbuka.

## Klasifikasi temuan
- KRITIS: fakta salah yang material, aset tanpa hak, klaim menyesatkan, konten sensitif tanpa review.
- MAYOR: klaim tanpa sumber, nama tidak konsisten, label AI/rekonstruksi hilang.
- MINOR: gaya bahasa, ritme, detail visual.

## Prosedur
1. Kumpulkan laporan fact-checker, brand-editor, copyright-policy-reviewer.
2. Isi `templates/qc-report.md`.
3. Lakukan cek silang: judul-thumbnail-isi, durasi, nama, label.
4. Putuskan dan serahkan ke Studio Director. Ulangi setelah perbaikan; jangan menurunkan ambang agar lolos.
