# Panduan penggunaan (untuk pemula)

## Gambaran singkat
Studio ini adalah tim agen AI dengan satu pemimpin, **Studio Director**. Anda adalah **owner**: Anda memberi tujuan dan menyetujui. AI meriset, menulis, menyiapkan paket konten untuk YouTube, Facebook, dan TikTok, lalu memeriksa mutunya. **Tidak ada yang dipublikasikan tanpa persetujuan Anda.**

## Tiga cara memakai
1. **Di chat Claude.ai:** tempel isi `STUDIO_DIRECTOR.md` sebagai pedoman, lalu tempel isi command yang ingin dipakai (misalnya `commands/history-documentary.md`) beserta topik Anda. Cara ini tidak memasang repositori otomatis.
2. **Di Claude Code:** salin `agents/`, `commands/`, dan `skills/` ke folder yang didukung versi Anda (umumnya `.claude/agents`, `.claude/commands`, `.claude/skills`; cek dokumentasi terbaru). Lalu ketik, misalnya, `/history-documentary Perjanjian Giyanti`.
3. **Platform agen lain:** impor file sesuai format platform itu.

## Langkah pertama (sekitar 10 menit)
1. Buka `config/studio.yaml`. Isi `brand.name` bila sudah punya nama; jika belum, biarkan `null`.
2. Jalankan `/viral-research` untuk mendapat daftar topik bersinyal, atau langsung `/history-documentary <topik>`.
3. Baca paket yang kembali. Jawab dengan "Setujui gerbang A" atau minta perubahan.
4. Ulangi untuk gerbang B (naskah), C (aset final), D (aksi publikasi).

## Empat gerbang persetujuan
| Gerbang | Yang Anda setujui |
|---|---|
| A | Topik dan sudut |
| B | Naskah dan klaim faktual |
| C | Video, thumbnail, subtitle, metadata final |
| D | Aksi publikasi persis: akun, platform, tanggal, jam |
Persetujuan satu gerbang tidak berlaku untuk gerbang lain. Catat di `templates/approval-record.md`.

## Rutinitas harian yang disarankan
- Pagi: `/daily-content` atau `/production-board` untuk melihat status.
- Setelah naskah disetujui: `/repurpose-content` untuk versi Shorts, Reels, TikTok.
- Setelah unggah: tempel data performa nyata ke `/weekly-report` tiap pekan.

## Daftar command
| Command | Fungsi |
|---|---|
| `/daily-content` | Paket konten harian 3 platform |
| `/history-documentary` | Dokumenter sejarah dari riset sampai storyboard |
| `/youtube-video` | Video panjang YouTube lengkap dengan metadata dan thumbnail |
| `/tiktok-video` | Satu video TikTok |
| `/facebook-reels` | Satu Reels Facebook |
| `/viral-research` | Topik bersinyal nyata (tanpa janji viral) |
| `/content-campaign` | Seri 2-4 minggu |
| `/content-audit` | Audit draf terhadap rubrik QC |
| `/repurpose-content` | Satu aset menjadi tiga platform |
| `/weekly-report` | Laporan mingguan dari data Anda |
| `/thumbnail-lab` | Judul dan thumbnail |
| `/production-board` | Papan produksi dan jadwal |

## Arti label
- **TERVERIFIKASI:** punya sumber yang bisa dibuka. **DIPERSOALKAN:** sejarawan berbeda tafsir. **BELUM TERVERIFIKASI:** belum ada bukti kuat. **KREATIF:** dramatisasi yang dilabeli.
- **ASUMSI:** tebakan terstruktur yang perlu Anda koreksi.

## Yang perlu Anda ketahui
- Publikasi, penjadwalan, dan pembacaan analitik otomatis memerlukan integrasi resmi (belum terpasang). Saat ini studio menyiapkan teks dan aset siap salin.
- Untuk kebijakan platform, syarat monetisasi, dan lisensi musik, agen selalu meminta verifikasi ke sumber resmi pada hari unggah.
- Validasi repositori: `python3 tools/validate.py`.
