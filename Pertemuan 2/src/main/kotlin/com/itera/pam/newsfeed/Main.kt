package com.itera.pam.newsfeed

import com.itera.pam.newsfeed.data.NewsRepository
import com.itera.pam.newsfeed.manager.NewsFeedManager
import com.itera.pam.newsfeed.model.NewsCategory
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

/**
 * News Feed Simulator - Aplikasi Utama
 *
 * Tugas Praktikum Pertemuan 2: Advanced Kotlin, Coroutines, dan Flow
 * Mata Kuliah: Pengembangan Aplikasi Mobile (PAM)
 * Institut Teknologi Sumatera (ITERA)
 *
 * Nama  : Muhammad Fatahillah Farid
 * NIM   : 123140203
 *
 * Fitur yang diimplementasikan:
 * 1. Flow yang mensimulasikan data berita baru setiap 2 detik
 * 2. Filter berita berdasarkan kategori tertentu
 * 3. Transform data menjadi format yang ditampilkan
 * 4. StateFlow untuk menyimpan jumlah berita yang sudah dibaca
 * 5. Coroutines untuk mengambil detail berita secara async
 */

fun main() = runBlocking {
    val repository = NewsRepository()
    val feedManager = NewsFeedManager(repository)

    printHeader()

    // ============================================================
    // DEMO 1: Flow + Filter + Transform (Semua Kategori)
    // ============================================================
    println("\n${"=".repeat(60)}")
    println("📡 DEMO 1: News Feed - Semua Kategori (5 berita pertama)")
    println("${"=".repeat(60)}")
    println("Flow memancarkan berita baru setiap 2 detik...\n")

    feedManager.getFilteredNewsFeed()     // Flow tanpa filter
        .take(5)                          // Ambil 5 berita pertama
        .collect { formattedNews ->
            println(formattedNews.displayText)
            // Simulasi: tandai berita sebagai sudah dibaca
            feedManager.markAsRead((1..15).random())
        }

    println("📊 Jumlah berita dibaca sejauh ini: ${feedManager.readCount.value}")

    // ============================================================
    // DEMO 2: Flow + Filter Kategori Tertentu (TEKNOLOGI)
    // ============================================================
    println("\n${"=".repeat(60)}")
    println("🔍 DEMO 2: News Feed - Filter Kategori TEKNOLOGI")
    println("${"=".repeat(60)}")
    println("Hanya menampilkan berita kategori Teknologi...\n")

    feedManager.getFilteredNewsFeed(NewsCategory.TEKNOLOGI)
        .take(3)                          // Ambil 3 berita teknologi
        .collect { formattedNews ->
            println(formattedNews.displayText)
            feedManager.markAsRead((1..15).random())
        }

    println("📊 Total berita dibaca: ${feedManager.readCount.value}")

    // ============================================================
    // DEMO 3: Flow + Filter Kategori Tertentu (SAINS)
    // ============================================================
    println("\n${"=".repeat(60)}")
    println("🔬 DEMO 3: News Feed - Filter Kategori SAINS")
    println("${"=".repeat(60)}")
    println("Hanya menampilkan berita kategori Sains...\n")

    feedManager.getFilteredNewsFeed(NewsCategory.SAINS)
        .take(2)                          // Ambil 2 berita sains
        .collect { formattedNews ->
            println(formattedNews.displayText)
            feedManager.markAsRead((1..15).random())
        }

    println("📊 Total berita dibaca: ${feedManager.readCount.value}")

    // ============================================================
    // DEMO 4: StateFlow - Monitoring Jumlah Berita Dibaca
    // ============================================================
    println("\n${"=".repeat(60)}")
    println("📈 DEMO 4: StateFlow - Monitoring Read Count")
    println("${"=".repeat(60)}")

    // Launch collector di background untuk mengamati perubahan StateFlow
    val stateFlowJob = launch {
        feedManager.readCount.collect { count ->
            println("   [StateFlow Update] 📖 Berita dibaca: $count")
        }
    }

    // Simulasi membaca beberapa berita
    println("Simulasi membaca berita satu per satu...\n")
    delay(300)
    feedManager.markAsRead(1)
    delay(300)
    feedManager.markAsRead(3)
    delay(300)
    feedManager.markAsRead(5)
    delay(300)
    feedManager.markAsRead(7)
    delay(300)

    // Cancel collector setelah demo selesai
    stateFlowJob.cancel()

    println("\n   ✅ StateFlow berhasil memantau perubahan state secara reaktif!")

    // ============================================================
    // DEMO 5: Coroutines Async - Mengambil Detail Berita Paralel
    // ============================================================
    println("\n${"=".repeat(60)}")
    println("⚡ DEMO 5: Coroutines Async - Fetch Detail Berita Paralel")
    println("${"=".repeat(60)}")

    val articleIds = listOf(1, 5, 10)
    println("Mengambil detail untuk berita ID: $articleIds secara PARALEL...\n")

    val startTime = System.currentTimeMillis()

    // Menggunakan async/await untuk mengambil detail secara paralel
    val details = feedManager.getMultipleNewsDetailsParallel(this, articleIds)

    val endTime = System.currentTimeMillis()

    details.forEach { detail ->
        println("─".repeat(50))
        println("📰 ${detail.article.title}")
        println("   ${detail.article.category} | 👁️ ${detail.viewCount} views")
        println("   🏷️ Topik terkait: ${detail.relatedTopics.joinToString(", ")}")
    }

    println("\n⏱️ Waktu eksekusi paralel: ${endTime - startTime}ms")
    println("   (Sequential ~${articleIds.size * 1000}ms, Paralel lebih cepat!)")

    // ============================================================
    // DEMO 6: Coroutines Async - Fetch Detail Tunggal
    // ============================================================
    println("\n${"=".repeat(60)}")
    println("🔎 DEMO 6: Coroutines - Fetch Detail Berita Tunggal")
    println("${"=".repeat(60)}")

    val singleStartTime = System.currentTimeMillis()
    val singleDetail = feedManager.getNewsDetail(6)
    val singleEndTime = System.currentTimeMillis()

    if (singleDetail != null) {
        println("\n${singleDetail.content}")
        println("\n   👁️ Views: ${singleDetail.viewCount}")
        println("   🏷️ Topik terkait: ${singleDetail.relatedTopics.joinToString(", ")}")
        println("   ⏱️ Waktu fetch: ${singleEndTime - singleStartTime}ms")
    }

    // ============================================================
    // RINGKASAN AKHIR
    // ============================================================
    printSummary(feedManager)
}

