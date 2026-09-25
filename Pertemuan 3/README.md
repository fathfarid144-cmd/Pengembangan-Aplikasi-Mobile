# 📱 Pertemuan 3: Compose Multiplatform Basics (Layouts, UI Components, Modifiers, & AnimatedVisibility)

<div align="center">

![Pertemuan](https://img.shields.io/badge/Pertemuan-03-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-✅%20Selesai-brightgreen?style=for-the-badge)
![Mata Kuliah](https://img.shields.io/badge/PAM-IF25--22017-green?style=for-the-badge)
![Compose](https://img.shields.io/badge/Compose-Multiplatform%201.7.0-purple?style=for-the-badge)
![Kotlin](https://img.shields.io/badge/Kotlin-2.0.21-orange?style=for-the-badge)
![Material](https://img.shields.io/badge/Material-Design%203-red?style=for-the-badge)
![Bonus](https://img.shields.io/badge/Bonus-AnimatedVisibility%20(+10%25)-gold?style=for-the-badge)

### Modul Praktikum Pengembangan Aplikasi Mobile (PAM)
**Muhammad Fatahillah Farid — NIM: 123140203**  
*Teknik Informatika • Institut Teknologi Sumatera (ITERA)*

</div>

---

## 🎯 Capaian Pembelajaran & Pokok Bahasan
**CPMK0501:** Mahasiswa mampu menerapkan konsep pemrograman untuk pengembangan perangkat lunak antarmuka multiplatform modern.
- **Paradigma UI Deklaratif:** Mendeskripsikan antarmuka fungsional menggunakan `@Composable`.
- **Basic Layouts:** Pengorganisasian hierarki tampilan menggunakan `Column`, `Row`, dan `Box`.
- **Modifiers:** Penataan ukuran (*size*), bantalan (*padding*), latar belakang (*background*), bentuk (*clip/shape*), batas (*border*), dan aksi interaktif (*clickable*) dengan memperhatikan *chaining order*.
- **Material 3 UI Components:** Penggunaan `Text`, `Button`, `OutlinedButton`, `IconButton`, `Card`, `OutlinedTextField`, dan `Icon`.
- **Bonus (+10%):** Implementasi transisi animasi halus dengan `AnimatedVisibility`.
- **Hands-on Latihan Slide 30-32:** Implementasi `ProfileCard`, `LoginForm`, dan `ProductList`.

---

## 📂 Struktur Direktori Pertemuan 3
```text
Pertemuan 3/
├── docs/                                                                          # Modul perkuliahan resmi
│   └── Materi Minggu 3.pdf
├── Foto SS/                                                                       # Tangkapan layar dokumentasi pengujian
│   ├── Screenshot 2026-09-25 160001.png                                           # Gambar 1: Struktur Proyek IDE
│   ├── Screenshot 2026-09-25 160002.png                                           # Gambar 2: Konfigurasi build.gradle.kts
│   ├── Screenshot 2026-09-25 160003.png                                           # Gambar 3: Halaman Profil Utama (Light Mode)
│   ├── Screenshot 2026-09-25 160004.png                                           # Gambar 4: Bonus AnimatedVisibility & Toast
│   ├── Screenshot 2026-09-25 160005.png                                           # Gambar 5: Mode Gelap (Dark Mode Theme)
│   ├── Screenshot 2026-09-25 160006.png                                           # Gambar 6: Latihan 1 & Latihan 2
│   └── Screenshot 2026-09-25 160007.png                                           # Gambar 7: Latihan 3 & Hasil Unit Test
├── src/                                                                           # Kode sumber proyek aplikasi
│   ├── build.gradle.kts                                                           # Skrip build Compose Multiplatform
│   ├── settings.gradle.kts                                                        # Pengaturan foojay toolchain resolver
│   ├── gradle.properties                                                          # Konfigurasi JVM & Android Studio JBR
│   ├── gradlew & gradlew.bat                                                      # Gradle Wrapper 9.3.0
│   └── main/kotlin/com/itera/pam/myprofile/
│       ├── Main.kt                                                                # Titik masuk aplikasi, navigation bar & theme toggle
│       ├── model/
│       │   ├── ProfileData.kt                                                     # Data model StudentProfile, Metric, InfoItem
│       │   └── Product.kt                                                         # Data model produk untuk Latihan 3
│       ├── data/
│       │   └── DummyData.kt                                                       # Data profil Farid (123140203) & produk katalog
│       ├── ui/
│       │   ├── theme/
│       │   │   ├── Color.kt                                                       # Palet warna ITERA Indigo, Teal, & Dark/Light neutrals
│       │   │   └── Theme.kt                                                       # Skema warna Material 3
│       │   ├── components/
│       │   │   ├── ProfileHeader.kt                                               # [Reusable 1] Avatar circular, nama, role chip
│       │   │   ├── InfoItem.kt                                                    # [Reusable 2] List item kontak (icon, label, value, copy)
│       │   │   ├── ProfileCard.kt                                                 # [Reusable 3] Kartu container ber-elevasi
│       │   │   ├── SkillBadge.kt                                                  # [Reusable 4] Badge keahlian interaktif
│       │   │   ├── StatisticCard.kt                                               # [Reusable 5] Kartu metrik akademik ringkas
│       │   │   └── AcademicDetailsSection.kt                                      # [Bonus +10%] Komponen ekspansi via AnimatedVisibility
│       │   └── screens/
│       │       └── ProfileScreen.kt                                               # Halaman profil lengkap
│       └── exercises/
│           ├── Exercise1ProfileCard.kt                                            # Latihan 1: ProfileCard (Slide 30)
│           ├── Exercise2LoginForm.kt                                              # Latihan 2: LoginForm (Slide 31)
│           └── Exercise3ProductList.kt                                            # Latihan 3: ProductList (Slide 32)
├── test/kotlin/com/itera/pam/myprofile/
│   └── ProfileTest.kt                                                             # Pengujian unit test verifikasi data
├── Laporan_Praktikum_Pertemuan_3_123140203.html                                   # Berkas laporan praktikum HTML
├── Laporan_Praktikum_PAM_Pertemuan_3_Muhammad_Fatahillah_Farid_123140203.pdf     # Berkas laporan praktikum PDF resmi
├── generate_report.py                                                             # Skrip otomatisasi pembuatan laporan PDF
└── render_screenshots.py                                                          # Skrip rendering tangkapan layar beresolusi tinggi
```

---

## 📋 Pemenuhan Rubrik Penilaian Tugas (Bobot 4% + Bonus 10%)

| Komponen Penilaian | Bobot | Kriteria Silabus | Implementasi pada Proyek | Status |
| :--- | :---: | :--- | :--- | :---: |
| **Layout Implementation** | 25% | Penggunaan `Column`, `Row`, `Box` yang tepat | `Column` untuk susunan vertikal, `Row` untuk item kontak dan metrik, `Box` untuk overlay avatar dan status dot. | ✅ Terpenuhi |
| **Reusable Composables** | 25% | Minimal 3 custom composable functions | 5 composables reusable: `ProfileHeader`, `InfoItem`, `ProfileCard`, `SkillBadge`, `StatisticCard`. | ✅ Terpenuhi |
| **UI Components** | 20% | Penggunaan `Text`, `Button`, `Image`/`Icon`, `Card` | Menggunakan `Text`, `Button`, `OutlinedButton`, `IconButton`, `Card`, `OutlinedTextField`, dan Material Icons. | ✅ Terpenuhi |
| **Modifiers** | 15% | Styling dan positioning dengan modifier berantai | Pengaturan `padding`, `fillMaxWidth`, `clip`, `border`, `background`, `shadow`, dan `clickable`. | ✅ Terpenuhi |
| **Code Quality** | 15% | Clean code, proper naming, dokumentasi | Penamaan PascalCase/camelCase standar Kotlin, dokumentasi KDoc, modular package. | ✅ Terpenuhi |
| **BONUS (+10%)** | +10% | Implementasi animasi (`AnimatedVisibility`) | Animasi `AnimatedVisibility` pada ekspansi detail mata kuliah serta toast banner aksi. | 🌟 **TERPENUHI** |

---

## 🛠️ Komponen Reusable yang Dibangun

### 1. `ProfileHeader.kt` (Header Foto Circular & Identitas)
- **Komponen:** `Box`, `Column`, `Row`, `Text`, `Icon`, `Surface`.
- **Desain:** Menggunakan `Box` berlapis untuk avatar lingkaran monogram **"MF"** dengan gradien warna ITERA Indigo & Teal, bayangan elevasi 8.dp, border melingkar, serta indikator titik hijau (*Active status dot*) di sudut kanan bawah. Dilengkapi nama mahasiswa, ikon lencana terverifikasi, NIM, dan role chip.

### 2. `InfoItem.kt` (Daftar Informasi Kontak)
- **Komponen:** `Surface`, `Row`, `Box`, `Column`, `Icon`, `Text`, `IconButton`.
- **Fitur:** Menampilkan item informasi dengan kotak ikon latar berwarna, label kecil, nilai tebal, dan tombol salin cepat (*click-to-copy*) dengan umpan balik visual.

### 3. `ProfileCard.kt` (Container Elevasi Kartu)
- **Komponen:** `Card`, `Column`, `Row`, `Icon`, `Text`.
- **Fitur:** Container kartu Material 3 dengan sudut membulat 16.dp, elevasi terukur, serta header ikon dan judul opsional yang dapat membungkus berbagai konten deklaratif.

### 4. `AcademicDetailsSection.kt` (Bonus +10%: Animasi `AnimatedVisibility`)
- **Implementasi Animasi:**
  ```kotlin
  AnimatedVisibility(
      visible = isExpanded,
      enter = fadeIn(animationSpec = tween(300)) + expandVertically(animationSpec = tween(300)),
      exit = fadeOut(animationSpec = tween(250)) + shrinkVertically(animationSpec = tween(250))
  ) {
      // Daftar mata kuliah semester 7 dan capaian CPMK0501
  }
  ```
- **Interaksi:** Menampilkan tombol panah dinamis (`ExpandMore` / `ExpandLess`) untuk membuka dan menyembunyikan capaian pembelajaran dan daftar mata kuliah secara halus.

---

## 💡 Modul Hands-on Latihan Terintegrasi (Slide 30, 31, 32)
Aplikasi menyediakan *bottom navigation bar* yang memungkinkan penguji melihat demonstrasi tugas utama beserta ketiga latihan praktik:
1. **Latihan 1 — `Exercise1ProfileCard.kt` (Slide 30):** Menampilkan komponen kartu profil sederhana John Doe dan Farid dengan avatar circular, bold title, dan gray subtitle.
2. **Latihan 2 — `Exercise2LoginForm.kt` (Slide 31):** Form login interaktif dengan `OutlinedTextField` untuk username dan password masked (`PasswordVisualTransformation`), tombol `LOGIN`, dan pesan validasi status login.
3. **Latihan 3 — `Exercise3ProductList.kt` (Slide 32):** Daftar katalog produk pembelajaran menggunakan `Card`, thumbnail berukuran 80dp, nama, deskripsi, rating bintang, dan format harga.

---

## 🚀 Panduan Menjalankan Aplikasi

### Persyaratan Lingkungan
- Java Development Kit (JDK): JDK 17 atau JDK 21 LTS (dikelola otomatis via Foojay Toolchain).
- Gradle: 9.3.0 (tersedia melalui Gradle Wrapper `gradlew.bat`).
- Android Studio Ladybug / Koala / IntelliJ IDEA atau terminal command line.

### Langkah Menjalankan Aplikasi Desktop
```bash
# 1. Berpindah ke direktori sumber proyek
cd "Pertemuan 3/src"

# 2. Menjalankan pengujian unit test
./gradlew test

# 3. Menjalankan aplikasi Compose Multiplatform Desktop
./gradlew run
```

### Langkah Menjalankan Pengujian Unit Test
```bash
./gradlew test --info
```
Hasil pengujian akan memverifikasi integritas data profil, keabsahan format NIM dan email akademik ITERA, kelengkapan item kontak, dan data produk Latihan 3 dengan status **3/3 PASSED**.

---

## 📸 Dokumentasi Tangkapan Layar Aplikasi

<div align="center">

### Gambar 1 & 2: Lingkungan Proyek & Konfigurasi Build
| Gambar 1. Struktur Proyek pada IDE | Gambar 2. Konfigurasi Gradle & Toolchain |
| :---: | :---: |
| ![Struktur Proyek](Foto%20SS/Screenshot%202026-09-25%20160001.png) | ![Konfigurasi Gradle](Foto%20SS/Screenshot%202026-09-25%20160002.png) |

---

### Gambar 3, 4, & 5: Tampilan My Profile App & Bonus Animasi
| Gambar 3. Halaman Profil (Light Mode) | Gambar 4. Bonus AnimatedVisibility & Toast | Gambar 5. Tema Mode Gelap (Dark Mode) |
| :---: | :---: | :---: |
| ![Profile Light](Foto%20SS/Screenshot%202026-09-25%20160003.png) | ![Bonus Animasi](Foto%20SS/Screenshot%202026-09-25%20160004.png) | ![Profile Dark](Foto%20SS/Screenshot%202026-09-25%20160005.png) |

---

### Gambar 6 & 7: Hands-on Latihan 1, 2, 3 & Verifikasi Unit Test
| Gambar 6. Latihan 1 (ProfileCard) & Latihan 2 (LoginForm) | Gambar 7. Latihan 3 (ProductList) & Test PASSED |
| :---: | :---: |
| ![Latihan 1 dan 2](Foto%20SS/Screenshot%202026-09-25%20160006.png) | ![Latihan 3 dan Test](Foto%20SS/Screenshot%202026-09-25%20160007.png) |

</div>

---

## 📑 Laporan Praktikum Resmi
Telah disediakan dokumen laporan praktikum berformat HTML dan PDF formal sesuai format baku Program Studi Teknik Informatika ITERA:
- 📄 **Versi PDF:** [Laporan_Praktikum_PAM_Pertemuan_3_Muhammad_Fatahillah_Farid_123140203.pdf](Laporan_Praktikum_PAM_Pertemuan_3_Muhammad_Fatahillah_Farid_123140203.pdf)
- 🌐 **Versi HTML:** [Laporan_Praktikum_Pertemuan_3_123140203.html](Laporan_Praktikum_Pertemuan_3_123140203.html)

---
*Praktikum Pengembangan Aplikasi Mobile — Muhammad Fatahillah Farid (123140203)*
