import os
import base64
import subprocess

def get_base64_img(rel_path):
    if not os.path.exists(rel_path):
        return ""
    with open(rel_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{data}"

base_dir = os.path.dirname(os.path.abspath(__file__))
foto_dir = os.path.join(base_dir, "Foto SS")

img1 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160001.png"))
img2 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160002.png"))
img3 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160003.png"))
img4 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160004.png"))
img5 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160005.png"))
img6 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160006.png"))
img7 = get_base64_img(os.path.join(foto_dir, "Screenshot 2026-09-25 160007.png"))

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Laporan Praktikum PAM Pertemuan 3 - 123140203</title>
<style>
    @page {{
        size: A4;
        margin: 18mm 16mm 18mm 16mm;
    }}
    body {{
        font-family: 'Times New Roman', Times, serif;
        font-size: 11pt;
        line-height: 1.45;
        color: #111;
        margin: 0;
        padding: 0;
    }}
    .header-box {{
        text-align: center;
        border-bottom: 2px solid #000;
        padding-bottom: 6px;
        margin-bottom: 14px;
    }}
    .header-box h2 {{
        margin: 0 0 2px 0;
        font-size: 13pt;
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 0.5px;
    }}
    .header-box h3 {{
        margin: 0 0 2px 0;
        font-size: 11pt;
        font-weight: normal;
    }}
    .header-box p {{
        margin: 0;
        font-size: 9pt;
        color: #333;
    }}
    .report-title {{
        text-align: center;
        margin-top: 10px;
        margin-bottom: 14px;
    }}
    .report-title h1 {{
        font-size: 13.5pt;
        font-weight: bold;
        margin: 0 0 3px 0;
        text-transform: uppercase;
    }}
    .report-title h2 {{
        font-size: 11.5pt;
        font-weight: bold;
        margin: 0 0 8px 0;
    }}
    .identity-table {{
        margin: 0 auto 16px auto;
        border-collapse: collapse;
        width: 90%;
        background-color: #fafafa;
        border: 1px solid #ccc;
    }}
    .identity-table td {{
        padding: 4px 10px;
        font-size: 10.5pt;
    }}
    .identity-table td.label {{
        width: 32%;
        font-weight: bold;
    }}
    .identity-table td.colon {{
        width: 3%;
        text-align: center;
    }}
    h2.section-title {{
        font-size: 11.5pt;
        font-weight: bold;
        border-bottom: 1px solid #333;
        padding-bottom: 3px;
        margin-top: 16px;
        margin-bottom: 8px;
        text-transform: uppercase;
    }}
    h3.sub-title {{
        font-size: 10.5pt;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 4px;
    }}
    p {{
        margin: 0 0 8px 0;
        text-align: justify;
    }}
    ul, ol {{
        margin: 0 0 10px 0;
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 3px;
        text-align: justify;
    }}
    .code-snippet {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 9pt;
        background-color: #f5f5f5;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 8px 12px;
        margin: 8px 0 12px 0;
        white-space: pre-wrap;
        line-height: 1.35;
    }}
    .figure-container {{
        text-align: center;
        margin: 12px auto;
        page-break-inside: avoid;
    }}
    .figure-container img {{
        max-width: 88%;
        max-height: 380px;
        height: auto;
        border: 1px solid #bbb;
        border-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }}
    .figure-caption {{
        font-size: 9.5pt;
        font-style: italic;
        margin-top: 4px;
        color: #222;
        text-align: center;
    }}
    .two-col-images {{
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin: 10px 0;
        page-break-inside: avoid;
    }}
    .two-col-images .col {{
        flex: 1;
        text-align: center;
    }}
    .two-col-images img {{
        max-width: 100%;
        max-height: 340px;
        height: auto;
        border: 1px solid #bbb;
        border-radius: 4px;
    }}
    table.data-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 10px 0 14px 0;
        font-size: 10pt;
    }}
    table.data-table th, table.data-table td {{
        border: 1px solid #444;
        padding: 5px 8px;
    }}
    table.data-table th {{
        background-color: #f0f0f0;
        font-weight: bold;
        text-align: center;
    }}
    .page-break {{
        page-break-before: always;
    }}
</style>
</head>
<body>

<div class="header-box">
    <h2>Institut Teknologi Sumatera</h2>
    <h3>Jurusan Teknologi Produksi dan Industri • Program Studi Teknik Informatika</h3>
    <p>Jalan Terusan Ryacudu, Way Hui, Kec. Jati Agung, Kabupaten Lampung Selatan, Lampung 35365</p>
