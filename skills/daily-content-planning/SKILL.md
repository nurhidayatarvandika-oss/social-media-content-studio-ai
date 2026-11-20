---
name: daily-content-planning
description: "Menghasilkan slate topik, memilih satu, dan menyusun kalender produksi yang realistis."
agents: [content-manager, content-strategist, trend-researcher, project-manager]
---

# Skill: Perencanaan harian

Menghasilkan slate topik, memilih satu, dan menyusun kalender produksi yang realistis.
## Kapan dipakai
Saat owner meminta ide, konten harian, atau kalender.

## Prosedur
1. Baca `config/studio.yaml` (niche, audiens, kadensi) dan backlog.
2. Kumpulkan 5-8 kandidat dari: kalender peringatan sejarah 30-60 hari ke depan, pertanyaan audiens, celah pesaing, tema evergreen.
3. Beri skor 1-5 pada: Relevansi audiens, Ketersediaan sumber, Kebaruan sudut, Kelayakan produksi (kreator tunggal), Risiko (5 = aman). Total maksimum 25.
4. Pilih kandidat dengan skor tertinggi; jika skor sama, pilih yang sumbernya paling kuat.
5. Beri kandidat peringkat 2 dan 3 sebagai cadangan.
6. Susun kalender 7 hari dengan kadensi default config (`cadence`), lengkap dengan gerbang persetujuan sebagai tonggak.

## Format slate
| # | Topik | Sudut | Relev | Sumber | Baru | Layak | Risiko | Total |
|---|---|---|---|---|---|---|---|---|

## Aturan
- Skor adalah penilaian terstruktur, bukan prediksi performa.
- Setiap topik dari peringatan tanggal harus diverifikasi tanggalnya.
- Hentikan di Gerbang A untuk persetujuan topik.
