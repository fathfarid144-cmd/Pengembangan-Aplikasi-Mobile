package com.itera.pam.newsfeed.data

import com.itera.pam.newsfeed.model.NewsArticle
import com.itera.pam.newsfeed.model.NewsCategory
import com.itera.pam.newsfeed.model.NewsDetail
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import kotlin.random.Random

/**
 * Repository yang menyediakan data berita.
 *
 * Kelas ini mensimulasikan sumber data berita menggunakan Flow dan Coroutines.
 * Dalam aplikasi nyata, data akan diambil dari API atau database.
 */
class NewsRepository {

    // Database simulasi berita
    private val newsDatabase = listOf(
        NewsArticle(1, "Kotlin 2.0 Resmi Dirilis dengan Fitur K2 Compiler", NewsCategory.TEKNOLOGI,
            "JetBrains mengumumkan rilis stabil Kotlin 2.0 dengan K2 compiler yang lebih cepat.", "Ahmad Rizki"),
        NewsArticle(2, "Tim Nasional Indonesia Lolos ke Piala Dunia 2026", NewsCategory.OLAHRAGA,
            "Prestasi bersejarah! Indonesia berhasil lolos ke Piala Dunia untuk pertama kalinya.", "Budi Santoso"),
        NewsArticle(3, "RUU Perlindungan Data Pribadi Disahkan DPR", NewsCategory.POLITIK,
            "DPR RI resmi mengesahkan RUU Perlindungan Data Pribadi menjadi undang-undang.", "Citra Dewi"),
        NewsArticle(4, "Film Indonesia Raih Penghargaan di Festival Cannes", NewsCategory.HIBURAN,
            "Film karya sutradara muda Indonesia berhasil meraih Palme d'Or di Festival Cannes.", "Diana Putri"),
        NewsArticle(5, "Peneliti LIPI Temukan Spesies Baru di Hutan Kalimantan", NewsCategory.SAINS,
            "Tim peneliti LIPI menemukan spesies katak baru yang hanya ada di Kalimantan.", "Eko Prasetyo"),
        NewsArticle(6, "Android 15 Hadirkan Fitur AI Generatif Bawaan", NewsCategory.TEKNOLOGI,
            "Google mengintegrasikan Gemini langsung ke dalam sistem operasi Android 15.", "Fajar Nugroho"),
        NewsArticle(7, "Liga Champions: Barcelona vs Real Madrid di Final", NewsCategory.OLAHRAGA,
            "El Clasico akan menghiasi final Liga Champions musim ini di Wembley.", "Gunawan Hadi"),
        NewsArticle(8, "Pemilu 2029: KPU Mulai Persiapan Tahapan Awal", NewsCategory.POLITIK,
            "KPU mulai menyusun jadwal dan regulasi untuk Pemilihan Umum 2029.", "Hana Safitri"),
        NewsArticle(9, "Konser Musik Virtual Pertama dengan Teknologi Hologram", NewsCategory.HIBURAN,
            "Konser virtual menggunakan hologram 3D pertama di Indonesia sukses digelar.", "Irfan Maulana"),
        NewsArticle(10, "Vaksin Malaria Baru Terbukti 90% Efektif", NewsCategory.SAINS,
            "Vaksin malaria generasi baru menunjukkan efektivitas hingga 90% dalam uji klinis fase 3.", "Julia Hartono"),
        NewsArticle(11, "Compose Multiplatform 1.6 Mendukung iOS Stabil", NewsCategory.TEKNOLOGI,
            "JetBrains merilis Compose Multiplatform 1.6 dengan dukungan iOS yang sudah stabil.", "Kevin Wijaya"),
        NewsArticle(12, "Olimpiade 2028 Los Angeles: Indonesia Kirim 45 Atlet", NewsCategory.OLAHRAGA,
            "Kontingen Indonesia akan mengirimkan 45 atlet di 12 cabang olahraga ke Olimpiade LA.", "Lina Maharani"),
        NewsArticle(13, "Teleskop James Webb Temukan Planet Mirip Bumi", NewsCategory.SAINS,
            "NASA mengumumkan penemuan exoplanet di zona layak huni yang mirip dengan Bumi.", "Muhammad Ali"),
        NewsArticle(14, "Startup Indonesia Raih Pendanaan Seri C Rp 2 Triliun", NewsCategory.TEKNOLOGI,
            "Startup edtech asal Indonesia berhasil mendapatkan pendanaan terbesar di Asia Tenggara.", "Nadia Kusuma"),
        NewsArticle(15, "Festival Film Indonesia 2026 Umumkan Nominasi", NewsCategory.HIBURAN,
            "FFI 2026 mengumumkan daftar nominasi dengan 8 film berkompetisi di kategori utama.", "Omar Farhan")
    )

