package com.itera.pam.myprofile.model

/**
 * Data class Product sesuai spesifikasi Latihan 3 pada slide 32
 */
data class Product(
    val name: String,
    val price: String,
    val category: String,
    val description: String,
    val rating: Double = 4.8
)
