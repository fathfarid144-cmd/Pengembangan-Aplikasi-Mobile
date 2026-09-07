import os

pam_dir = r"C:\Kuliah\Semester 7\PAM"
p1_dir = os.path.join(pam_dir, "Pertemuan 1")

# 1. Create .gitignore in PAM
gitignore_content = """# Android Studio & IntelliJ
.idea/
*.iml
.gradle/
build/
captures/
local.properties
.cxx/

# OS & Office Temp Files
Thumbs.db
Desktop.ini
.DS_Store
~$*.docx
*.tmp

# Python Cache
__pycache__/
*.pyc

# VS Code
.vscode/
"""

with open(os.path.join(pam_dir, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(gitignore_content)
print("Created .gitignore in PAM root")

# 2. Syllabi for Pertemuan 1 - 16
meetings = [
    {
        "num": 1,
        "folder": "Pertemuan 1",
        "title": "Pengenalan Android Studio, Toolchain SDK, & Kebutuhan Spesifikasi Laptop",
        "status": "✅ Selesai",
        "desc": "Instalasi resmi Android Studio Quail 4 (2026.1.4), setup Android SDK Platform 37, emulator AVD, analisis spesifikasi hardware laptop (RAM 8GB vs 16GB), optimasi performa, dan pengujian proyek pertama."
    },
    {
        "num": 2,
        "folder": "Pertemuan 2",
        "title": "Activity Lifecycle, View Binding, & Desain Layout XML",
        "status": "⏳ Mendatang",
        "desc": "Siklus hidup Activity (onCreate, onStart, onResume, onPause, onStop, onDestroy), View Binding modern, dan hierarki ViewGroup (ConstraintLayout, LinearLayout, FrameLayout)."
    },
    {
        "num": 3,
        "folder": "Pertemuan 3",
        "title": "Komponen UI Interaktif, Event Handling, & Material 3",
        "status": "⏳ Mendatang",
        "desc": "Eksplorasi TextView, EditText, Button, ImageView, RadioButton, CheckBox, Spinner, penanganan event (OnClickListener), input validation, dan Material 3 styling."
    },
    {
        "num": 4,
        "folder": "Pertemuan 4",
        "title": "Navigasi Antar-Layar: Explicit Intent, Implicit Intent, & Data Passing",
        "status": "⏳ Mendatang",
        "desc": "Perpindahan halaman menggunakan Explicit Intent, pertukaran data antar-activity (Bundle, Intent.putExtra, Parcelable), dan Implicit Intent (telepon, kamera, browser, share)."
    },
    {
        "num": 5,
        "folder": "Pertemuan 5",
        "title": "Penyajian Data Dinamis: RecyclerView, Adapter, ViewHolder, & CardView",
        "status": "⏳ Mendatang",
        "desc": "Implementasi RecyclerView efisien dengan custom Adapter, pattern ViewHolder, DiffUtil, interaksi klik item list, serta layout list dan grid."
    },
    {
        "num": 6,
        "folder": "Pertemuan 6",
        "title": "Modularisasi Tampilan: Fragment, Bottom Navigation, & ViewPager2",
        "status": "⏳ Mendatang",
        "desc": "Konsep Fragment lifecycle, FragmentManager, TabLayout, integrasi ViewPager2 (geser layar), serta implementasi BottomNavigationView modern."
    },
    {
        "num": 7,
        "folder": "Pertemuan 7",
        "title": "Penyimpanan Data Lokal: SQLite & Room Persistence Library",
        "status": "⏳ Mendatang",
        "desc": "Konsep basis data lokal pada Android, arsitektur Room ORM (Entity, DAO, RoomDatabase), operasi CRUD (Create, Read, Update, Delete) secara asinkron."
    },
    {
        "num": 8,
        "folder": "Pertemuan 8",
        "title": "Evaluasi Tengah Semester (UTS) / Ujian Praktikum",
        "status": "⏳ Mendatang",
        "desc": "Pengerjaan proyek evaluasi tengah semester mengintegrasikan seluruh materi Pertemuan 1 hingga Pertemuan 7 (UI, Intent, RecyclerView, Room DB)."
    },
    {
        "num": 9,
        "folder": "Pertemuan 9",
        "title": "Komunikasi Jaringan: RESTful API, Retrofit 2, & Kotlin Coroutines",
        "status": "⏳ Mendatang",
        "desc": "Konsumsi data web service JSON menggunakan Retrofit 2, converter Moshi / Gson, OkHttp logging interceptor, dan penanganan asynchronous dengan Kotlin Coroutines."
    },
    {
        "num": 10,
        "folder": "Pertemuan 10",
        "title": "Manajemen Preferensi & State: DataStore & ViewModel",
        "status": "⏳ Mendatang",
        "desc": "Pengganti SharedPreferences modern dengan Jetpack Preferences DataStore (tipe data aman, asinkron), arsitektur MVVM (Model-View-ViewModel), dan LiveData / StateFlow."
    },
    {
        "num": 11,
        "folder": "Pertemuan 11",
        "title": "Layanan Latar Belakang: WorkManager, BroadcastReceiver, & Notifikasi",
        "status": "⏳ Mendatang",
        "desc": "Eksekusi background task terjadwal dengan WorkManager, penanganan event sistem menggunakan BroadcastReceiver, serta pembuatan Push / Local Notification (NotificationChannel)."
    },
    {
        "num": 12,
        "folder": "Pertemuan 12",
        "title": "Integrasi Backend-as-a-Service: Firebase Auth & Cloud Firestore",
        "status": "⏳ Mendatang",
        "desc": "Otentikasi pengguna (Firebase Authentication: Email/Password & Google Sign-In), penyimpanan basis data cloud NoSQL (Cloud Firestore) secara real-time."
    },
    {
        "num": 13,
        "folder": "Pertemuan 13",
        "title": "Pemanfaatan Sensor & Lokasi: Google Maps SDK & FusedLocationProviderClient",
        "status": "⏳ Mendatang",
        "desc": "Akses permission lokasi runtime, integrasi Google Maps Android SDK, penandaan marker, dan pemanfaatan sensor perangkat keras (akselerometer, giroskop)."
    },
    {
        "num": 14,
        "folder": "Pertemuan 14",
        "title": "Modern Android Development (MAD): Jetpack Compose Declarative UI",
        "status": "⏳ Mendatang",
        "desc": "Paradigma UI deklaratif menggunakan Jetpack Compose, Composable functions, State hoisting, tata letak Row/Column/Box, Material 3 Compose, dan Compose Navigation."
    },
    {
        "num": 15,
        "folder": "Pertemuan 15",
        "title": "Pengujian Aplikasi (Testing), R8 Obfuscation, & Build Release APK/AAB",
        "status": "⏳ Mendatang",
        "desc": "Unit testing (JUnit), UI testing (Espresso / Compose Test), konfigurasi ProGuard / R8 code shrinking, penandatanganan sertifikat (Keystore signing), dan ekspor Android App Bundle (AAB)."
    },
    {
        "num": 16,
        "folder": "Pertemuan 16",
        "title": "Evaluasi Akhir Semester (UAS) & Showcase Proyek Aplikasi Mobile",
        "status": "⏳ Mendatang",
        "desc": "Presentasi tugas besar akhir semester, demo aplikasi mobile lengkap, dokumentasi teknis, dan publikasi repositori GitHub."
    }
]

# 3. Create Root README.md
root_readme = f"""# 📱 Pengembangan Aplikasi Mobile (PAM)

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
"""

for m in meetings:
    root_readme += f"| {m['num']:02d} | [{m['folder']}/]({m['folder'].replace(' ', '%20')}/) | **{m['title']}**<br>_{m['desc']}_ | {m['status']} |\n"

root_readme += """
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
"""

with open(os.path.join(pam_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(root_readme)
print("Created root README.md")


# 4. Create Pertemuan 1 README.md
p1_readme = """# 🛠️ Pertemuan 1: Pengenalan Android Studio & Analisis Spesifikasi Laptop

<div align="center">

![Pertemuan 1](https://img.shields.io/badge/Pertemuan-01-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Selesai%20%E2%9C%85-success?style=for-the-badge)
![Format](https://img.shields.io/badge/Dokumen-Microsoft%20Word%20(.docx)-blue?style=for-the-badge&logo=microsoftword&logoColor=white)

### Modul Praktikum Pengembangan Aplikasi Mobile (PAM)
**Muhammad Fatahillah Farid — NIM: 123140203**  
*Teknik Informatika • Institut Teknologi Sumatera (ITERA)*

</div>

---

## 📄 Berkas Laporan Resmi (Word Document)

Laporan praktikum lengkap telah disusun secara komprehensif dalam format Microsoft Word (**`.docx`**) berstandar akademik yang memuat cover formal, analisis mendalam spesifikasi hardware, 15 langkah tutorial visual dengan tangkapan layar, verifikasi pengujian Hello World, dan panduan troubleshooting:

1. 📥 **[Muhammad Fatahillah Farid_123140203_P1.docx](Muhammad%20Fatahillah%20Farid_123140203_P1.docx)** *(Format penamaan tugas resmi)*
2. 📥 **[Panduan_Instalasi_Android_Studio_dan_Spesifikasi_Laptop.docx](Panduan_Instalasi_Android_Studio_dan_Spesifikasi_Laptop.docx)** *(Salinan berkas panduan teknis)*

---

## 📊 1. Analisis Kebutuhan Spesifikasi Laptop / PC

Pengembangan aplikasi mobile Android menuntut spesifikasi perangkat keras yang memadai karena IDE menjalankan JVM IntelliJ, background indexing, server latar belakang Gradle Daemon, serta mesin virtual emulator Android AVD secara serentak.

### Tabel Komparasi Spesifikasi

| Komponen Hardware | Minimum Resmi (Google) | Rekomendasi Standar | Rekomendasi Optimal (PAM Power User) |
| :--- | :--- | :--- | :--- |
| **Sistem Operasi** | Windows 8 / 10 / 11 (64-bit) | Windows 10 / 11 (64-bit) Update Terkini | Windows 11 (64-bit) Pro / Home |
| **Processor (CPU)** | x86_64 CPU; Intel Core Gen 2 / AMD | Intel Core i5 (Gen 10+) / AMD Ryzen 5 (Min. 4 Core / 8 Thread) | Intel Core i7 (Gen 12+) / AMD Ryzen 7 (8–16 Core / Thread) |
| **Virtualisasi** | VT-x / AMD-V didukung CPU | VT-x / SVM diaktifkan di BIOS & WHPX aktif | Hardware Virtualization + Hyper-V aktif penuh |
| **RAM (Memori)** | 8 GB RAM fisik | **16 GB DDR4 / DDR5 Dual Channel** | **32 GB DDR4 / DDR5 Dual Channel** |
| **Penyimpanan (Disk)**| 8 GB ruang kosong (HDD diizinkan) | **SSD SATA / NVMe** (Min. 30 GB free) | **SSD NVMe M.2 PCIe Gen 4** (60–100 GB free) |
| **Resolusi Layar** | 1280 x 800 piksel | 1920 x 1080 piksel (Full HD 1080p) | 1920 x 1080 atau Dual Monitor |
| **Kartu Grafis (GPU)**| Integrated GPU (OpenGL 3.3) | Dedicated GPU (GTX/RTX / Radeon) | Dedicated GPU RTX 3050+ (DirectX 12/Vulkan) |
| **Koneksi Internet** | 2–5 Mbps | 10–20 Mbps (Kuota min. 5 GB) | 50+ Mbps Fiber Optic Tanpa Kuota |

### 💡 Tips Khusus untuk Laptop RAM 8 GB:
* **Gunakan Smartphone Android Fisik via USB Debugging**: Menghilangkan beban kerja emulator AVD di laptop, langsung menghemat alokasi RAM 2.5 GB – 3.5 GB!
* **Atur JVM Heap Gradle**: Tambahkan `org.gradle.jvmargs=-Xmx1536m -XX:MaxMetaspaceSize=512m` pada berkas `gradle.properties`.
* **Wajib Gunakan SSD**: Menghindari bottleneck *Disk Usage 100%* yang sering terjadi pada HDD mekanik konvensional.
* **Aktifkan Power Save Mode**: Di Android Studio melalui `File > Power Save Mode` saat mengetik kode.

---

## 📸 2. Dokumentasi 15 Langkah Instalasi & Konfigurasi

Rangkaian penginstalan terdokumentasikan secara lengkap dalam 15 langkah visual:

### Fase 1: Pengunduhan Berkas Resmi
* **Langkah 1**: Mengunduh installer resmi Android Studio Quail 4 (2026.1.4) dari `developer.android.com/studio`.  
  ![Langkah 1](Step_01_Download_Android_Studio.png)

### Fase 2: Pemasangan Perangkat Lunak Inti (Windows Setup Wizard)
* **Langkah 2**: Menjalankan installer dengan hak Administrator & Layar Sambutan (*Welcome to Android Studio Setup*).  
  ![Langkah 2](Step_02_Installer_Welcome.png)
* **Langkah 3**: Pemilihan komponen software: Memastikan opsi **Android Studio** dan **Android Virtual Device (AVD)** tercentang.  
  ![Langkah 3](Step_03_Choose_Components.png)
* **Langkah 4**: Konfigurasi lokasi direktori instalasi (`C:\\Program Files\\Android\\Android Studio`).  
  ![Langkah 4](Step_04_Install_Location.png)
* **Langkah 5**: Proses ekstraksi berkas sistem dan font (`NotoSansCJK-Regular.ttc`).  
  ![Langkah 5](Screenshot%202026-09-07%20100427.png)
* **Langkah 6**: Instalasi software selesai & mencentang opsi *Start Android Studio*.  
  ![Langkah 6](Screenshot%202026-09-07%20100532.png)

### Fase 3: Initial Run & Setup Android SDK Toolchain
* **Langkah 7**: Splash Screen inisialisasi Android Studio Quail 4 (2026.1.4).  
  ![Langkah 7](Screenshot%202026-09-07%20100551.png)
* **Langkah 8**: Dialog telemetri dan data privasi *Help improve Android Studio* (*Don't send* / *Send usage statistics*).  
  ![Langkah 8](Screenshot%202026-09-07%20100619.png)
* **Langkah 9**: Memulai *Android Studio Setup Wizard* untuk penyiapan *development environment*.  
  ![Langkah 9](Screenshot%202026-09-07%20100640.png)
* **Langkah 10**: Pemilihan tipe instalasi: Memilih opsi **Standard** yang stabil dan direkomendasikan.  
  ![Langkah 10](Screenshot%202026-09-07%20100650.png)
* **Langkah 11**: Verifikasi pengaturan komponen SDK yang akan diunduh (SDK Platform 37.0, Build-Tools 36, Platform-Tools, Emulator ~600 MB).  
  ![Langkah 11](Screenshot%202026-09-07%20100700.png)
* **Langkah 12**: Persetujuan lisensi legal Google `android-sdk-license` (*Accept*).  
  ![Langkah 12](Screenshot%202026-09-07%20100713.png)
* **Langkah 13**: Proses pengunduhan komponen SDK dari server repositori Google `dl.google.com`.  
  ![Langkah 13](Screenshot%202026-09-07%20100722.png)
* **Langkah 14**: Log konfirmasi instalasi komponen selesai (*"Android SDK is up to date"*).  
  ![Langkah 14](Screenshot%202026-09-07%20101547.png)

### Fase 4: Dashboard Utama Siap Pakai
* **Langkah 15**: Tampilan selamat datang di Android Studio (*New Project*, *Open*, *Clone Repository*, *Customize*, *Plugins*, *Learn*).  
  ![Langkah 15](Screenshot%202026-09-07%20101602.png)

---

## 🧪 3. Verifikasi Pengujian Proyek Pertama (Hello World)

1. **Pembuatan Proyek**: Memilih template `Empty Views Activity` atau `Empty Activity (Compose)`.
2. **Konfigurasi Project**:
   * Name: `MyFirstPAMApp`
   * Package: `com.example.myfirstpamapp`
   * Language: `Kotlin`
   * Minimum SDK: `API 26 (Android 8.0 Oreo)`
   * Build Configuration: `Kotlin DSL (build.gradle.kts)`
3. **Gradle Sync**: Menunggu dependensi selesai diunduh hingga muncul status *"BUILD SUCCESSFUL"*.
4. **Execution (Run App)**: Menjalankan aplikasi ke perangkat emulator AVD atau smartphone fisik via USB Debugging.

---

## 🛠️ 4. Panduan Troubleshooting Singkat

| Permasalahan | Penyebab Utama | Solusi Tindakan |
| :--- | :--- | :--- |
| **VT-x / AMD-V Disabled** | Fitur virtualisasi CPU belum diaktifkan di BIOS | Masuk BIOS (F2/F12/Del) > Menu Advanced / CPU > Aktifkan *Intel Virtualization Technology* atau *SVM Mode*. |
| **Gradle Sync Timeout** | Koneksi internet terhalang firewall / proxy | Beralih ke Hotspot seluler pribadi, lalu klik ikon Gajah *Sync Project with Gradle Files*. |
| **SDK Path Spasi Error** | Username Windows memiliki spasi (`C:\\Users\\Nama User\\...`) | Buka *Tools > SDK Manager* > Pindahkan direktori SDK ke path tanpa spasi seperti `C:\\Android\\Sdk`. |
| **Device Unauthorized** | Belum menyetujui izin USB Debugging di HP | Pada HP, buka Developer Options > Revoke USB debugging > cabut & colok ulang kabel > centang *"Always allow"* > ketuk OK. |
| **Out of Memory Error** | Heap Java kompilasi melebihi kapasitas | Buka `gradle.properties`, tambahkan: `org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m`. |

---
*Dokumen Laporan Praktikum Pertemuan 1 — Muhammad Fatahillah Farid (123140203)*
"""

with open(os.path.join(p1_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(p1_readme)
print("Created Pertemuan 1 README.md")


# 5. Create folders Pertemuan 2 through 16 with .gitkeep and structured README.md
for m in meetings[1:]:
    folder_path = os.path.join(pam_dir, m["folder"])
    os.makedirs(folder_path, exist_ok=True)
    
    # Create .gitkeep
    with open(os.path.join(folder_path, ".gitkeep"), "w", encoding="utf-8") as f:
        f.write("")
        
    # Create structured README.md for each meeting
    meeting_readme = f"""# 📱 {m['folder']}: {m['title']}

<div align="center">

![Pertemuan](https://img.shields.io/badge/Pertemuan-{m['num']:02d}-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-{m['status'].replace(' ', '%20')}-orange?style=for-the-badge)
![Mata Kuliah](https://img.shields.io/badge/PAM-Pertemuan%20{m['num']:02d}-green?style=for-the-badge)

### Modul Praktikum Pengembangan Aplikasi Mobile (PAM)
**Muhammad Fatahillah Farid — NIM: 123140203**  
*Teknik Informatika • Institut Teknologi Sumatera (ITERA)*

</div>

---

## 🎯 Pokok Bahasan & Silabus
{m['desc']}

---

## 📂 Struktur Direktori Pertemuan
```text
{m['folder']}/
├── README.md               # Dokumentasi dan laporan praktikum
├── docs/                   # Modul, materi, dan dokumentasi PDF/Word
└── src/                    # Kode sumber proyek aplikasi Android Studio
```

---

## 📌 Rencana Kegiatan Pembelajaran
1. Pemaparan konsep teori dan arsitektur materi {m['title']}.
2. Praktikum mandiri / terbimbing pembuatan aplikasi mobile di Android Studio.
3. Pengujian fitur pada perangkat pengujian (AVD Emulator / Smartphone fisik).
4. Dokumentasi teknis dan pengunggahan hasil praktikum ke repositori GitHub.

---
*Praktikum Pengembangan Aplikasi Mobile — Muhammad Fatahillah Farid (123140203)*
"""
    with open(os.path.join(folder_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(meeting_readme)
    print(f"Created {m['folder']} with .gitkeep and README.md")

print("All directories and README files created successfully!")
