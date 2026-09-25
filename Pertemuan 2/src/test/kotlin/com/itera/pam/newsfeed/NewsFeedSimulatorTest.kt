package com.itera.pam.newsfeed

import com.itera.pam.newsfeed.data.NewsRepository
import com.itera.pam.newsfeed.manager.NewsFeedManager
import com.itera.pam.newsfeed.model.NewsCategory
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.launch
import kotlin.test.*

/**
 * Unit tests untuk News Feed Simulator.
 *
 * Menggunakan kotlinx-coroutines-test untuk testing Flow dan Coroutines.
 * Tests ini memberikan bonus +10% pada nilai tugas.
 */
class NewsFeedSimulatorTest {

    private lateinit var repository: NewsRepository
    private lateinit var feedManager: NewsFeedManager

    @BeforeTest
    fun setup() {
        repository = NewsRepository()
        feedManager = NewsFeedManager(repository)
    }

    // ==========================================
    // TESTS UNTUK FLOW
    // ==========================================

    @Test
    fun `Flow harus memancarkan berita secara berurutan`() = runTest {
        val articles = repository.getNewsFeed()
            .take(3)
            .toList()

        assertEquals(3, articles.size, "Harus ada 3 artikel yang di-emit")
        assertEquals(1, articles[0].id, "Artikel pertama harus memiliki ID 1")
        assertEquals(2, articles[1].id, "Artikel kedua harus memiliki ID 2")
        assertEquals(3, articles[2].id, "Artikel ketiga harus memiliki ID 3")
    }

    @Test
    fun `Flow filter harus menyaring berita berdasarkan kategori`() = runTest {
        val techArticles = feedManager.getFilteredNewsFeed(NewsCategory.TEKNOLOGI)
            .take(2)
            .toList()

        assertTrue(
            techArticles.all { it.displayText.contains("Teknologi") },
            "Semua berita harus berkategori Teknologi"
        )
    }

    @Test
    fun `Flow tanpa filter harus menampilkan semua kategori`() = runTest {
        val allArticles = feedManager.getFilteredNewsFeed(null)
            .take(5)
            .toList()

        assertEquals(5, allArticles.size, "Harus ada 5 artikel tanpa filter")
    }

    @Test
    fun `Flow map harus mentransformasi data ke format tampilan`() = runTest {
        val formattedNews = feedManager.getFilteredNewsFeed()
            .take(1)
            .first()

        assertTrue(
            formattedNews.displayText.isNotBlank(),
            "Display text tidak boleh kosong"
        )
        assertTrue(
            formattedNews.displayText.contains("📰") || formattedNews.displayText.contains("⚡"),
            "Harus ada emoji indikator prioritas"
        )
    }

    @Test
    fun `Berita Teknologi dan Sains harus high priority`() = runTest {
        val techNews = feedManager.getFilteredNewsFeed(NewsCategory.TEKNOLOGI)
            .take(1)
            .first()

        assertTrue(techNews.isHighPriority, "Berita Teknologi harus high priority")

        val scienceNews = feedManager.getFilteredNewsFeed(NewsCategory.SAINS)
            .take(1)
            .first()

        assertTrue(scienceNews.isHighPriority, "Berita Sains harus high priority")
    }

    @Test
    fun `Berita Olahraga tidak high priority`() = runTest {
        val sportsNews = feedManager.getFilteredNewsFeed(NewsCategory.OLAHRAGA)
            .take(1)
            .first()

        assertFalse(sportsNews.isHighPriority, "Berita Olahraga tidak boleh high priority")
    }

    // ==========================================
    // TESTS UNTUK STATEFLOW
    // ==========================================

    @Test
    fun `StateFlow readCount harus dimulai dari 0`() = runTest {
        assertEquals(0, feedManager.readCount.value, "Read count awal harus 0")
    }

    @Test
    fun `markAsRead harus menambah readCount`() = runTest {
        feedManager.markAsRead(1)
        assertEquals(1, feedManager.readCount.value, "Read count harus 1 setelah baca 1 berita")

        feedManager.markAsRead(2)
        assertEquals(2, feedManager.readCount.value, "Read count harus 2 setelah baca 2 berita")

        feedManager.markAsRead(3)
        assertEquals(3, feedManager.readCount.value, "Read count harus 3 setelah baca 3 berita")
    }

    @Test
    fun `markAsRead tidak boleh menghitung duplikat`() = runTest {
        feedManager.markAsRead(1)
        feedManager.markAsRead(1) // duplikat
        feedManager.markAsRead(1) // duplikat

        assertEquals(1, feedManager.readCount.value, "Read count tidak boleh bertambah untuk duplikat")
    }

    @Test
    fun `readArticleIds harus menyimpan ID yang sudah dibaca`() = runTest {
        feedManager.markAsRead(1)
        feedManager.markAsRead(5)
        feedManager.markAsRead(10)

        val readIds = feedManager.readArticleIds.value
        assertTrue(readIds.contains(1), "Harus berisi ID 1")
        assertTrue(readIds.contains(5), "Harus berisi ID 5")
        assertTrue(readIds.contains(10), "Harus berisi ID 10")
        assertEquals(3, readIds.size, "Harus ada 3 ID unik")
    }

