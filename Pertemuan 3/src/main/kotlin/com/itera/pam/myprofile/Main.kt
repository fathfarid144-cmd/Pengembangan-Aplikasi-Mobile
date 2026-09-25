package com.itera.pam.myprofile

import androidx.compose.animation.Crossfade
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.DpSize
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.WindowPosition
import androidx.compose.ui.window.application
import androidx.compose.ui.window.rememberWindowState
import com.itera.pam.myprofile.exercises.Exercise1ProfileCard
import com.itera.pam.myprofile.exercises.Exercise2LoginForm
import com.itera.pam.myprofile.exercises.ProductList
import com.itera.pam.myprofile.ui.screens.ProfileScreen
import com.itera.pam.myprofile.ui.theme.MyProfileTheme

enum class AppTab(val title: String, val icon: ImageVector) {
    PROFILE("Profil Saya", Icons.Default.AccountCircle),
    EXERCISE_1("Latihan 1", Icons.Default.Badge),
    EXERCISE_2("Latihan 2", Icons.Default.Lock),
    EXERCISE_3("Latihan 3", Icons.Default.ShoppingBag)
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun App() {
    var isDarkMode by remember { mutableStateOf(false) }
    var selectedTab by remember { mutableStateOf(AppTab.PROFILE) }

    MyProfileTheme(darkTheme = isDarkMode) {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = {
                        Column {
                            Text(
                                text = "My Profile App",
                                style = MaterialTheme.typography.titleMedium,
                                fontWeight = FontWeight.Bold
                            )
                            Text(
                                text = "PAM Minggu 3 • Muhammad Fatahillah Farid (123140203)",
                                style = MaterialTheme.typography.labelSmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant
                            )
                        }
                    },
                    actions = {
                        // Dark/Light Mode Toggle Button
                        IconButton(onClick = { isDarkMode = !isDarkMode }) {
                            Icon(
                                imageVector = if (isDarkMode) Icons.Default.LightMode else Icons.Default.DarkMode,
                                contentDescription = "Toggle Theme",
                                tint = MaterialTheme.colorScheme.primary
                            )
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(
                        containerColor = MaterialTheme.colorScheme.surface,
                        titleContentColor = MaterialTheme.colorScheme.onSurface
                    )
                )
            },
            bottomBar = {
                NavigationBar(
                    containerColor = MaterialTheme.colorScheme.surface,
                    tonalElevation = 6.dp
                ) {
                    AppTab.values().forEach { tab ->
                        NavigationBarItem(
                            selected = (selectedTab == tab),
                            onClick = { selectedTab = tab },
                            icon = {
                                Icon(
                                    imageVector = tab.icon,
                                    contentDescription = tab.title
                                )
                            },
                            label = {
                                Text(
                                    text = tab.title,
                                    fontWeight = if (selectedTab == tab) FontWeight.Bold else FontWeight.Normal
                                )
                            },
                            colors = NavigationBarItemDefaults.colors(
                                selectedIconColor = MaterialTheme.colorScheme.primary,
                                selectedTextColor = MaterialTheme.colorScheme.primary,
                                indicatorColor = MaterialTheme.colorScheme.primaryContainer
                            )
                        )
                    }
                }
            }
        ) { innerPadding ->
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding)
                    .background(MaterialTheme.colorScheme.background)
            ) {
                Crossfade(targetState = selectedTab) { tab ->
                    when (tab) {
                        AppTab.PROFILE -> ProfileScreen()
                        AppTab.EXERCISE_1 -> {
                            Column(
                                modifier = Modifier
                                    .fillMaxSize()
                                    .padding(16.dp),
                                horizontalAlignment = Alignment.CenterHorizontally,
                                verticalArrangement = Arrangement.Center
                            ) {
                                Text(
                                    text = "Latihan 1: ProfileCard Component",
                                    style = MaterialTheme.typography.titleLarge,
                                    fontWeight = FontWeight.Bold,
                                    modifier = Modifier.padding(bottom = 12.dp)
                                )
                                Exercise1ProfileCard(
                                    name = "John Doe",
                                    bio = "Mobile Developer & UI/UX Specialist",
                                    avatarInitial = "JD"
                                )
                                Exercise1ProfileCard(
                                    name = "Muhammad Fatahillah Farid",
                                    bio = "Teknik Informatika ITERA (123140203)",
                                    avatarInitial = "MF"
                                )
                            }
                        }
                        AppTab.EXERCISE_2 -> {
                            Box(
                                modifier = Modifier
                                    .fillMaxSize()
                                    .padding(16.dp),
                                contentAlignment = Alignment.Center
                            ) {
                                Exercise2LoginForm()
                            }
                        }
                        AppTab.EXERCISE_3 -> {
                            Box(
                                modifier = Modifier
                                    .fillMaxSize()
                                    .padding(horizontal = 8.dp),
                                contentAlignment = Alignment.TopCenter
                            ) {
                                ProductList()
                            }
                        }
                    }
                }
            }
        }
    }
}

fun main() = application {
    val windowState = rememberWindowState(
        size = DpSize(500.dp, 840.dp),
        position = WindowPosition(Alignment.Center)
    )

    Window(
        onCloseRequest = ::exitApplication,
        state = windowState,
        title = "My Profile App - PAM Pertemuan 3 (ITERA 123140203)"
    ) {
        App()
    }
}
