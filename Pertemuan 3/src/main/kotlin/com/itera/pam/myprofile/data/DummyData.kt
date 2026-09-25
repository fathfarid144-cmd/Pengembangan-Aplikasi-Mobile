package com.itera.pam.myprofile.data

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Email
import androidx.compose.material.icons.filled.LocationOn
import androidx.compose.material.icons.filled.Phone
import androidx.compose.material.icons.filled.School
import androidx.compose.material.icons.filled.Code
import androidx.compose.material.icons.filled.Badge
import com.itera.pam.myprofile.model.AcademicMetric
import com.itera.pam.myprofile.model.Product
import com.itera.pam.myprofile.model.ProfileInfoItemData
import com.itera.pam.myprofile.model.StudentProfile

object DummyData {
    val sampleProfile = StudentProfile(
        name = "Muhammad Fatahillah Farid",
        nim = "123140203",
        programStudy = "Teknik Informatika (S1)",
        institution = "Institut Teknologi Sumatera (ITERA)",
        roleTitle = "Mobile & Multiplatform Developer",
        statusText = "Mahasiswa Aktif ITERA • Semester 7",
        bio = "Mahasiswa Teknik Informatika Institut Teknologi Sumatera (ITERA) yang memiliki passion mendalam di bidang Mobile Application Development, Compose Multiplatform, Kotlin Coroutines & Flow, serta Clean Architecture. Aktif membangun aplikasi modern dengan pendekatan deklaratif dan responsif.",
        email = "fatahillah.123140203@student.itera.ac.id",
        phone = "+62 821-8172-9014",
        location = "Lampung Selatan, Lampung, Indonesia",
        githubUrl = "https://github.com/fathfarid144-cmd",
        linkedinUrl = "https://linkedin.com/in/fatahillah-farid",
        skills = listOf(
            "Kotlin",
            "Jetpack Compose",
            "Compose Multiplatform",
            "Coroutines & Flow",
            "Material Design 3",
            "Android SDK",
            "Git & GitHub",
            "Clean Architecture"
        ),
        metrics = listOf(
            AcademicMetric("NIM", "123140203", "Angkatan 2023"),
            AcademicMetric("Semester", "7", "Tingkat Akhir"),
            AcademicMetric("Mata Kuliah", "PAM", "IF25-22017"),
            AcademicMetric("Status", "Aktif", "Genap 2025/2026")
        ),
        courses = listOf(
            "Pengembangan Aplikasi Mobile (PAM)",
            "Pemrograman Berorientasi Objek",
            "Struktur Data dan Algoritma",
            "Rekayasa Perangkat Lunak",
            "Interaksi Manusia dan Komputer",
            "Arsitektur Komputer & Jaringan"
        )
    )

    fun getProfileInfoItems(profile: StudentProfile): List<ProfileInfoItemData> {
        return listOf(
            ProfileInfoItemData(
                id = "nim",
                icon = Icons.Default.Badge,
                label = "Nomor Induk Mahasiswa (NIM)",
                value = profile.nim,
                actionHint = "Salin NIM"
            ),
            ProfileInfoItemData(
                id = "email",
                icon = Icons.Default.Email,
                label = "Email Akademik",
                value = profile.email,
                actionHint = "Kirim Email"
            ),
            ProfileInfoItemData(
                id = "phone",
                icon = Icons.Default.Phone,
                label = "Nomor Telepon / WhatsApp",
                value = profile.phone,
                actionHint = "Hubungi"
            ),
            ProfileInfoItemData(
                id = "location",
                icon = Icons.Default.LocationOn,
                label = "Domisili & Kampus",
                value = profile.location,
                actionHint = "Buka Peta"
            ),
            ProfileInfoItemData(
                id = "study",
                icon = Icons.Default.School,
                label = "Program Studi & Kampus",
                value = "${profile.programStudy}, ${profile.institution}",
                actionHint = "Info Kampus"
            ),
            ProfileInfoItemData(
                id = "github",
                icon = Icons.Default.Code,
                label = "Repositori GitHub",
                value = profile.githubUrl,
                actionHint = "Buka GitHub"
            )
        )
    }

    val sampleProducts = listOf(
        Product(
            name = "Android Studio Masterclass",
            price = "Rp 150.000",
            category = "Course",
            description = "E-Book panduan lengkap membangun aplikasi Android modern dari pemula hingga mahir dengan Jetpack Compose.",
            rating = 4.9
        ),
        Product(
            name = "Kotlin Multiplatform in Action",
            price = "Rp 250.000",
            category = "Book",
            description = "Buku panduan arsitektur single codebase untuk Android, iOS, Desktop, dan Web.",
            rating = 4.8
        ),
        Product(
            name = "Compose UI UI/UX Kit",
            price = "Rp 75.000",
            category = "Asset",
            description = "Kumpulan komponen Material 3 siap pakai dengan tema dark/light dan micro-interactions.",
            rating = 4.7
        ),
        Product(
            name = "ITERA Informatics Lanyard & Pin",
            price = "Rp 45.000",
            category = "Merchandise",
            description = "Merchandise resmi Teknik Informatika Institut Teknologi Sumatera (ITERA).",
            rating = 5.0
        )
    )
}