/**
 * Menampilkan header aplikasi.
 */
fun printHeader() {
    val header = """
    |
    |╔══════════════════════════════════════════════════════════════╗
    |║                                                            ║
    |║       📰  NEWS FEED SIMULATOR  📰                         ║
    |║                                                            ║
    |║   Tugas Praktikum PAM - Pertemuan 2                        ║
    |║   Advanced Kotlin, Coroutines, dan Flow                    ║
    |║                                                            ║
    |║   Nama : Muhammad Fatahillah Farid                         ║
    |║   NIM  : 123140203                                         ║
    |║   Prodi: Teknik Informatika - ITERA                        ║
    |║                                                            ║
    |╚══════════════════════════════════════════════════════════════╝
    """.trimMargin()
    println(header)
}

/**
 * Menampilkan ringkasan akhir aplikasi.
 */
fun printSummary(feedManager: NewsFeedManager) {
    val summary = """
    |
    |╔══════════════════════════════════════════════════════════════╗
    |║                   📊 RINGKASAN AKHIR                       ║
    |╠══════════════════════════════════════════════════════════════╣
    |║                                                            ║
    |║  Total berita dibaca : ${feedManager.readCount.value.toString().padEnd(35)}║
    |║  ID berita dibaca    : ${feedManager.readArticleIds.value.toString().padEnd(35)}║
    |║                                                            ║
    |║  ✅ Fitur yang diimplementasikan:                          ║
    |║     1. Flow (emit berita setiap 2 detik)                   ║
    |║     2. Filter (berdasarkan kategori)                       ║
    |║     3. Transform (map ke format tampilan)                  ║
    |║     4. StateFlow (tracking berita dibaca)                  ║
    |║     5. Coroutines async (fetch detail paralel)             ║
    |║     6. Error handling (.catch operator)                    ║
    |║                                                            ║
    |╚══════════════════════════════════════════════════════════════╝
    """.trimMargin()
    println(summary)
}
