package com.itera.pam.myprofile

import com.itera.pam.myprofile.data.DummyData
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class ProfileTest {

    @Test
    fun testStudentProfileDataIntegrity() {
        val profile = DummyData.sampleProfile
        assertEquals("Muhammad Fatahillah Farid", profile.name)
        assertEquals("123140203", profile.nim)
        assertTrue(profile.email.endsWith("@student.itera.ac.id"))
        assertTrue(profile.nim.startsWith("12314"))
        assertTrue(profile.skills.isNotEmpty())
        assertTrue(profile.skills.contains("Compose Multiplatform"))
        assertTrue(profile.skills.contains("Kotlin"))
    }

    @Test
    fun testProfileInfoItemsGeneration() {
        val profile = DummyData.sampleProfile
        val items = DummyData.getProfileInfoItems(profile)
        assertEquals(6, items.size)
        assertTrue(items.any { it.id == "nim" && it.value == "123140203" })
        assertTrue(items.any { it.id == "email" && it.value.contains("itera.ac.id") })
        assertTrue(items.any { it.id == "phone" })
        assertTrue(items.any { it.id == "location" })
    }

    @Test
    fun testProductsData() {
        val products = DummyData.sampleProducts
        assertTrue(products.isNotEmpty())
        products.forEach { product ->
            assertFalse(product.name.isBlank())
            assertTrue(product.price.startsWith("Rp"))
            assertTrue(product.rating in 0.0..5.0)
        }
    }
}