    @Test
    fun `resetState harus mengembalikan semua state ke awal`() = runTest {
        // Setup: tambah beberapa state
        feedManager.markAsRead(1)
        feedManager.markAsRead(2)
        feedManager.setFilter(NewsCategory.TEKNOLOGI)

        // Reset
        feedManager.resetState()

        // Verifikasi
        assertEquals(0, feedManager.readCount.value, "Read count harus 0 setelah reset")
        assertTrue(feedManager.readArticleIds.value.isEmpty(), "Read IDs harus kosong setelah reset")
        assertNull(feedManager.activeFilter.value, "Filter harus null setelah reset")
    }

    @Test
    fun `setFilter harus mengubah filter aktif`() = runTest {
        assertNull(feedManager.activeFilter.value, "Filter awal harus null")

        feedManager.setFilter(NewsCategory.OLAHRAGA)
        assertEquals(NewsCategory.OLAHRAGA, feedManager.activeFilter.value, "Filter harus OLAHRAGA")

        feedManager.setFilter(null)
        assertNull(feedManager.activeFilter.value, "Filter harus null setelah di-reset")
    }

    @Test
    fun `StateFlow harus emit update ke collector`() = runTest {
        val collectedValues = mutableListOf<Int>()

        val job = launch {
            feedManager.readCount
                .take(4) // Initial (0) + 3 updates
                .toList(collectedValues)
        }

        feedManager.markAsRead(1)
        feedManager.markAsRead(2)
        feedManager.markAsRead(3)

        job.join()

        assertEquals(listOf(0, 1, 2, 3), collectedValues, "StateFlow harus emit 0, 1, 2, 3")
    }

    // ==========================================
    // TESTS UNTUK COROUTINES
    // ==========================================

    @Test
    fun `fetchNewsDetail harus mengembalikan detail yang benar`() = runTest {
        val detail = repository.fetchNewsDetail(1)

        assertNotNull(detail, "Detail tidak boleh null untuk ID valid")
        assertEquals(1, detail.article.id, "ID artikel harus 1")
        assertTrue(detail.content.isNotBlank(), "Content tidak boleh kosong")
        assertTrue(detail.relatedTopics.isNotEmpty(), "Related topics tidak boleh kosong")
        assertTrue(detail.viewCount >= 100, "View count minimal 100")
    }

    @Test
    fun `fetchNewsDetail harus return null untuk ID invalid`() = runTest {
        val detail = repository.fetchNewsDetail(999)

        assertNull(detail, "Detail harus null untuk ID yang tidak ada")
    }

    @Test
    fun `fetchMultipleNewsDetails harus mengembalikan beberapa detail`() = runTest {
        val details = repository.fetchMultipleNewsDetails(listOf(1, 3, 5))

        assertEquals(3, details.size, "Harus ada 3 detail berita")
        assertTrue(details.any { it.article.id == 1 }, "Harus berisi detail untuk ID 1")
        assertTrue(details.any { it.article.id == 3 }, "Harus berisi detail untuk ID 3")
        assertTrue(details.any { it.article.id == 5 }, "Harus berisi detail untuk ID 5")
    }

    @Test
    fun `parallel fetch harus mengembalikan hasil yang benar`() = runTest {
        val articleIds = listOf(1, 5, 10)
        val details = feedManager.getMultipleNewsDetailsParallel(this, articleIds)

        assertEquals(3, details.size, "Harus ada 3 detail dari fetch paralel")
    }

    @Test
    fun `related topics harus sesuai dengan kategori`() = runTest {
        val techDetail = repository.fetchNewsDetail(1) // Teknologi
        assertNotNull(techDetail)
        assertTrue(
            techDetail.relatedTopics.contains("Programming"),
            "Topik terkait Teknologi harus berisi 'Programming'"
        )

        val sportDetail = repository.fetchNewsDetail(2) // Olahraga
        assertNotNull(sportDetail)
        assertTrue(
            sportDetail.relatedTopics.contains("Sepak Bola"),
            "Topik terkait Olahraga harus berisi 'Sepak Bola'"
        )
    }

    // ==========================================
    // TESTS UNTUK ERROR HANDLING
    // ==========================================

    @Test
    fun `NewsCategory enum harus memiliki display name dan emoji`() {
        NewsCategory.entries.forEach { category ->
            assertTrue(category.displayName.isNotBlank(), "Display name tidak boleh kosong")
            assertTrue(category.emoji.isNotBlank(), "Emoji tidak boleh kosong")
            assertTrue(category.toString().contains(category.displayName), "toString harus berisi display name")
        }
    }

    @Test
    fun `NewsCategory harus memiliki 5 kategori`() {
        assertEquals(5, NewsCategory.entries.size, "Harus ada 5 kategori")
    }
}
