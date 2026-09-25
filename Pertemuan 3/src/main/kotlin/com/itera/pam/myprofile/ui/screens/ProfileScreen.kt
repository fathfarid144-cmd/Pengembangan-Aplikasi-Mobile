package com.itera.pam.myprofile.ui.screens

import androidx.compose.animation.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.itera.pam.myprofile.data.DummyData
import com.itera.pam.myprofile.model.StudentProfile
import com.itera.pam.myprofile.ui.components.*
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

/**
 * Halaman Utama: ProfileScreen (My Profile App)
 * Memenuhi seluruh spesifikasi Tugas Praktikum Minggu 3:
 * 1. Halaman Profile dengan Header foto circular, nama, bio, dan list info kontak
 * 2. Menggunakan minimal 3 reusable composables: ProfileHeader, InfoItem, ProfileCard, dsb.
 * 3. Menggunakan Column, Row, Box, Card, Text, Button, Image/Icon
 * 4. Bonus (+10%): Animasi AnimatedVisibility pada ekspansi detail dan toast feedback interaktif
 */
@Composable
fun ProfileScreen(
    profile: StudentProfile = DummyData.sampleProfile,
    modifier: Modifier = Modifier
) {
    val scrollState = rememberScrollState()
    val coroutineScope = rememberCoroutineScope()

    // State untuk feedback toast pesan/aksi
    var feedbackMessage by remember { mutableStateOf<String?>(null) }
    var selectedSkill by remember { mutableStateOf<String?>(null) }

    fun showToast(msg: String) {
        feedbackMessage = msg
        coroutineScope.launch {
            delay(2800)
            if (feedbackMessage == msg) {
                feedbackMessage = null
            }
        }
    }

    Box(
        modifier = modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {
        // Konten Profil Utama dengan Smooth Scroll
        Column(
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(scrollState)
                .padding(horizontal = 20.dp, vertical = 16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // 1. REUSABLE COMPOSABLE: ProfileHeader (Header foto circular, nama, NIM)
            ProfileHeader(
                name = profile.name,
                nim = profile.nim,
                roleTitle = profile.roleTitle,
                institution = profile.institution
            )

            // 2. METRIK AKADEMIK (Row Layout of Cards)
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                profile.metrics.forEach { metric ->
                    StatisticCard(
                        metric = metric,
                        modifier = Modifier.weight(1f)
                    )
                }
            }

            // 3. REUSABLE COMPOSABLE: ProfileCard (Bio / Deskripsi Singkat)
            ProfileCard(
                title = "Tentang Saya (Bio)",
                icon = Icons.Default.Person
            ) {
                Text(
                    text = profile.bio,
                    style = MaterialTheme.typography.bodyMedium,
                    lineHeight = MaterialTheme.typography.bodyMedium.lineHeight,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }

            // 4. REUSABLE COMPOSABLE: ProfileCard + InfoItem (List Informasi: Email, Phone, Location)
            ProfileCard(
                title = "Informasi Kontak & Mahasiswa",
                icon = Icons.Default.ContactMail
            ) {
                Column(
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    val infoList = DummyData.getProfileInfoItems(profile)
                    infoList.forEach { info ->
                        InfoItem(
                            icon = info.icon,
                            label = info.label,
                            value = info.value,
                            actionHint = info.actionHint,
                            onActionClick = {
                                showToast("${info.label} (${info.value}) berhasil disalin!")
                            }
                        )
                    }
                }
            }

            // 5. KEAHLIAN & TEKNOLOGI (Skill Badges)
            ProfileCard(
                title = "Keahlian & Teknologi (Skills)",
                icon = Icons.Default.Code
            ) {
                Text(
                    text = "Klik badge untuk memfilter fokus keahlian:",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(bottom = 10.dp)
                )

                // Layout Fleksibel Keahlian dalam Baris-Baris
                Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    val chunkedSkills = profile.skills.chunked(3)
                    chunkedSkills.forEach { rowSkills ->
                        Row(
                            horizontalArrangement = Arrangement.spacedBy(8.dp),
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            rowSkills.forEach { skill ->
                                SkillBadge(
                                    skill = skill,
                                    isSelected = (selectedSkill == skill),
                                    onClick = {
                                        selectedSkill = if (selectedSkill == skill) null else skill
                                        showToast("Fokus teknologi: $skill")
                                    }
                                )
                            }
                        }
                    }
                }
            }

            // 6. BONUS COMPOSABLE: AcademicDetailsSection (AnimatedVisibility)
            AcademicDetailsSection(
                courses = profile.courses
            )

            // 7. TOMBOL AKSI UTAMA (Button & OutlinedButton)
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 8.dp),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                Button(
                    onClick = {
                        showToast("Membuka form kontak ke ${profile.email}")
                    },
                    modifier = Modifier.weight(1f),
                    shape = RoundedCornerShape(12.dp)
                ) {
                    Icon(
                        imageVector = Icons.Default.Email,
                        contentDescription = "Hubungi",
                        modifier = Modifier.size(18.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text("Hubungi Saya")
                }

                OutlinedButton(
                    onClick = {
                        showToast("Profil ${profile.name} (NIM: ${profile.nim}) berhasil disalin!")
                    },
                    modifier = Modifier.weight(1f),
                    shape = RoundedCornerShape(12.dp)
                ) {
                    Icon(
                        imageVector = Icons.Default.Share,
                        contentDescription = "Bagikan",
                        modifier = Modifier.size(18.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text("Bagikan Profil")
                }
            }

            // Footer Penanda Praktikum ITERA
            Text(
                text = "Praktikum Pengembangan Aplikasi Mobile • ITERA 2026",
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.6f),
                modifier = Modifier.padding(bottom = 24.dp)
            )
        }

        // 8. INTERACTIVE TOAST FEEDBACK: Menggunakan AnimatedVisibility
        AnimatedVisibility(
            visible = feedbackMessage != null,
            enter = slideInVertically(initialOffsetY = { it }) + fadeIn(),
            exit = slideOutVertically(targetOffsetY = { it }) + fadeOut(),
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .padding(bottom = 24.dp)
        ) {
            feedbackMessage?.let { msg ->
                Surface(
                    shape = RoundedCornerShape(24.dp),
                    color = MaterialTheme.colorScheme.inverseSurface,
                    shadowElevation = 8.dp,
                    modifier = Modifier.padding(horizontal = 24.dp)
                ) {
                    Row(
                        modifier = Modifier.padding(horizontal = 18.dp, vertical = 10.dp),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        Icon(
                            imageVector = Icons.Default.Info,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.inverseOnSurface,
                            modifier = Modifier.size(18.dp)
                        )
                        Text(
                            text = msg,
                            style = MaterialTheme.typography.bodyMedium,
                            fontWeight = FontWeight.Medium,
                            color = MaterialTheme.colorScheme.inverseOnSurface
                        )
                    }
                }
            }
        }
    }
}
