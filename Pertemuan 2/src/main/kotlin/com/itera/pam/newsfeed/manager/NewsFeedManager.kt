package com.itera.pam.newsfeed.manager

import com.itera.pam.newsfeed.data.NewsRepository
import com.itera.pam.newsfeed.model.*
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

/**
 * Manager yang mengelola state dan logika bisnis News Feed.
 *
 * Menggunakan StateFlow untuk state management dan Flow operators
 * untuk transformasi dan filtering data berita.
 *
 * @property repository Sumber data berita
 */
class NewsFeedManager(private val repository: NewsRepository) {

    // ==========================================
    // STATE MANAGEMENT DENGAN STATEFLOW
    // ==========================================

    /**
     * MutableStateFlow untuk menyimpan jumlah berita yang sudah dibaca.
     * Private agar hanya bisa diubah dari dalam kelas ini.
     */
    private val _readCount = MutableStateFlow(0)

    /**
     * StateFlow publik (read-only) yang di-expose ke luar.
     * Collector bisa mengamati perubahan jumlah berita yang dibaca.
     */
    val readCount: StateFlow<Int> = _readCount.asStateFlow()

    /**
     * MutableStateFlow untuk menyimpan daftar ID berita yang sudah dibaca.
     */
    private val _readArticleIds = MutableStateFlow<Set<Int>>(emptySet())

    /**
     * StateFlow publik untuk daftar ID berita yang sudah dibaca.
     */
    val readArticleIds: StateFlow<Set<Int>> = _readArticleIds.asStateFlow()

    /**
     * MutableStateFlow untuk menyimpan kategori filter aktif.
     * null berarti tidak ada filter (tampilkan semua).
     */
    private val _activeFilter = MutableStateFlow<NewsCategory?>(null)

    /**
     * StateFlow publik untuk kategori filter aktif.
     */
    val activeFilter: StateFlow<NewsCategory?> = _activeFilter.asStateFlow()

    // ==========================================
    // FLOW OPERATIONS
    // ==========================================

    /**
     * Mendapatkan stream berita yang sudah difilter dan diformat.
     *
     * Menggunakan Flow operators:
     * - filter: Menyaring berita berdasarkan kategori
     * - map: Mentransformasi data menjadi format tampilan
     * - onEach: Side effect untuk logging
     * - catch: Error handling
     *
     * @param category Kategori filter (null = semua kategori)
     * @return Flow<FormattedNews> stream berita yang sudah diformat
     */
    fun getFilteredNewsFeed(category: NewsCategory? = null): Flow<FormattedNews> {
        return repository.getNewsFeed()
            // 1. FILTER: Saring berita berdasarkan kategori tertentu
            .filter { article ->
                category == null || article.category == category
            }
            // 2. TRANSFORM (map): Ubah data menjadi format yang ditampilkan
            .map { article ->
                transformToDisplayFormat(article)
            }
            // 3. SIDE EFFECT (onEach): Logging setiap berita yang masuk
            .onEach { formattedNews ->
                println("   [LOG] Berita baru diproses: ${if (formattedNews.isHighPriority) "⚡ PRIORITAS TINGGI" else "📰 Normal"}")
            }
            // 4. ERROR HANDLING (catch): Tangani error dalam flow
            .catch { exception ->
                println("   [ERROR] Terjadi kesalahan: ${exception.message}")
                // Emit berita fallback saat terjadi error
                emit(FormattedNews(
                    displayText = "⚠️ Gagal memuat berita. Silakan coba lagi.",
                    isHighPriority = false
                ))
            }
    }

    /**
     * Menandai berita sebagai sudah dibaca dan update StateFlow counter.
     *
     * @param articleId ID berita yang dibaca
     */
    fun markAsRead(articleId: Int) {
        val currentIds = _readArticleIds.value.toMutableSet()
        if (currentIds.add(articleId)) {
            _readArticleIds.value = currentIds
            _readCount.value = currentIds.size
        }
    }

    /**
     * Mengatur filter kategori aktif.
     *
     * @param category Kategori yang ingin difilter (null = semua)
     */
    fun setFilter(category: NewsCategory?) {
        _activeFilter.value = category
    }

    /**
     * Mereset semua state ke kondisi awal.
     */
    fun resetState() {
        _readCount.value = 0
        _readArticleIds.value = emptySet()
        _activeFilter.value = null
    }

    /**
     * Mengambil detail berita secara async menggunakan coroutines.
     *
     * @param articleId ID artikel
     * @return NewsDetail atau null
     */
    suspend fun getNewsDetail(articleId: Int): NewsDetail? {
        return repository.fetchNewsDetail(articleId)
    }

    /**
     * Mengambil detail beberapa berita secara paralel menggunakan async/await.
     *
     * @param scope CoroutineScope untuk menjalankan operasi async
     * @param articleIds Daftar ID berita
     * @return List<NewsDetail> detail berita
     */
    suspend fun getMultipleNewsDetailsParallel(
        scope: CoroutineScope,
        articleIds: List<Int>
    ): List<NewsDetail> {
        // Menggunakan async/await untuk mengambil detail secara PARALEL
        val deferredResults = articleIds.map { id ->
            scope.async {
                repository.fetchNewsDetail(id)
            }
        }

        // Tunggu semua hasil dengan await dan filter null
        return deferredResults.awaitAll().filterNotNull()
    }

    // ==========================================
    // HELPER / PRIVATE FUNCTIONS
    // ==========================================

    /**
     * Mentransformasi NewsArticle ke format tampilan FormattedNews.
     *
     * @param article Artikel berita asli
     * @return FormattedNews berita yang sudah diformat
     */
    private fun transformToDisplayFormat(article: NewsArticle): FormattedNews {
        val isHighPriority = article.category == NewsCategory.TEKNOLOGI ||
                article.category == NewsCategory.SAINS

        val priorityIndicator = if (isHighPriority) "⚡" else "📰"
        val separator = "─".repeat(50)

        val displayText = buildString {
            appendLine(separator)
            appendLine("$priorityIndicator [${article.category}] ${article.title}")
            appendLine("   📝 ${article.summary}")
            appendLine("   ✍️  Oleh: ${article.author} | 🆔 ID: ${article.id}")
            appendLine(separator)
        }

        return FormattedNews(
            displayText = displayText,
            isHighPriority = isHighPriority
        )
    }
}
