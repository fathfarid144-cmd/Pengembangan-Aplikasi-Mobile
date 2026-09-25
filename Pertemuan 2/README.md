# 📰 News Feed Simulator

<div align="center">

![Pertemuan](https://img.shields.io/badge/Pertemuan-02-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-✅%20Selesai-success?style=for-the-badge)
![Mata Kuliah](https://img.shields.io/badge/PAM-Pertemuan%2002-green?style=for-the-badge)
![Kotlin](https://img.shields.io/badge/Kotlin-1.9.22-purple?style=for-the-badge&logo=kotlin)

### Tugas Praktikum Pengembangan Aplikasi Mobile (PAM)
**Muhammad Fatahillah Farid — NIM: 123140203**  
*Teknik Informatika • Institut Teknologi Sumatera (ITERA)*

</div>

---

## 🎯 Deskripsi Tugas

Membuat aplikasi **"News Feed Simulator"** menggunakan Kotlin yang mengimplementasikan konsep **Advanced Kotlin**, **Coroutines**, dan **Flow** sesuai materi Pertemuan 2.

---

## ✅ Fitur yang Diimplementasikan

| No | Fitur | Deskripsi | Status |
|----|-------|-----------|--------|
| 1 | **Flow** | Flow yang mensimulasikan data berita baru setiap 2 detik | ✅ |
| 2 | **Filter** | Filter berita berdasarkan kategori (Teknologi, Olahraga, Politik, Hiburan, Sains) | ✅ |
| 3 | **Transform** | Transform data menjadi format tampilan menggunakan `map` operator | ✅ |
| 4 | **StateFlow** | StateFlow untuk menyimpan dan memantau jumlah berita yang sudah dibaca | ✅ |
| 5 | **Coroutines** | Coroutines `async/await` untuk mengambil detail berita secara paralel | ✅ |
| 🌟 | **Bonus: Unit Test** | 20 unit tests untuk Flow, StateFlow, dan Coroutines | ✅ |
| 🌟 | **Bonus: Error Handling** | Error handling dengan `.catch` operator dan exception handling | ✅ |

---

## 📂 Struktur Proyek

```text
Pertemuan 2/
├── README.md                          # Dokumentasi proyek
├── docs/                              # Modul dan materi PDF
│   └── Materi_02_Advanced_Kotlin_Coroutines_Flow.pdf
└── src/                               # Kode sumber proyek Kotlin
    ├── build.gradle.kts               # Build configuration (Gradle + Kotlin DSL)
    ├── settings.gradle.kts            # Project settings
    ├── main/kotlin/com/itera/pam/newsfeed/
    │   ├── Main.kt                    # Entry point aplikasi utama
    │   ├── model/
    │   │   └── NewsModels.kt          # Data classes (NewsArticle, NewsCategory, dll)
    │   ├── data/
    │   │   └── NewsRepository.kt      # Repository dengan Flow data source
    │   └── manager/
    │       └── NewsFeedManager.kt     # Business logic, StateFlow, Flow operators
    └── test/kotlin/com/itera/pam/newsfeed/
        └── NewsFeedSimulatorTest.kt   # Unit tests (20 test cases)
```

---

## 🚀 Cara Menjalankan

### Prasyarat
- **JDK 17** atau lebih baru
- **Gradle 8.x** (opsional, bisa menggunakan Gradle wrapper)

### Langkah-langkah

1. **Clone repository:**
   ```bash
   git clone https://github.com/fathfarid144-cmd/Pengembangan-Aplikasi-Mobile.git
   cd "Pengembangan-Aplikasi-Mobile/Pertemuan 2/src"
   ```

2. **Jalankan aplikasi:**
   ```bash
   # Menggunakan Gradle
   gradle run

   # Atau menggunakan Gradle wrapper (jika tersedia)
   ./gradlew run
   ```

3. **Jalankan unit tests:**
   ```bash
   gradle test
   ```

### Alternatif: Jalankan di IntelliJ IDEA / Android Studio
1. Buka folder `src/` sebagai proyek Gradle
2. Tunggu sinkronisasi Gradle selesai
3. Klik kanan `Main.kt` → **Run 'MainKt'**
4. Untuk tests: Klik kanan folder `test` → **Run All Tests**

---

## 📖 Penjelasan Implementasi

### 1. Flow — Stream Berita Real-time
```kotlin
// Flow yang memancarkan berita baru setiap 2 detik
fun getNewsFeed(): Flow<NewsArticle> = flow {
    for (article in newsDatabase) {
        delay(2000L) // Simulasi berita baru setiap 2 detik
        emit(article)
    }
}
```
Flow bersifat **cold** — hanya berjalan ketika ada collector yang mengumpulkan data.

### 2. Filter — Penyaringan Berdasarkan Kategori
```kotlin
.filter { article ->
    category == null || article.category == category
}
```
Menggunakan operator `filter` untuk menyaring berita berdasarkan `NewsCategory` (Teknologi, Olahraga, Politik, Hiburan, Sains).

### 3. Transform — Format Data Tampilan
```kotlin
.map { article ->
    transformToDisplayFormat(article) // NewsArticle → FormattedNews
}
```
Operator `map` mentransformasi `NewsArticle` menjadi `FormattedNews` dengan format yang indah dan indikator prioritas.

### 4. StateFlow — State Management
```kotlin
private val _readCount = MutableStateFlow(0)
val readCount: StateFlow<Int> = _readCount.asStateFlow()

fun markAsRead(articleId: Int) {
    _readCount.value = currentIds.size // Update state secara reaktif
}
```
`StateFlow` digunakan sebagai pengganti LiveData untuk memantau jumlah berita yang sudah dibaca secara reaktif.

### 5. Coroutines Async — Fetch Paralel
```kotlin
val deferredResults = articleIds.map { id ->
    scope.async { repository.fetchNewsDetail(id) }
}
return deferredResults.awaitAll().filterNotNull()
```
Menggunakan `async/await` untuk mengambil detail beberapa berita secara **paralel**, sehingga lebih cepat dibanding sequential.

### 6. Error Handling (Bonus)
```kotlin
.catch { exception ->
    println("[ERROR] Terjadi kesalahan: ${exception.message}")
    emit(FormattedNews("⚠️ Gagal memuat berita.", false))
}
```
Operator `.catch` menangkap error dalam Flow dan menyediakan fallback.

---

## 🧪 Unit Tests

Terdapat **20 test cases** yang mencakup:

| Kategori | Jumlah | Deskripsi |
|----------|--------|-----------|
| Flow Tests | 6 | Emisi data, filter kategori, transformasi, prioritas |
| StateFlow Tests | 6 | Initial state, increment, duplikat, reset, collector |
| Coroutines Tests | 5 | Fetch detail, ID invalid, multiple fetch, paralel, topik |
| Error Handling Tests | 3 | Enum validation, kategori count |

---

## 🏗️ Teknologi yang Digunakan

- **Kotlin 1.9.22** — Bahasa pemrograman utama
- **Kotlinx Coroutines 1.8.0** — Pemrograman asynchronous
- **Kotlinx Coroutines Flow** — Reactive streams
- **Kotlinx Coroutines Test** — Testing coroutines dan Flow
- **Gradle Kotlin DSL** — Build system
- **JUnit 5** — Framework testing

---

## 📝 Rubrik Penilaian

| Komponen | Bobot | Status |
|----------|-------|--------|
| Implementasi Flow | 25% | ✅ Flow builder, emit setiap 2 detik, collect benar |
| Penggunaan Operators | 20% | ✅ filter, map, onEach, catch, take |
| StateFlow Implementation | 20% | ✅ MutableStateFlow, asStateFlow(), reactive updates |
| Coroutines Usage | 20% | ✅ async/await, paralel fetch, suspend functions |
| Kode dan Dokumentasi | 15% | ✅ Clean code, README lengkap, KDoc comments |
| **Bonus** | +10% | ✅ Unit tests + error handling |

---

*Praktikum Pengembangan Aplikasi Mobile — Muhammad Fatahillah Farid (123140203)*
