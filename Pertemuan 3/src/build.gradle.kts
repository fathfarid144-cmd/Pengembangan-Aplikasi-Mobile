plugins {
    kotlin("jvm") version "2.0.21"
    id("org.jetbrains.compose") version "1.7.0"
    id("org.jetbrains.kotlin.plugin.compose") version "2.0.21"
}

group = "com.itera.pam"
version = "1.0.0"

repositories {
    google()
    mavenCentral()
}

sourceSets {
    main {
        kotlin.srcDirs("main/kotlin")
        resources.srcDirs("main/resources")
    }
    test {
        kotlin.srcDirs("test/kotlin")
    }
}

dependencies {
    implementation(compose.desktop.currentOs)
    implementation(compose.material3)
    implementation(compose.materialIconsExtended)
    implementation(compose.animation)
    implementation(compose.ui)
    implementation(compose.foundation)

    testImplementation(kotlin("test"))
}

compose.desktop {
    application {
        mainClass = "com.itera.pam.myprofile.MainKt"
        nativeDistributions {
            packageName = "MyProfileApp"
            packageVersion = "1.0.0"
            description = "My Profile App - Praktikum PAM Pertemuan 3 ITERA"
            copyright = "© 2026 Muhammad Fatahillah Farid (123140203)"
            vendor = "Teknik Informatika ITERA"
        }
    }
}

kotlin {
    jvmToolchain(21)
}


