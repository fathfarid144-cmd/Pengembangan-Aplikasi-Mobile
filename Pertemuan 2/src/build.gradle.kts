plugins {
    kotlin("jvm") version "1.9.22"
    application
}

group = "com.itera.pam"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    // Kotlin Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.0")

    // Testing
    testImplementation(kotlin("test"))
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.8.0")
}

application {
    mainClass.set("com.itera.pam.newsfeed.MainKt")
}

tasks.test {
    useJUnitPlatform()
}

tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
    kotlinOptions.jvmTarget = "1.8"
}

tasks.withType<JavaCompile> {
    sourceCompatibility = "1.8"
    targetCompatibility = "1.8"
}
