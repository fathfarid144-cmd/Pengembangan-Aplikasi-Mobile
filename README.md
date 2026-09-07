# 📱 Pengembangan Aplikasi Mobile (PAM)

<div align="center">

![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)
![Android Studio](https://img.shields.io/badge/Android%20Studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Android%20SDK%2037-blue?style=for-the-badge)
![ITERA](https://img.shields.io/badge/Institution-ITERA-darkblue?style=for-the-badge)

### Repositori Pembelajaran & Modul Praktikum Perkuliahan
**Program Studi Teknik Informatika — Institut Teknologi Sumatera (ITERA)**
*Semester 7 • Tahun Akademik 2026/2027*

</div>

---

## 👤 Informasi Mahasiswa

| Komponen | Keterangan |
| :--- | :--- |
| **Nama Lengkap** | **Muhammad Fatahillah Farid** |
| **NIM** | **123140203** |
| **Mata Kuliah** | Pengembangan Aplikasi Mobile (PAM) |
| **Program Studi** | Teknik Informatika (S1) |
| **Fakultas** | Jurusan Teknologi Produksi dan Industri (JTPI) |
| **Perguruan Tinggi** | Institut Teknologi Sumatera (ITERA) |
| **Repositori GitHub** | [fathfarid144-cmd/Pengembangan-Aplikasi-Mobile](https://github.com/fathfarid144-cmd/Pengembangan-Aplikasi-Mobile) |

---

## 🎯 Deskripsi Mata Kuliah

Mata kuliah **Pengembangan Aplikasi Mobile (PAM)** membahas prinsip, konsep, dan implementasi pembuatan aplikasi pada platform bergerak (*mobile platform*) menggunakan sistem operasi Android. Fokus pembelajaran mencakup penguasaan bahasa pemrograman **Kotlin**, perancangan antarmuka pengguna responsif (*XML* & *Jetpack Compose*), manajemen siklus hidup komponen aplikasi, persistensi data lokal (*Room Database*), integrasi jaringan (*RESTful API* & *Retrofit*), layanan cloud (*Firebase*), pemanfaatan sensor & GPS, hingga proses *deployment* dan *testing* aplikasi berstandar industri.

---

## 🗺️ Roadmap & Silabus Praktikum (Pertemuan 1 – 16)

Berikut adalah daftar folder kegiatan praktikum dan tugas untuk setiap pertemuan:

| No | Folder Pertemuan | Topik & Materi Pembahasan | Status |
| :-: | :--- | :--- | :-: |
| 01 | [Pertemuan 1/](Pertemuan%201/) | **Pengenalan Android Studio, Toolchain SDK, & Kebutuhan Spesifikasi Laptop**<br>_Instalasi resmi Android Studio Quail 4 (2026.1.4), setup Android SDK Platform 37, emulator AVD, analisis spesifikasi hardware laptop (RAM 8GB vs 16GB), optimasi performa, dan pengujian proyek pertama._ | ✅ Selesai |
| 02 | [Pertemuan 2/](Pertemuan%202/) | **Activity Lifecycle, View Binding, & Desain Layout XML**<br>_Siklus hidup Activity (onCreate, onStart, onResume, onPause, onStop, onDestroy), View Binding modern, dan hierarki ViewGroup (ConstraintLayout, LinearLayout, FrameLayout)._ | ⏳ Mendatang |
| 03 | [Pertemuan 3/](Pertemuan%203/) | **Komponen UI Interaktif, Event Handling, & Material 3**<br>_Eksplorasi TextView, EditText, Button, ImageView, RadioButton, CheckBox, Spinner, penanganan event (OnClickListener), input validation, dan Material 3 styling._ | ⏳ Mendatang |
| 04 | [Pertemuan 4/](Pertemuan%204/) | **Navigasi Antar-Layar: Explicit Intent, Implicit Intent, & Data Passing**<br>_Perpindahan halaman menggunakan Explicit Intent, pertukaran data antar-activity (Bundle, Intent.putExtra, Parcelable), dan Implicit Intent (telepon, kamera, browser, share)._ | ⏳ Mendatang |
| 05 | [Pertemuan 5/](Pertemuan%205/) | **Penyajian Data Dinamis: RecyclerView, Adapter, ViewHolder, & CardView**<br>_Implementasi RecyclerView efisien dengan custom Adapter, pattern ViewHolder, DiffUtil, interaksi klik item list, serta layout list dan grid._ | ⏳ Mendatang |
| 06 | [Pertemuan 6/](Pertemuan%206/) | **Modularisasi Tampilan: Fragment, Bottom Navigation, & ViewPager2**<br>_Konsep Fragment lifecycle, FragmentManager, TabLayout, integrasi ViewPager2 (geser layar), serta implementasi BottomNavigationView modern._ | ⏳ Mendatang |
| 07 | [Pertemuan 7/](Pertemuan%207/) | **Penyimpanan Data Lokal: SQLite & Room Persistence Library**<br>_Konsep basis data lokal pada Android, arsitektur Room ORM (Entity, DAO, RoomDatabase), operasi CRUD (Create, Read, Update, Delete) secara asinkron._ | ⏳ Mendatang |
| 08 | [Pertemuan 8/](Pertemuan%208/) | **Evaluasi Tengah Semester (UTS) / Ujian Praktikum**<br>_Pengerjaan proyek evaluasi tengah semester mengintegrasikan seluruh materi Pertemuan 1 hingga Pertemuan 7 (UI, Intent, RecyclerView, Room DB)._ | ⏳ Mendatang |
| 09 | [Pertemuan 9/](Pertemuan%209/) | **Komunikasi Jaringan: RESTful API, Retrofit 2, & Kotlin Coroutines**<br>_Konsumsi data web service JSON menggunakan Retrofit 2, converter Moshi / Gson, OkHttp logging interceptor, dan penanganan asynchronous dengan Kotlin Coroutines._ | ⏳ Mendatang |
| 10 | [Pertemuan 10/](Pertemuan%2010/) | **Manajemen Preferensi & State: DataStore & ViewModel**<br>_Pengganti SharedPreferences modern dengan Jetpack Preferences DataStore (tipe data aman, asinkron), arsitektur MVVM (Model-View-ViewModel), dan LiveData / StateFlow._ | ⏳ Mendatang |
| 11 | [Pertemuan 11/](Pertemuan%2011/) | **Layanan Latar Belakang: WorkManager, BroadcastReceiver, & Notifikasi**<br>_Eksekusi background task terjadwal dengan WorkManager, penanganan event sistem menggunakan BroadcastReceiver, serta pembuatan Push / Local Notification (NotificationChannel)._ | ⏳ Mendatang |
| 12 | [Pertemuan 12/](Pertemuan%2012/) | **Integrasi Backend-as-a-Service: Firebase Auth & Cloud Firestore**<br>_Otentikasi pengguna (Firebase Authentication: Email/Password & Google Sign-In), penyimpanan basis data cloud NoSQL (Cloud Firestore) secara real-time._ | ⏳ Mendatang |
| 13 | [Pertemuan 13/](Pertemuan%2013/) | **Pemanfaatan Sensor & Lokasi: Google Maps SDK & FusedLocationProviderClient**<br>_Akses permission lokasi runtime, integrasi Google Maps Android SDK, penandaan marker, dan pemanfaatan sensor perangkat keras (akselerometer, giroskop)._ | ⏳ Mendatang |
| 14 | [Pertemuan 14/](Pertemuan%2014/) | **Modern Android Development (MAD): Jetpack Compose Declarative UI**<br>_Paradigma UI deklaratif menggunakan Jetpack Compose, Composable functions, State hoisting, tata letak Row/Column/Box, Material 3 Compose, dan Compose Navigation._ | ⏳ Mendatang |
| 15 | [Pertemuan 15/](Pertemuan%2015/) | **Pengujian Aplikasi (Testing), R8 Obfuscation, & Build Release APK/AAB**<br>_Unit testing (JUnit), UI testing (Espresso / Compose Test), konfigurasi ProGuard / R8 code shrinking, penandatanganan sertifikat (Keystore signing), dan ekspor Android App Bundle (AAB)._ | ⏳ Mendatang |
| 16 | [Pertemuan 16/](Pertemuan%2016/) | **Evaluasi Akhir Semester (UAS) & Showcase Proyek Aplikasi Mobile**<br>_Presentasi tugas besar akhir semester, demo aplikasi mobile lengkap, dokumentasi teknis, dan publikasi repositori GitHub._ | ⏳ Mendatang |

---

## 📂 Struktur Direktori Repositori

```text
Pengembangan-Aplikasi-Mobile/
├── .gitignore
├── README.md                                          # Dokumentasi utama repositori
├── Pertemuan 1/                                       # Pengenalan & Instalasi Android Studio
│   ├── README.md                                      # Laporan praktikum Pertemuan 1
│   ├── Muhammad Fatahillah Farid_123140203_P1.docx   # Laporan resmi format Word (NIM & Nama)
│   ├── Panduan_Instalasi_Android_Studio_...docx       # Salinan dokumen panduan lengkap
│   ├── build_full_guide.py                           # Generator berkas Word dokumen
│   ├── generate_missing_screens.py                   # Generator tangkapan layar installer
│   └── *.png                                          # Dokumentasi 15 tangkapan layar otentik
├── Pertemuan 2/                                       # Activity Lifecycle & XML Layout
├── Pertemuan 3/                                       # UI Components & Material 3
├── Pertemuan 4/                                       # Explicit & Implicit Intent
├── Pertemuan 5/                                       # RecyclerView & Adapter Pattern
├── Pertemuan 6/                                       # Fragment & ViewPager2
├── Pertemuan 7/                                       # SQLite & Room Database
├── Pertemuan 8/                                       # Evaluasi Tengah Semester (UTS)
├── Pertemuan 9/                                       # Networking & RESTful API Retrofit
├── Pertemuan 10/                                      # DataStore & ViewModel (MVVM)
├── Pertemuan 11/                                      # Background Work & WorkManager
├── Pertemuan 12/                                      # Firebase Auth & Cloud Firestore
├── Pertemuan 13/                                      # Google Maps SDK & Sensors
├── Pertemuan 14/                                      # Jetpack Compose Declarative UI
├── Pertemuan 15/                                      # Testing, ProGuard & Release Bundle
└── Pertemuan 16/                                      # Evaluasi Akhir Semester (UAS)
```

---

## 💻 Standar Lingkungan Pengembangan (Development Environment)

* **IDE**: Android Studio Quail 4 (Versi 2026.1.4)
* **Bahasa Pemrograman**: Kotlin (Kotlin DSL `build.gradle.kts`)
* **Target SDK**: Android 16 / 17 (API Level 37.0)
* **Minimum SDK**: Android 8.0 Oreo (API Level 26) atau Android 7.0 Nougat (API Level 24)
* **Java Runtime**: JetBrains Runtime (JBR) OpenJDK 21
* **Build System**: Gradle 8.x+
* **VCS**: Git & GitHub

---

## 📝 Lisensi & Hak Cipta

Seluruh kode sumber, dokumentasi, dan materi dalam repositori ini disusun untuk keperluan akademik mata kuliah **Pengembangan Aplikasi Mobile (PAM)** di **Institut Teknologi Sumatera (ITERA)**.

&copy; 2026 **Muhammad Fatahillah Farid (123140203)**. All rights reserved.