</div>

<div class="report-title">
    <h1>Laporan Praktikum Pengembangan Aplikasi Mobile</h1>
    <h2>Pertemuan 3: Compose Multiplatform Basics (Layouts, UI Components, Modifiers, & AnimatedVisibility)</h2>
</div>

<table class="identity-table">
    <tr>
        <td class="label">Nama Lengkap</td>
        <td class="colon">:</td>
        <td>Muhammad Fatahillah Farid</td>
    </tr>
    <tr>
        <td class="label">NIM</td>
        <td class="colon">:</td>
        <td>123140203</td>
    </tr>
    <tr>
        <td class="label">Mata Kuliah / Kode</td>
        <td class="colon">:</td>
        <td>Pengembangan Aplikasi Mobile (PAM) / IF25-22017</td>
    </tr>
    <tr>
        <td class="label">Semester / Tahun Akademik</td>
        <td class="colon">:</td>
        <td>Semester 7 / Genap 2025/2026</td>
    </tr>
    <tr>
        <td class="label">Repositori GitHub</td>
        <td class="colon">:</td>
        <td><a href="https://github.com/fathfarid144-cmd/Pengembangan-Aplikasi-Mobile/tree/main/Pertemuan%203" style="color: #1e3a8a; text-decoration: underline; font-weight: 500;">https://github.com/fathfarid144-cmd/Pengembangan-Aplikasi-Mobile/tree/main/Pertemuan%203</a></td>
    </tr>
    <tr>
        <td class="label">Tanggal Pelaksanaan</td>
        <td class="colon">:</td>
        <td>25 September 2026</td>
    </tr>
</table>

<h2 class="section-title">I. Capaian Pembelajaran (CPMK) & Tujuan Praktikum</h2>
<p>
    Berdasarkan silabus dan modul pembelajaran Minggu 3 (CPMK0501: Mahasiswa mampu menerapkan konsep pemrograman untuk pengembangan perangkat lunak multiplatform), praktikum ini bertujuan agar mahasiswa:
</p>
<ol>
    <li>Memahami paradigma antarmuka pengguna (UI) deklaratif pada Compose Multiplatform dan perbedaannya dengan pendekatan imperatif berbasis XML konvensional.</li>
    <li>Mampu mendesain dan mengimplementasikan <em>Composable Functions</em> yang modular, bersih, dan dapat digunakan kembali (<em>reusable</em>).</li>
    <li>Menguasai penggunaan <em>Basic Layouts</em> fundamental: <code>Column</code> (susunan vertikal), <code>Row</code> (susunan horizontal), dan <code>Box</code> (penumpukan layer/stack).</li>
    <li>Menerapkan rangkaian <em>Modifiers</em> untuk pengaturan ukuran (<em>size</em>), jarak (<em>padding</em>), latar belakang (<em>background</em>), bentuk (<em>clip/shape</em>), border, dan penanganan interaksi klik (<em>clickable</em>) dengan memperhatikan urutan eksekusi rantai (<em>chaining order</em>).</li>
    <li>Mengimplementasikan komponen UI Material 3: <code>Text</code>, <code>Button</code>, <code>OutlinedButton</code>, <code>IconButton</code>, <code>Card</code>, <code>OutlinedTextField</code>, serta <code>Icon</code>/<code>Image</code>.</li>
    <li><strong>Bonus Nilai (+10%):</strong> Menguasai dan mengimplementasikan transisi animasi antarmuka menggunakan <code>AnimatedVisibility</code> (kombinasi <em>fadeIn</em>, <em>fadeOut</em>, <em>expandVertically</em>, dan <em>shrinkVertically</em>).</li>
</ol>

<h2 class="section-title">II. Landasan Teori</h2>

<h3 class="sub-title">2.1 Paradigma UI Deklaratif vs Imperatif</h3>
<p>
    Pada pendekatan imperatif tradisional (Android XML + View binding), pengembang menuliskan instruksi mutasi status UI langkah demi langkah (misal <code>findViewById</code>, <code>setText</code>, <code>setVisibility</code>). Sementara pada Compose Multiplatform, UI dideklarasikan secara fungsional menggunakan anotasi <code>@Composable</code>. Fungsi ini mendeskripsikan secara eksplisit bagaimana tampilan seharusnya terlihat berdasarkan <em>state</em> saat ini. Ketika state berubah, Compose secara otomatis melakukan proses <em>Recomposition</em> hanya pada bagian pohon UI yang relevan.
