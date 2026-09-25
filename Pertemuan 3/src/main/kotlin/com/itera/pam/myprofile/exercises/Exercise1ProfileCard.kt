package com.itera.pam.myprofile.exercises

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.itera.pam.myprofile.ui.theme.PrimaryIndigo
import com.itera.pam.myprofile.ui.theme.SecondaryTeal

/**
 * LATIHAN 1: PROFILE CARD (Slide 30 Modul Praktikum)
 * Buat komponen ProfileCard dengan foto circular, nama, dan bio.
 * Checklist yang dipenuhi:
 * [x] Avatar (circular image / monogram)
 * [x] Nama (bold)
 * [x] Bio (gray color)
 * [x] Card dengan elevasi
 * [x] Padding yang rapi
 */
@Composable
fun Exercise1ProfileCard(
    name: String = "John Doe",
    bio: String = "Mobile Developer",
    avatarInitial: String = "JD",
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier
            .fillMaxWidth()
            .padding(16.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 4.dp),
        shape = RoundedCornerShape(12.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface)
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Avatar (circular container)
            Box(
                modifier = Modifier
                    .size(56.dp)
                    .clip(CircleShape)
                    .background(PrimaryIndigo)
                    .border(2.dp, SecondaryTeal, CircleShape),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = avatarInitial,
                    color = Color.White,
                    fontWeight = FontWeight.Bold,
                    fontSize = 20.sp
                )
            }

            // Column untuk name dan bio
            Column(
                verticalArrangement = Arrangement.Center
            ) {
                Text(
                    text = name,
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.Bold,
                    color = MaterialTheme.colorScheme.onSurface
                )
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = bio,
                    style = MaterialTheme.typography.bodyMedium,
                    color = Color.Gray
                )
            }
        }
    }
}
