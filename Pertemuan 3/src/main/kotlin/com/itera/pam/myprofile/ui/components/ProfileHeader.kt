package com.itera.pam.myprofile.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Verified
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.itera.pam.myprofile.ui.theme.AccentGreen
import com.itera.pam.myprofile.ui.theme.PrimaryIndigo
import com.itera.pam.myprofile.ui.theme.SecondaryTeal

/**
 * Reusable Composable: ProfileHeader
 * Memenuhi kriteria tugas: Header dengan foto profil circular, nama, dan role status
 * Menggunakan kombinasi Box, Column, Row, Text, dan Icon
 */
@Composable
fun ProfileHeader(
    name: String,
    nim: String,
    roleTitle: String,
    institution: String,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxWidth()
            .padding(top = 16.dp, bottom = 12.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        // Box Layout: Avatar Container dengan Status Indicator
        Box(
            contentAlignment = Alignment.BottomEnd,
            modifier = Modifier.size(112.dp)
        ) {
            // Layer 1: Circular Avatar dengan Gradient & Shadow
            Box(
                modifier = Modifier
                    .size(108.dp)
                    .shadow(elevation = 8.dp, shape = CircleShape)
                    .clip(CircleShape)
                    .background(
                        brush = Brush.linearGradient(
                            colors = listOf(
                                PrimaryIndigo,
                                SecondaryTeal
                            )
                        )
                    )
                    .border(
                        width = 3.dp,
                        color = MaterialTheme.colorScheme.surface,
                        shape = CircleShape
                    ),
                contentAlignment = Alignment.Center
            ) {
                // Inisial / Monogram Avatar Mahasiswa
                Text(
                    text = "MF",
                    fontSize = 36.sp,
                    fontWeight = FontWeight.ExtraBold,
                    color = Color.White,
                    letterSpacing = 1.sp
                )
            }

            // Layer 2: Online / Active Status Badge Indicator
            Box(
                modifier = Modifier
                    .size(26.dp)
                    .clip(CircleShape)
                    .background(MaterialTheme.colorScheme.surface)
                    .padding(3.dp)
            ) {
                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .clip(CircleShape)
                        .background(AccentGreen)
                )
            }
        }

        Spacer(modifier = Modifier.height(4.dp))

        // Row Layout: Nama Mahasiswa dan Badge Terverifikasi
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            Text(
                text = name,
                style = MaterialTheme.typography.headlineSmall,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.onSurface,
                textAlign = TextAlign.Center
            )
            Icon(
                imageVector = Icons.Default.Verified,
                contentDescription = "Verified Student",
                tint = MaterialTheme.colorScheme.primary,
                modifier = Modifier.size(20.dp)
            )
        }

        // Subtitle: NIM & Institusi Kampus
        Text(
            text = "NIM: $nim • $institution",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.Medium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            textAlign = TextAlign.Center
        )

        // Chip Status / Peran
        Surface(
            shape = RoundedCornerShape(16.dp),
            color = MaterialTheme.colorScheme.primaryContainer,
            modifier = Modifier.padding(top = 4.dp)
        ) {
            Text(
                text = roleTitle,
                style = MaterialTheme.typography.labelMedium,
                fontWeight = FontWeight.SemiBold,
                color = MaterialTheme.colorScheme.onPrimaryContainer,
                modifier = Modifier.padding(horizontal = 14.dp, vertical = 6.dp)
            )
        }
    }
}