</p>

<h3 class="sub-title">2.2 Tiga Komponen Tata Letak Utama (Layouts)</h3>
<ul>
    <li><strong>Column:</strong> Menyusun elemen anak secara vertikal dari atas ke bawah. Parameter penting meliputi <code>verticalArrangement</code> (misalnya <code>Arrangement.spacedBy(dp)</code>) dan <code>horizontalAlignment</code>.</li>
    <li><strong>Row:</strong> Menyusun elemen anak secara horizontal dari kiri ke kanan. Mendukung pembagian ruang dinamis menggunakan modifier <code>Modifier.weight(1f)</code>.</li>
    <li><strong>Box:</strong> Menyusun elemen secara bertumpuk (<em>stack</em> / <em>z-axis overlay</em>), sangat berguna untuk avatar dengan indikator status aktif atau banner dengan teks di atas gambar.</li>
</ul>

<h3 class="sub-title">2.3 Pentingnya Urutan Modifiers</h3>
<p>
    Modifier adalah objek yang memodifikasi perilaku, ukuran, dan penampilan elemen composable. Di Compose, urutan pemanggilan method pada modifier menentukan urutan eksekusi secara berurutan. Sebagai contoh, menerapkan <code>Modifier.padding(16.dp).background(Color.Blue)</code> akan menghasilkan margin di luar bidang biru, sedangkan <code>Modifier.background(Color.Blue).padding(16.dp)</code> menghasilkan bidang biru penuh dengan bantalan teks di dalamnya.
</p>

<div class="page-break"></div>

<h2 class="section-title">III. Arsitektur Proyek & Implementasi Kode</h2>
<p>
    Aplikasi <strong>"My Profile App"</strong> dibangun dengan mematuhi prinsip arsitektur modular, <em>clean code</em>, serta pemisahan tanggung jawab (<em>separation of concerns</em>) sebagai berikut:
</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Paket / Direktori</th>
            <th>Berkas Sumber</th>
            <th>Peran & Tanggung Jawab</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>model/</code></td>
            <td><code>ProfileData.kt</code>, <code>Product.kt</code></td>
            <td>Struktur data entitas profil mahasiswa, metrik akademik, dan produk latihan.</td>
        </tr>
        <tr>
            <td><code>data/</code></td>
            <td><code>DummyData.kt</code></td>
            <td>Data sumber profil Muhammad Fatahillah Farid (123140203) & data katalog Latihan 3.</td>
        </tr>
        <tr>
            <td><code>ui/theme/</code></td>
            <td><code>Color.kt</code>, <code>Theme.kt</code></td>
            <td>Definisi skema warna Material Design 3 (ITERA Indigo & Teal), palet Dark & Light mode.</td>
        </tr>
        <tr>
            <td><code>ui/components/</code></td>
            <td><code>ProfileHeader.kt</code></td>
            <td><strong>Reusable Composable 1:</strong> Avatar circular (Box layer, gradient, active dot), nama, NIM, verified badge.</td>
        </tr>
        <tr>
            <td><code>ui/components/</code></td>
            <td><code>InfoItem.kt</code></td>
            <td><strong>Reusable Composable 2:</strong> Item informasi kontak (Icon box, label, value, click-to-copy).</td>
        </tr>
        <tr>
            <td><code>ui/components/</code></td>
            <td><code>ProfileCard.kt</code></td>
            <td><strong>Reusable Composable 3:</strong> Container elevasi kartu Material 3 dengan slot konten dinamis.</td>
        </tr>
        <tr>
            <td><code>ui/components/</code></td>
            <td><code>AcademicDetailsSection.kt</code></td>
            <td><strong>Bonus Composable:</strong> Ekspansi daftar mata kuliah semester 7 menggunakan <code>AnimatedVisibility</code>.</td>
        </tr>
        <tr>
            <td><code>ui/screens/</code></td>
            <td><code>ProfileScreen.kt</code></td>
            <td>Layar profil utama yang memadukan seluruh komponen, tata letak, dan interaksi pengguna.</td>
        </tr>
        <tr>
            <td><code>exercises/</code></td>
            <td><code>Exercise1ProfileCard.kt</code></td>
            <td>Implementasi terpadu Latihan 1: ProfileCard (Slide 30).</td>
        </tr>
        <tr>
            <td><code>exercises/</code></td>
            <td><code>Exercise2LoginForm.kt</code></td>
            <td>Implementasi terpadu Latihan 2: LoginForm dengan Password Masking (Slide 31).</td>
        </tr>
        <tr>
            <td><code>exercises/</code></td>
            <td><code>Exercise3ProductList.kt</code></td>
            <td>Implementasi terpadu Latihan 3: ProductList dengan rating dan harga (Slide 32).</td>
        </tr>
        <tr>
            <td><code>src/</code></td>
            <td><code>Main.kt</code></td>
            <td>Entry point aplikasi dengan NavigationBar tab switcher dan theme mode toggle.</td>
        </tr>
    </tbody>
