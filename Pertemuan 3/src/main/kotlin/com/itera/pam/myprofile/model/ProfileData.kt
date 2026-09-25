package com.itera.pam.myprofile.model

import androidx.compose.ui.graphics.vector.ImageVector

/**
 * Data model untuk item informasi profil (Email, Telepon, Lokasi, dsb.)
 */
data class ProfileInfoItemData(
    val id: String,
    val icon: ImageVector,
    val label: String,
    val value: String,
    val actionHint: String = "Salin"
)

/**
 * Data model untuk metrik statistik akademik mahasiswa
 */
data class AcademicMetric(
    val label: String,
    val value: String,
    val subtext: String
)

/**
 * Data model utama yang memuat seluruh informasi profil mahasiswa ITERA
 */
data class StudentProfile(
    val name: String,
    val nim: String,
    val programStudy: String,
    val institution: String,
    val roleTitle: String,
    val statusText: String,
    val bio: String,
    val email: String,
    val phone: String,
    val location: String,
    val githubUrl: String,
    val linkedinUrl: String,
    val skills: List<String>,
    val metrics: List<AcademicMetric>,
    val courses: List<String>
)
