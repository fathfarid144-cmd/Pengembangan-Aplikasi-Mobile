package com.itera.pam.newsfeed.model

/**
 * Data class untuk merepresentasikan sebuah artikel berita.
 *
 * @property id ID unik berita
 * @property title Judul berita
 * @property category Kategori berita (TEKNOLOGI, OLAHRAGA, POLITIK, HIBURAN, SAINS)
 * @property summary Ringkasan singkat berita
 * @property author Penulis berita
 * @property timestamp Waktu publikasi (epoch millis)
 */
data class NewsArticle(
    val id: Int,
    val title: String,
    val category: NewsCategory,
    val summary: String,
    val author: String,
    val timestamp: Long = System.currentTimeMillis()
)

/**
 * Enum class untuk kategori berita.
 */
enum class NewsCategory(val displayName: String, val emoji: String) {
    TEKNOLOGI("Teknologi", "💻"),
    OLAHRAGA("Olahraga", "⚽"),
    POLITIK("Politik", "🏛️"),
    HIBURAN("Hiburan", "🎬"),
    SAINS("Sains", "🔬");

    override fun toString(): String = "$emoji $displayName"
}

/**
 * Data class untuk detail berita yang diambil secara async.
 *
 * @property article Artikel berita asli
 * @property content Konten lengkap berita
 * @property relatedTopics Topik terkait
 * @property viewCount Jumlah views
 */
data class NewsDetail(
    val article: NewsArticle,
    val content: String,
    val relatedTopics: List<String>,
    val viewCount: Int
)

/**
 * Data class untuk format tampilan berita di feed.
 *
 * @property displayText Teks yang sudah diformat untuk ditampilkan
 * @property isHighPriority Apakah berita ini prioritas tinggi
 */
data class FormattedNews(
    val displayText: String,
    val isHighPriority: Boolean
)