</table>

<h3 class="sub-title">3.1 Potongan Kode Implementasi Bonus (+10%): AnimatedVisibility</h3>
<div class="code-snippet">
// Potongan kode dari AcademicDetailsSection.kt
AnimatedVisibility(
    visible = isExpanded,
    enter = fadeIn(animationSpec = tween(durationMillis = 300)) +
            expandVertically(animationSpec = tween(durationMillis = 300)),
    exit = fadeOut(animationSpec = tween(durationMillis = 250)) +
            shrinkVertically(animationSpec = tween(durationMillis = 250))
) {{
    Column(modifier = Modifier.fillMaxWidth().padding(top = 10.dp)) {{
        HorizontalDivider(color = MaterialTheme.colorScheme.outline.copy(alpha = 0.2f))
        // Render daftar mata kuliah semester 7 dan capaian CPMK0501
        courses.forEach {{ course ->
            Row(verticalAlignment = Alignment.CenterVertically) {{
                Icon(Icons.Default.CheckCircle, contentDescription = null, tint = AccentGreen)
                Text(text = course, style = MaterialTheme.typography.bodyMedium)
            }}
        }}
    }}
}}
</div>

<div class="page-break"></div>

<h2 class="section-title">IV. Hasil Pengujian, Tampilan Antarmuka, dan Analisis</h2>
<p>
    Berikut disajikan dokumentasi visual dan analisis eksekusi sistem dari proyek aplikasi yang telah diselesaikan:
</p>

<div class="figure-container">
    <img src="{img1}" alt="Struktur Direktori Proyek Compose Multiplatform">
    <div class="figure-caption">Gambar 1. Struktur proyek Compose Multiplatform pada lingkungan Android Studio / Antigravity IDE</div>
</div>

<p>
    Pada Gambar 1, tampak struktur proyek yang tersusun rapi di dalam <code>Pertemuan 3/src</code> dengan pembagian paket fungsional yang terdefinisi jelas antara komponen UI, tema, model data, serta modul hands-on latihan praktikum.
</p>

<div class="figure-container">
    <img src="{img2}" alt="Konfigurasi build.gradle.kts dan Toolchain">
    <div class="figure-caption">Gambar 2. Konfigurasi Gradle script (Compose Multiplatform 1.7.0, Kotlin 2.0.21, Foojay Toolchain JDK 21 LTS)</div>
</div>

<p>
    Gambar 2 memperlihatkan skrip <code>build.gradle.kts</code> dan <code>settings.gradle.kts</code>. Proyek memanfaatkan Foojay Toolchain Resolver untuk mendistribusikan OpenJDK 21 Temurin LTS secara otomatis, mengatasi incompatibilitas JVM 25 pada compiler Kotlin dan memastikan stabilitas build multiplatform.
</p>

<div class="page-break"></div>

<div class="two-col-images">
    <div class="col">
        <img src="{img3}" alt="Tampilan Halaman Utama My Profile App Light Mode">
        <div class="figure-caption">Gambar 3. Halaman Utama Profil (Light Mode)</div>
    </div>
    <div class="col">
        <img src="{img4}" alt="Implementasi Bonus AnimatedVisibility">
        <div class="figure-caption">Gambar 4. Interaksi Bonus AnimatedVisibility & Toast</div>
    </div>
</div>

<p>
    Pada <strong>Gambar 3</strong>, halaman profil menampilkan seluruh komponen wajib: foto profil circular dengan inisial "MF" dan active status dot, nama mahasiswa <em>Muhammad Fatahillah Farid</em> (123140203), ringkasan metrik akademik dalam Row of Cards, bio singkat, daftar informasi kontak (Email, Telepon, Lokasi, Kampus), skill chips, serta tombol aksi cepat.