    /**
     * Flow yang mensimulasikan data berita baru setiap 2 detik.
     *
     * Flow ini bersifat COLD - hanya berjalan ketika ada collector.
     * Setiap emisi mengirimkan satu NewsArticle secara berurutan.
     *
     * @return Flow<NewsArticle> stream berita yang di-emit setiap 2 detik
     */
    fun getNewsFeed(): Flow<NewsArticle> = flow {
        for (article in newsDatabase) {
            delay(2000L) // Simulasi berita baru setiap 2 detik
            emit(article)
        }
    }

    /**
     * Mengambil detail berita secara async menggunakan suspend function.
     *
     * Mensimulasikan network delay saat mengambil detail dari server.
     *
     * @param articleId ID artikel yang ingin diambil detailnya
     * @return NewsDetail atau null jika tidak ditemukan
     */
    suspend fun fetchNewsDetail(articleId: Int): NewsDetail? {
        delay(Random.nextLong(500, 1500)) // Simulasi network delay

        val article = newsDatabase.find { it.id == articleId } ?: return null

        // Simulasi konten detail berita
        val content = generateDetailContent(article)
        val relatedTopics = generateRelatedTopics(article.category)
        val viewCount = Random.nextInt(100, 10000)

        return NewsDetail(
            article = article,
            content = content,
            relatedTopics = relatedTopics,
            viewCount = viewCount
        )
    }

    /**
     * Mengambil detail dari beberapa berita secara paralel.
     *
     * @param articleIds daftar ID artikel
     * @return List<NewsDetail> detail berita yang berhasil diambil
     */
    suspend fun fetchMultipleNewsDetails(articleIds: List<Int>): List<NewsDetail> {
        return articleIds.mapNotNull { id -> fetchNewsDetail(id) }
    }

    // Helper: Generate konten detail berita
    private fun generateDetailContent(article: NewsArticle): String {
        return """
            |${article.title}
            |
            |Oleh: ${article.author}
            |Kategori: ${article.category}
            |
            |${article.summary}
            |
            |[Konten lengkap berita disimulasikan di sini. Dalam aplikasi nyata,
            |konten ini akan diambil dari server/API secara asynchronous.]
        """.trimMargin()
    }

    // Helper: Generate topik terkait berdasarkan kategori
    private fun generateRelatedTopics(category: NewsCategory): List<String> {
        return when (category) {
            NewsCategory.TEKNOLOGI -> listOf("Programming", "AI", "Mobile Development", "Cloud Computing")
            NewsCategory.OLAHRAGA -> listOf("Sepak Bola", "Badminton", "Atletik", "E-Sports")
            NewsCategory.POLITIK -> listOf("Pemerintahan", "Legislasi", "Demokrasi", "Kebijakan Publik")
            NewsCategory.HIBURAN -> listOf("Film", "Musik", "Seni", "Festival")
            NewsCategory.SAINS -> listOf("Penelitian", "Biologi", "Fisika", "Astronomi")
        }
    }
}