</p>
<p>
    Pada <strong>Gambar 4</strong>, fitur bonus <code>AnimatedVisibility</code> diperagakan ketika kartu detail akademik di-expand. Transisi vertikal dan fade yang mulus menampilkan capaian CPMK0501 serta daftar mata kuliah yang sedang ditempuh. Di bagian bawah, toast feedback interaktif muncul saat tombol salin NIM diklik.
</p>

<div class="two-col-images">
    <div class="col">
        <img src="{img5}" alt="Tampilan My Profile App pada Dark Mode">
        <div class="figure-caption">Gambar 5. Tampilan Aplikasi dalam Mode Gelap (Dark Mode)</div>
    </div>
    <div class="col">
        <img src="{img6}" alt="Tampilan Latihan 1 dan Latihan 2">
        <div class="figure-caption">Gambar 6. Implementasi Hands-on Latihan 1 & Latihan 2</div>
    </div>
</div>

<p>
    <strong>Gambar 5</strong> membuktikan konsistensi adaptasi tema Material 3 ketika mode gelap diaktifkan melalui tombol toggle di TopAppBar. Seluruh surface, elevation, dan kontras warna secara otomatis beralih ke palet <em>Dark Neutral</em> yang nyaman di mata.
</p>
<p>
    <strong>Gambar 6</strong> mendokumentasikan implementasi dua latihan hands-on dari materi slide: Latihan 1 (ProfileCard dengan avatar circular, bold title, and gray subtitle) dan Latihan 2 (LoginForm dengan OutlinedTextField, PasswordVisualTransformation, dan tombol Login dengan validasi kredensial).
</p>

<div class="figure-container">
    <img src="{img7}" alt="Tampilan Latihan 3 dan Hasil Eksekusi Unit Test">
    <div class="figure-caption">Gambar 7. Implementasi Latihan 3 (ProductList) dan Verifikasi Build & Test Terminal (BUILD SUCCESSFUL)</div>
</div>

<p>
    Pada <strong>Gambar 7</strong>, terlihat implementasi Latihan 3 (ProductList) yang menampilkan katalog produk berbasis Card dan Row. Di sampingnya, log terminal mengonfirmasi bahwa seluruh rangkaian pengujian unit test (<code>ProfileTest.kt</code>) telah dijalankan melalui <code>gradlew test</code> dan seluruhnya berstatus <strong>PASSED (BUILD SUCCESSFUL)</strong>.
</p>

<h2 class="section-title">V. Kesimpulan</h2>
<ol>
    <li>Compose Multiplatform memberikan efisiensi signifikan dalam pengembangan antarmuka mobile melalui paradigma deklaratif yang intuitif, memungkinkan satu basis kode UI Kotlin dieksekusi di multi-target (Android, Desktop, Web).</li>
    <li>Penggunaan layout dasar <code>Column</code>, <code>Row</code>, dan <code>Box</code> terbukti sangat fleksibel dalam membentuk hierarki antarmuka modern yang responsif.</li>
    <li>Urutan penerapan <em>Modifiers</em> memegang peranan krusial dalam menentukan urutan render visual (seperti padding sebelum atau sesudah background).</li>
    <li>Komponen Material 3 (Card, Text, Button, TextField) memfasilitasi pembuatan UI yang estetik, konsisten, dan mudah diakses.</li>
    <li>Implementasi animasi <code>AnimatedVisibility</code> berhasil memberikan <em>micro-interaction</em> yang halus dan profesional pada aplikasi, memenuhi seluruh kriteria tugas reguler maupun poin bonus nilai (+10%).</li>
</ol>

</body>
</html>
"""

html_out_path = os.path.join(base_dir, "Laporan_Praktikum_Pertemuan_3_123140203.html")
pdf_out_path = os.path.join(base_dir, "Laporan_Praktikum_PAM_Pertemuan_3_Muhammad_Fatahillah_Farid_123140203.pdf")

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated at: {html_out_path}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_out_path}",
    "--no-pdf-header-footer",
    html_out_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge print-to-pdf return code:", res.returncode)
if os.path.exists(pdf_out_path):
    print(f"PDF successfully generated: {pdf_out_path} (Size: {os.path.getsize(pdf_out_path)} bytes)")
else:
    print("PDF generation failed!")
