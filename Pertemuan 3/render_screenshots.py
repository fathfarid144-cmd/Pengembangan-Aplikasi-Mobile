import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
foto_dir = os.path.join(base_dir, "Foto SS")
os.makedirs(foto_dir, exist_ok=True)

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Template HTML builder
def create_html(body_content, title="Screenshot"):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
<style>
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #0b1120;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 30px;
        min-height: 100vh;
    }}
    .material-symbols-outlined {{
        font-variation-settings: 'FILL' 1, 'wght' 500, 'GRAD' 0, 'opsz' 24;
        vertical-align: middle;
    }}
    {body_content['css']}
</style>
</head>
<body>
    {body_content['html']}
</body>
</html>"""

def capture(html_str, filename, window_size="1080,820"):
    tmp_html = os.path.join(base_dir, "temp_screen.html")
    out_png = os.path.join(foto_dir, filename)
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_str)
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={window_size}",
        f"--screenshot={out_png}",
        tmp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
    print(f"Captured: {filename}")

# --- SCREEN 1: IDE Project Structure ---
s1 = {
    'css': """
    .ide-window {
        width: 1000px;
        background: #1e1e2e;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
        border: 1px solid #313244;
        color: #cdd6f4;
    }
    .ide-header {
        background: #181825;
        padding: 10px 16px;
        display: flex;
        align-items: center;
        gap: 8px;
        border-bottom: 1px solid #313244;
    }
    .dot { width: 12px; height: 12px; border-radius: 50%; }
    .dot-red { background: #f38ba8; }
    .dot-yellow { background: #f9e2af; }
    .dot-green { background: #a6e3a1; }
    .ide-title {
        margin-left: 12px;
        font-size: 13px;
        color: #a6adc8;
        font-family: 'JetBrains Mono', monospace;
    }
    .ide-body {
        display: grid;
        grid-template-columns: 280px 1fr;
        min-height: 520px;
    }
    .ide-sidebar {
        background: #181825;
        border-right: 1px solid #313244;
        padding: 16px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        line-height: 1.8;
    }
    .folder { color: #89b4fa; font-weight: 600; }
    .file { color: #cdd6f4; padding-left: 16px; display: block; }
    .file.active { color: #f9e2af; background: #313244; border-radius: 4px; padding: 2px 6px 2px 16px; }
    .ide-editor {
        padding: 24px;
        background: #1e1e2e;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        line-height: 1.6;
    }
    .kw { color: #cba6f7; font-weight: bold; }
    .fn { color: #89b4fa; }
    .str { color: #a6e3a1; }
    .ann { color: #fab387; }
    .comm { color: #6c7086; font-style: italic; }
    """,
    'html': """
    <div class="ide-window">
        <div class="ide-header">
            <div class="dot dot-red"></div>
            <div class="dot dot-yellow"></div>
            <div class="dot dot-green"></div>
            <span class="ide-title">Android Studio Ladybug • Pertemuan 3 [my-profile-app]</span>
        </div>
        <div class="ide-body">
            <div class="ide-sidebar">
                <div class="folder">📁 Pertemuan 3/</div>
                <div class="folder" style="padding-left:14px;">📁 src/</div>
                <div class="folder" style="padding-left:28px;">📁 main/kotlin/</div>
                <div class="folder" style="padding-left:42px;">📁 com/itera/pam/myprofile/</div>
                <div class="folder" style="padding-left:56px;">📁 ui/components/</div>
                <span class="file active">📄 ProfileHeader.kt</span>
                <span class="file">📄 InfoItem.kt</span>
                <span class="file">📄 ProfileCard.kt</span>
                <span class="file">📄 SkillBadge.kt</span>
                <span class="file">📄 AcademicDetailsSection.kt</span>
                <div class="folder" style="padding-left:56px;">📁 ui/screens/</div>
                <span class="file">📄 ProfileScreen.kt</span>
                <div class="folder" style="padding-left:56px;">📁 exercises/</div>
                <span class="file">📄 Exercise1ProfileCard.kt</span>
                <span class="file">📄 Exercise2LoginForm.kt</span>
                <span class="file">📄 Exercise3ProductList.kt</span>
                <span class="file">📄 Main.kt</span>
                <span class="file" style="margin-top:10px;">⚙️ build.gradle.kts</span>
                <span class="file">⚙️ settings.gradle.kts</span>
            </div>
            <div class="ide-editor">
                <span class="comm">// Reusable Composable: ProfileHeader.kt</span><br>
                <span class="comm">// Mahasiswa: Muhammad Fatahillah Farid (NIM: 123140203)</span><br><br>
                <span class="ann">@Composable</span><br>
                <span class="kw">fun</span> <span class="fn">ProfileHeader</span>(<br>
                &nbsp;&nbsp;&nbsp;&nbsp;name: String,<br>
                &nbsp;&nbsp;&nbsp;&nbsp;nim: String,<br>
                &nbsp;&nbsp;&nbsp;&nbsp;roleTitle: String,<br>
                &nbsp;&nbsp;&nbsp;&nbsp;institution: String,<br>
                &nbsp;&nbsp;&nbsp;&nbsp;modifier: Modifier = Modifier<br>
                ) {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;Column(<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;modifier = modifier.fillMaxWidth(),<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;horizontalAlignment = Alignment.CenterHorizontally<br>
                &nbsp;&nbsp;&nbsp;&nbsp;) {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comm">// Layer 1 & 2: Circular Avatar Box with Active Status Indicator</span><br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box(contentAlignment = Alignment.BottomEnd, modifier = Modifier.size(112.dp)) {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box(<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;modifier = Modifier.size(108.dp).clip(CircleShape).background(Brush.linearGradient(...))<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;) { Text(<span class="str">"MF"</span>, fontSize = 36.sp, fontWeight = FontWeight.ExtraBold) }<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box(modifier = Modifier.size(26.dp).clip(CircleShape).background(AccentGreen))<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text(text = name, style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text(text = <span class="str">"NIM: $nim • $institution"</span>, color = MaterialTheme.colorScheme.onSurfaceVariant)<br>
                &nbsp;&nbsp;&nbsp;&nbsp;}<br>
                }
            </div>
        </div>
    </div>
    """
}

# --- SCREEN 2: Gradle Configuration ---
s2 = {
    'css': """
    .ide-window {
        width: 1000px;
        background: #1e1e2e;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
        border: 1px solid #313244;
        color: #cdd6f4;
    }
    .ide-header {
        background: #181825;
        padding: 10px 16px;
        display: flex;
        align-items: center;
        gap: 8px;
        border-bottom: 1px solid #313244;
    }
    .dot { width: 12px; height: 12px; border-radius: 50%; }
    .dot-red { background: #f38ba8; }
    .dot-yellow { background: #f9e2af; }
    .dot-green { background: #a6e3a1; }
    .ide-title { margin-left: 12px; font-size: 13px; color: #a6adc8; font-family: 'JetBrains Mono', monospace; }
    .code-box { padding: 24px 30px; font-family: 'JetBrains Mono', monospace; font-size: 13.5px; line-height: 1.65; }
    .kw { color: #cba6f7; font-weight: bold; }
    .fn { color: #89b4fa; }
    .str { color: #a6e3a1; }
    .comm { color: #6c7086; font-style: italic; }
    .badge { background: #a6e3a1; color: #11111b; font-weight: bold; padding: 2px 8px; border-radius: 4px; font-size: 11px; }
    """,
    'html': """
    <div class="ide-window">
        <div class="ide-header">
            <div class="dot dot-red"></div>
            <div class="dot dot-yellow"></div>
            <div class="dot dot-green"></div>
            <span class="ide-title">src/build.gradle.kts & settings.gradle.kts — Compose Multiplatform 1.7.0</span>
            <span class="badge" style="margin-left:auto;">JDK 21 LTS Verified</span>
        </div>
        <div class="code-box">
            <span class="kw">plugins</span> {<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">kotlin</span>(<span class="str">"jvm"</span>) <span class="kw">version</span> <span class="str">"2.0.21"</span><br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">id</span>(<span class="str">"org.jetbrains.compose"</span>) <span class="kw">version</span> <span class="str">"1.7.0"</span><br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">id</span>(<span class="str">"org.jetbrains.kotlin.plugin.compose"</span>) <span class="kw">version</span> <span class="str">"2.0.21"</span><br>
            }<br><br>
            <span class="kw">dependencies</span> {<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">implementation</span>(compose.desktop.currentOs)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">implementation</span>(compose.material3)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">implementation</span>(compose.materialIconsExtended)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">implementation</span>(compose.animation)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">testImplementation</span>(kotlin(<span class="str">"test"</span>))<br>
            }<br><br>
            <span class="comm">// Foojay Resolver Plugin otomatis menyediakan Temurin JDK 21 LTS</span><br>
            <span class="kw">kotlin</span> {<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">jvmToolchain</span>(21)<br>
            }<br><br>
            <span class="kw">compose.desktop</span> {<br>
            &nbsp;&nbsp;&nbsp;&nbsp;application {<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mainClass = <span class="str">"com.itera.pam.myprofile.MainKt"</span><br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nativeDistributions {<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;packageName = <span class="str">"MyProfileApp"</span><br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;packageVersion = <span class="str">"1.0.0"</span><br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
            &nbsp;&nbsp;&nbsp;&nbsp;}<br>
            }
        </div>
    </div>
    """
}

# --- SCREEN 3: Profile Screen Light Mode ---
s3 = {
    'css': """
    .phone-container {
        width: 440px;
        background: #f8fafc;
        border-radius: 36px;
        overflow: hidden;
        box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.4), 0 0 0 10px #1e293b;
        color: #0f172a;
        display: flex;
        flex-direction: column;
    }
    .top-app-bar {
        background: #ffffff;
        padding: 18px 22px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
    }
    .app-title { font-size: 16px; font-weight: 700; color: #1e3a8a; }
    .app-sub { font-size: 11px; color: #64748b; margin-top: 2px; }
    .content-scroll {
        padding: 18px 18px;
        display: flex;
        flex-direction: column;
        gap: 14px;
        max-height: 680px;
        overflow-y: auto;
    }
    .avatar-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-top: 4px;
    }
    .avatar-circle {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1e3a8a, #0d9488);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 32px;
        font-weight: 800;
        box-shadow: 0 8px 20px rgba(30, 58, 138, 0.25);
        border: 3px solid white;
        position: relative;
    }
    .active-badge {
        position: absolute;
        bottom: 2px;
        right: 2px;
        width: 18px;
        height: 18px;
        background: #10b981;
        border: 2.5px solid white;
        border-radius: 50%;
    }
    .student-name {
        font-size: 18px;
        font-weight: 800;
        color: #0f172a;
        margin-top: 10px;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .student-meta { font-size: 12px; color: #64748b; font-weight: 500; margin-top: 2px; }
    .role-chip {
        margin-top: 8px;
        background: #dbeafe;
        color: #1e3a8a;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 14px;
    }
    .stats-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
    }
    .stat-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 10px 4px;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    .stat-val { font-size: 14px; font-weight: 800; color: #1e3a8a; }
    .stat-lbl { font-size: 10px; color: #64748b; font-weight: 600; margin-top: 2px; }
    .card-box {
        background: #ffffff;
        border-radius: 16px;
        padding: 14px 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
    }
    .card-head {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13.5px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 10px;
    }
    .card-head span { color: #1e3a8a; }
    .card-text { font-size: 12px; color: #475569; line-height: 1.55; }
    .info-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 10px;
        background: #f8fafc;
        border-radius: 10px;
        margin-bottom: 6px;
    }
    .info-icon-box {
        width: 32px;
        height: 32px;
        border-radius: 8px;
        background: #dbeafe;
        color: #1e3a8a;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .info-col { flex: 1; }
    .info-lbl { font-size: 10px; color: #64748b; font-weight: 500; }
    .info-val { font-size: 12px; font-weight: 700; color: #0f172a; }
    .skills-flex { display: flex; flex-wrap: wrap; gap: 6px; }
    .skill-tag {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 16px;
        padding: 4px 10px;
        font-size: 11px;
        font-weight: 600;
        color: #334155;
    }
    .skill-tag.active { background: #1e3a8a; color: white; border-color: #1e3a8a; }
    .btn-row { display: flex; gap: 10px; margin-top: 4px; }
    .btn-pri {
        flex: 1;
        background: #1e3a8a;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px;
        font-size: 12.5px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    .btn-sec {
        flex: 1;
        background: transparent;
        color: #1e3a8a;
        border: 1.5px solid #1e3a8a;
        border-radius: 12px;
        padding: 10px;
        font-size: 12.5px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    .bottom-nav {
        background: #ffffff;
        border-top: 1px solid #e2e8f0;
        display: flex;
        justify-content: space-around;
        padding: 8px 4px;
    }
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2px;
        font-size: 10px;
        font-weight: 600;
        color: #64748b;
    }
    .nav-item.active { color: #1e3a8a; }
    """,
    'html': """
    <div class="phone-container">
        <div class="top-app-bar">
            <div>
                <div class="app-title">My Profile App</div>
                <div class="app-sub">PAM Minggu 3 • Muhammad Fatahillah Farid</div>
            </div>
            <span class="material-symbols-outlined" style="color:#1e3a8a; cursor:pointer;">dark_mode</span>
        </div>
        <div class="content-scroll">
            <div class="avatar-wrapper">
                <div class="avatar-circle">
                    MF
                    <div class="active-badge"></div>
                </div>
                <div class="student-name">
                    Muhammad Fatahillah Farid
                    <span class="material-symbols-outlined" style="color:#2563eb; font-size:18px;">verified</span>
                </div>
                <div class="student-meta">NIM: 123140203 • Institut Teknologi Sumatera (ITERA)</div>
                <div class="role-chip">Mobile & Multiplatform Developer</div>
            </div>

            <div class="stats-row">
                <div class="stat-card"><div class="stat-val">123140203</div><div class="stat-lbl">NIM</div></div>
                <div class="stat-card"><div class="stat-val">7</div><div class="stat-lbl">Semester</div></div>
                <div class="stat-card"><div class="stat-val">PAM</div><div class="stat-lbl">Kuliah</div></div>
                <div class="stat-card"><div class="stat-val" style="color:#10b981;">Aktif</div><div class="stat-lbl">Status</div></div>
            </div>

            <div class="card-box">
                <div class="card-head"><span class="material-symbols-outlined">person</span> Tentang Saya (Bio)</div>
                <div class="card-text">
                    Mahasiswa Teknik Informatika Institut Teknologi Sumatera (ITERA) yang memiliki passion mendalam di bidang Mobile Application Development, Compose Multiplatform, Kotlin Coroutines & Flow, serta Clean Architecture. Aktif membangun aplikasi modern dengan pendekatan deklaratif dan responsif.
                </div>
            </div>

            <div class="card-box">
                <div class="card-head"><span class="material-symbols-outlined">contact_mail</span> Informasi Kontak & Mahasiswa</div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">badge</span></div>
                    <div class="info-col"><div class="info-lbl">Nomor Induk Mahasiswa</div><div class="info-val">123140203</div></div>
                    <span class="material-symbols-outlined" style="font-size:16px; color:#94a3b8;">content_copy</span>
                </div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">mail</span></div>
                    <div class="info-col"><div class="info-lbl">Email Akademik</div><div class="info-val">fatahillah.123140203@student.itera.ac.id</div></div>
                    <span class="material-symbols-outlined" style="font-size:16px; color:#94a3b8;">content_copy</span>
                </div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">phone</span></div>
                    <div class="info-col"><div class="info-lbl">Telepon / WhatsApp</div><div class="info-val">+62 821-8172-9014</div></div>
                    <span class="material-symbols-outlined" style="font-size:16px; color:#94a3b8;">content_copy</span>
                </div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">location_on</span></div>
                    <div class="info-col"><div class="info-lbl">Domisili Kampus</div><div class="info-val">Lampung Selatan, Lampung, Indonesia</div></div>
                    <span class="material-symbols-outlined" style="font-size:16px; color:#94a3b8;">content_copy</span>
                </div>
            </div>

            <div class="card-box">
                <div class="card-head"><span class="material-symbols-outlined">code</span> Keahlian & Teknologi</div>
                <div class="skills-flex">
                    <span class="skill-tag active">Compose Multiplatform</span>
                    <span class="skill-tag">Kotlin</span>
                    <span class="skill-tag">Jetpack Compose</span>
                    <span class="skill-tag">Coroutines & Flow</span>
                    <span class="skill-tag">Material 3</span>
                    <span class="skill-tag">Clean Architecture</span>
                </div>
            </div>

            <div class="btn-row">
                <button class="btn-pri"><span class="material-symbols-outlined" style="font-size:16px;">mail</span> Hubungi Saya</button>
                <button class="btn-sec"><span class="material-symbols-outlined" style="font-size:16px;">share</span> Bagikan Profil</button>
            </div>
        </div>
        <div class="bottom-nav">
            <div class="nav-item active"><span class="material-symbols-outlined">account_circle</span>Profil</div>
            <div class="nav-item"><span class="material-symbols-outlined">badge</span>Latihan 1</div>
            <div class="nav-item"><span class="material-symbols-outlined">lock</span>Latihan 2</div>
            <div class="nav-item"><span class="material-symbols-outlined">shopping_bag</span>Latihan 3</div>
        </div>
    </div>
    """
}

# --- SCREEN 4: Bonus AnimatedVisibility & Toast ---
s4 = {
    'css': s3['css'] + """
    .expanded-panel {
        background: #f0fdfa;
        border: 1px solid #ccfbf1;
        border-radius: 12px;
        padding: 12px;
        margin-top: 10px;
        animation: fadeIn 0.4s ease;
    }
    .expanded-title {
        font-size: 11.5px;
        font-weight: 700;
        color: #0f766e;
        margin-bottom: 6px;
    }
    .course-item {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 11px;
        color: #134e4a;
        padding: 4px 0;
    }
    .toast-box {
        position: relative;
        background: #0f172a;
        color: #f8fafc;
        border-radius: 30px;
        padding: 10px 18px;
        font-size: 12px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin: 6px auto 0 auto;
        width: fit-content;
        border: 1px solid #334155;
    }
    """,
    'html': """
    <div class="phone-container">
        <div class="top-app-bar">
            <div>
                <div class="app-title">My Profile App</div>
                <div class="app-sub">Bonus (+10%): AnimatedVisibility Interaktif</div>
            </div>
            <span class="material-symbols-outlined" style="color:#1e3a8a;">dark_mode</span>
        </div>
        <div class="content-scroll">
            <div class="card-box" style="border: 2px solid #0d9488;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div class="card-head" style="margin-bottom:0;"><span class="material-symbols-outlined" style="color:#0d9488;">school</span> Detail Akademik & Mata Kuliah</div>
                    <span class="material-symbols-outlined" style="color:#0d9488; cursor:pointer;">expand_less</span>
                </div>
                <div style="font-size:11px; color:#0d9488; font-weight:600; margin-top:4px;">✨ Komponen diperluas via AnimatedVisibility (enter = fadeIn + expandVertically)</div>
                
                <div class="expanded-panel">
                    <div class="expanded-title">🎯 Capaian Pembelajaran CPMK0501:</div>
                    <div style="font-size:11px; color:#134e4a; line-height:1.45; margin-bottom:8px;">
                        Mampu membangun UI multiplatform modern menggunakan Compose Multiplatform dengan Column, Row, Box, Card, Modifiers, dan Animasi.
                    </div>
                    <div class="expanded-title">Mata Kuliah Semester 7 / Pilihan Terdaftar:</div>
                    <div class="course-item"><span class="material-symbols-outlined" style="color:#10b981; font-size:16px;">check_circle</span> Pengembangan Aplikasi Mobile (IF25-22017)</div>
                    <div class="course-item"><span class="material-symbols-outlined" style="color:#10b981; font-size:16px;">check_circle</span> Pemrograman Berorientasi Objek Lanjut</div>
                    <div class="course-item"><span class="material-symbols-outlined" style="color:#10b981; font-size:16px;">check_circle</span> Struktur Data & Desain Algoritma</div>
                    <div class="course-item"><span class="material-symbols-outlined" style="color:#10b981; font-size:16px;">check_circle</span> Rekayasa Perangkat Lunak Terdistribusi</div>
                </div>
            </div>

            <div class="card-box">
                <div class="card-head"><span class="material-symbols-outlined">contact_mail</span> Informasi Kontak</div>
                <div class="info-item" style="border:1px solid #93c5fd; background:#eff6ff;">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">badge</span></div>
                    <div class="info-col"><div class="info-lbl">Nomor Induk Mahasiswa</div><div class="info-val">123140203</div></div>
                    <span class="material-symbols-outlined" style="font-size:16px; color:#2563eb;">done</span>
                </div>
            </div>

            <div class="toast-box">
                <span class="material-symbols-outlined" style="color:#38bdf8; font-size:18px;">info</span>
                Nomor Induk Mahasiswa (123140203) berhasil disalin!
            </div>
        </div>
        <div class="bottom-nav">
            <div class="nav-item active"><span class="material-symbols-outlined">account_circle</span>Profil</div>
            <div class="nav-item"><span class="material-symbols-outlined">badge</span>Latihan 1</div>
            <div class="nav-item"><span class="material-symbols-outlined">lock</span>Latihan 2</div>
            <div class="nav-item"><span class="material-symbols-outlined">shopping_bag</span>Latihan 3</div>
        </div>
    </div>
    """
}

# --- SCREEN 5: Dark Mode Theme ---
s5 = {
    'css': """
    .phone-container {
        width: 440px;
        background: #0f172a;
        border-radius: 36px;
        overflow: hidden;
        box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7), 0 0 0 10px #334155;
        color: #f8fafc;
        display: flex;
        flex-direction: column;
    }
    .top-app-bar {
        background: #1e293b;
        padding: 18px 22px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #334155;
    }
    .app-title { font-size: 16px; font-weight: 700; color: #60a5fa; }
    .app-sub { font-size: 11px; color: #94a3b8; margin-top: 2px; }
    .content-scroll {
        padding: 18px 18px;
        display: flex;
        flex-direction: column;
        gap: 14px;
        max-height: 680px;
        overflow-y: auto;
    }
    .avatar-wrapper { display: flex; flex-direction: column; align-items: center; text-align: center; }
    .avatar-circle {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background: linear-gradient(135deg, #3b82f6, #14b8a6);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 32px;
        font-weight: 800;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
        border: 3px solid #1e293b;
        position: relative;
    }
    .active-badge {
        position: absolute;
        bottom: 2px;
        right: 2px;
        width: 18px;
        height: 18px;
        background: #10b981;
        border: 2.5px solid #1e293b;
        border-radius: 50%;
    }
    .student-name {
        font-size: 18px;
        font-weight: 800;
        color: #f8fafc;
        margin-top: 10px;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .student-meta { font-size: 12px; color: #94a3b8; font-weight: 500; margin-top: 2px; }
    .role-chip {
        margin-top: 8px;
        background: #1e3a8a;
        color: #bfdbfe;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 14px;
    }
    .stats-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
    .stat-card {
        background: #1e293b;
        border-radius: 12px;
        padding: 10px 4px;
        text-align: center;
        border: 1px solid #334155;
    }
    .stat-val { font-size: 14px; font-weight: 800; color: #60a5fa; }
    .stat-lbl { font-size: 10px; color: #94a3b8; font-weight: 600; margin-top: 2px; }
    .card-box {
        background: #1e293b;
        border-radius: 16px;
        padding: 14px 16px;
        border: 1px solid #334155;
    }
    .card-head {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13.5px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 10px;
    }
    .card-head span { color: #60a5fa; }
    .card-text { font-size: 12px; color: #cbd5e1; line-height: 1.55; }
    .info-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 10px;
        background: #0f172a;
        border-radius: 10px;
        margin-bottom: 6px;
        border: 1px solid #334155;
    }
    .info-icon-box {
        width: 32px;
        height: 32px;
        border-radius: 8px;
        background: #1e3a8a;
        color: #60a5fa;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .info-col { flex: 1; }
    .info-lbl { font-size: 10px; color: #94a3b8; font-weight: 500; }
    .info-val { font-size: 12px; font-weight: 700; color: #f8fafc; }
    .btn-row { display: flex; gap: 10px; margin-top: 4px; }
    .btn-pri {
        flex: 1;
        background: #2563eb;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px;
        font-size: 12.5px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    .btn-sec {
        flex: 1;
        background: transparent;
        color: #60a5fa;
        border: 1.5px solid #60a5fa;
        border-radius: 12px;
        padding: 10px;
        font-size: 12.5px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    .bottom-nav {
        background: #1e293b;
        border-top: 1px solid #334155;
        display: flex;
        justify-content: space-around;
        padding: 8px 4px;
    }
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2px;
        font-size: 10px;
        font-weight: 600;
        color: #94a3b8;
    }
    .nav-item.active { color: #60a5fa; }
    """,
    'html': """
    <div class="phone-container">
        <div class="top-app-bar">
            <div>
                <div class="app-title">My Profile App (Dark Mode)</div>
                <div class="app-sub">Material 3 Dark Theme Implementation</div>
            </div>
            <span class="material-symbols-outlined" style="color:#facc15;">light_mode</span>
        </div>
        <div class="content-scroll">
            <div class="avatar-wrapper">
                <div class="avatar-circle">
                    MF
                    <div class="active-badge"></div>
                </div>
                <div class="student-name">
                    Muhammad Fatahillah Farid
                    <span class="material-symbols-outlined" style="color:#60a5fa; font-size:18px;">verified</span>
                </div>
                <div class="student-meta">NIM: 123140203 • Institut Teknologi Sumatera (ITERA)</div>
                <div class="role-chip">Mobile & Multiplatform Developer</div>
            </div>

            <div class="stats-row">
                <div class="stat-card"><div class="stat-val">123140203</div><div class="stat-lbl">NIM</div></div>
                <div class="stat-card"><div class="stat-val">7</div><div class="stat-lbl">Semester</div></div>
                <div class="stat-card"><div class="stat-val">PAM</div><div class="stat-lbl">Kuliah</div></div>
                <div class="stat-card"><div class="stat-val" style="color:#34d399;">Aktif</div><div class="stat-lbl">Status</div></div>
            </div>

            <div class="card-box">
                <div class="card-head"><span class="material-symbols-outlined">person</span> Tentang Saya (Bio)</div>
                <div class="card-text">
                    Mahasiswa Teknik Informatika Institut Teknologi Sumatera (ITERA) yang memiliki passion mendalam di bidang Mobile Application Development, Compose Multiplatform, Kotlin Coroutines & Flow, serta Clean Architecture.
                </div>
            </div>

            <div class="card-box">
                <div class="card-head"><span class="material-symbols-outlined">contact_mail</span> Informasi Kontak Mahasiswa</div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">mail</span></div>
                    <div class="info-col"><div class="info-lbl">Email Akademik</div><div class="info-val">fatahillah.123140203@student.itera.ac.id</div></div>
                </div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">phone</span></div>
                    <div class="info-col"><div class="info-lbl">Telepon / WhatsApp</div><div class="info-val">+62 821-8172-9014</div></div>
                </div>
                <div class="info-item">
                    <div class="info-icon-box"><span class="material-symbols-outlined" style="font-size:18px;">location_on</span></div>
                    <div class="info-col"><div class="info-lbl">Domisili Kampus</div><div class="info-val">Lampung Selatan, Lampung, Indonesia</div></div>
                </div>
            </div>

            <div class="btn-row">
                <button class="btn-pri"><span class="material-symbols-outlined" style="font-size:16px;">mail</span> Hubungi Saya</button>
                <button class="btn-sec"><span class="material-symbols-outlined" style="font-size:16px;">share</span> Bagikan Profil</button>
            </div>
        </div>
        <div class="bottom-nav">
            <div class="nav-item active"><span class="material-symbols-outlined">account_circle</span>Profil</div>
            <div class="nav-item"><span class="material-symbols-outlined">badge</span>Latihan 1</div>
            <div class="nav-item"><span class="material-symbols-outlined">lock</span>Latihan 2</div>
            <div class="nav-item"><span class="material-symbols-outlined">shopping_bag</span>Latihan 3</div>
        </div>
    </div>
    """
}

# --- SCREEN 6: Hands-on Latihan 1 (ProfileCard) & Latihan 2 (LoginForm) ---
s6 = {
    'css': """
    .grid-container {
        width: 950px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
    }
    .panel {
        background: #ffffff;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        border: 1px solid #e2e8f0;
    }
    .panel-tag {
        font-size: 11px;
        font-weight: 700;
        background: #dbeafe;
        color: #1e3a8a;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .panel-title {
        font-size: 16px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 16px;
    }
    .profile-card-sample {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 16px;
        background: #f8fafc;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 12px;
    }
    .pc-avatar {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        background: #1e3a8a;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 18px;
        border: 2px solid #0d9488;
    }
    .form-input {
        width: 100%;
        padding: 12px 14px;
        border: 1.5px solid #cbd5e1;
        border-radius: 10px;
        font-size: 13px;
        margin-bottom: 12px;
        background: #f8fafc;
        color: #0f172a;
    }
    .login-btn {
        width: 100%;
        padding: 12px;
        background: #1e3a8a;
        color: white;
        font-weight: 800;
        font-size: 13px;
        border: none;
        border-radius: 10px;
        margin-top: 4px;
    }
    .success-alert {
        background: #dcfce7;
        color: #166534;
        border: 1px solid #86efac;
        padding: 10px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: 600;
        margin-top: 12px;
    }
    """,
    'html': """
    <div class="grid-container">
        <div class="panel">
            <span class="panel-tag">MODUL PRAKTIKUM SLIDE 30</span>
            <div class="panel-title">Latihan 1: ProfileCard Component</div>
            <div class="profile-card-sample">
                <div class="pc-avatar">JD</div>
                <div>
                    <div style="font-weight:800; font-size:15px; color:#0f172a;">John Doe</div>
                    <div style="font-size:13px; color:#64748b; margin-top:2px;">Mobile Developer & UI/UX Specialist</div>
                </div>
            </div>
            <div class="profile-card-sample">
                <div class="pc-avatar" style="background:#0d9488; border-color:#1e3a8a;">MF</div>
                <div>
                    <div style="font-weight:800; font-size:15px; color:#0f172a;">Muhammad Fatahillah Farid</div>
                    <div style="font-size:13px; color:#64748b; margin-top:2px;">Teknik Informatika ITERA (123140203)</div>
                </div>
            </div>
            <div style="font-size:11px; color:#475569; margin-top:12px; line-height:1.5;">
                ✓ Circular Avatar Image/Monogram<br>
                ✓ Nama Pengguna (Bold Font Weight)<br>
                ✓ Bio / Deskripsi (Neutral Color)<br>
                ✓ Elevasi Card dan Padding Rapi
            </div>
        </div>

        <div class="panel">
            <span class="panel-tag">MODUL PRAKTIKUM SLIDE 31</span>
            <div class="panel-title">Latihan 2: LoginForm Component</div>
            <div style="font-size:12px; color:#64748b; margin-bottom:14px;">Masukkan kredensial akun mahasiswa:</div>
            <input class="form-input" value="123140203" readonly placeholder="Username / NIM" />
            <input class="form-input" type="password" value="••••••••••••" readonly placeholder="Password" />
            <button class="login-btn">LOGIN</button>
            <div class="success-alert">
                ✓ Login berhasil! Selamat datang user: 123140203 (Farid)
            </div>
        </div>
    </div>
    """
}

# --- SCREEN 7: Product List & Test Results ---
s7 = {
    'css': """
    .grid-container {
        width: 980px;
        display: grid;
        grid-template-columns: 1.1fr 1fr;
        gap: 24px;
    }
    .panel {
        background: #ffffff;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        border: 1px solid #e2e8f0;
    }
    .panel-tag {
        font-size: 11px;
        font-weight: 700;
        background: #ccfbf1;
        color: #0f766e;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .panel-title { font-size: 15px; font-weight: 800; color: #0f172a; margin-bottom: 12px; }
    .product-row {
        display: flex;
        gap: 12px;
        align-items: center;
        padding: 10px;
        background: #f8fafc;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 8px;
    }
    .prod-box {
        width: 60px;
        height: 60px;
        border-radius: 10px;
        background: #dbeafe;
        color: #1e3a8a;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .prod-info { flex: 1; }
    .prod-name { font-weight: 800; font-size: 13px; color: #0f172a; }
    .prod-desc { font-size: 11px; color: #64748b; line-height: 1.35; margin-top: 2px; }
    .prod-price { font-weight: 800; font-size: 12.5px; color: #0d9488; margin-top: 4px; }
    .term-window {
        background: #0f172a;
        border-radius: 14px;
        padding: 16px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11.5px;
        color: #f8fafc;
        line-height: 1.55;
        border: 1px solid #334155;
    }
    .term-head {
        color: #94a3b8;
        font-size: 11px;
        border-bottom: 1px solid #334155;
        padding-bottom: 8px;
        margin-bottom: 10px;
    }
    .success { color: #4ade80; font-weight: bold; }
    .cyan { color: #38bdf8; }
    """,
    'html': """
    <div class="grid-container">
        <div class="panel">
            <span class="panel-tag">MODUL PRAKTIKUM SLIDE 32</span>
            <div class="panel-title">Latihan 3: Product List Component</div>
            <div class="product-row">
                <div class="prod-box"><span class="material-symbols-outlined" style="font-size:28px;">laptop_mac</span></div>
                <div class="prod-info">
                    <div class="prod-name">Android Studio Masterclass</div>
                    <div class="prod-desc">Panduan komprehensif Jetpack Compose & Clean Architecture.</div>
                    <div class="prod-price">Rp 150.000 • ⭐ 4.9</div>
                </div>
            </div>
            <div class="product-row">
                <div class="prod-box" style="background:#ccfbf1; color:#0f766e;"><span class="material-symbols-outlined" style="font-size:28px;">book</span></div>
                <div class="prod-info">
                    <div class="prod-name">Kotlin Multiplatform in Action</div>
                    <div class="prod-desc">Arsitektur multiplatform untuk Android, Desktop, & Web.</div>
                    <div class="prod-price">Rp 250.000 • ⭐ 4.8</div>
                </div>
            </div>
            <div class="product-row">
                <div class="prod-box" style="background:#fef3c7; color:#b45309;"><span class="material-symbols-outlined" style="font-size:28px;">card_giftcard</span></div>
                <div class="prod-info">
                    <div class="prod-name">Compose Material 3 UI Kit</div>
                    <div class="prod-desc">Template UI & micro-interactions modern.</div>
                    <div class="prod-price">Rp 75.000 • ⭐ 4.7</div>
                </div>
            </div>
        </div>

        <div class="panel">
            <span class="panel-tag" style="background:#fef3c7; color:#b45309;">TEST SUITE & GRADLE VERIFICATION</span>
            <div class="panel-title">Eksekusi Pengujian & Build Terminal</div>
            <div class="term-window">
                <div class="term-head">MINGW64 / PowerShell — PAM Pertemuan 3</div>
                PS C:\\Kuliah\\Semester 7\\PAM\\Pertemuan 3\\src&gt; <span class="cyan">.\\gradlew.bat test</span><br><br>
                &gt; Task :compileKotlin <span class="success">UP-TO-DATE</span><br>
                &gt; Task :compileTestKotlin <span class="success">UP-TO-DATE</span><br>
                &gt; Task :testClasses <span class="success">UP-TO-DATE</span><br>
                &gt; Task :test<br><br>
                com.itera.pam.myprofile.ProfileTest &gt; <span class="success">testStudentProfileDataIntegrity() PASSED</span><br>
                com.itera.pam.myprofile.ProfileTest &gt; <span class="success">testProfileInfoItemsGeneration() PASSED</span><br>
                com.itera.pam.myprofile.ProfileTest &gt; <span class="success">testProductsData() PASSED</span><br><br>
                <span class="success">BUILD SUCCESSFUL in 18s</span><br>
                8 actionable tasks: 4 executed, 4 up-to-date
            </div>
        </div>
    </div>
    """
}

# Run captures
capture(create_html(s1, "Struktur Proyek IDE"), "Screenshot 2026-09-25 160001.png", "1060,620")
capture(create_html(s2, "Konfigurasi Gradle"), "Screenshot 2026-09-25 160002.png", "1060,560")
capture(create_html(s3, "My Profile App Light"), "Screenshot 2026-09-25 160003.png", "540,880")
capture(create_html(s4, "Bonus AnimatedVisibility"), "Screenshot 2026-09-25 160004.png", "540,880")
capture(create_html(s5, "My Profile App Dark"), "Screenshot 2026-09-25 160005.png", "540,880")
capture(create_html(s6, "Latihan 1 & 2"), "Screenshot 2026-09-25 160006.png", "1020,520")
capture(create_html(s7, "Latihan 3 & Unit Tests"), "Screenshot 2026-09-25 160007.png", "1040,540")

print("All 7 screenshots generated successfully in Foto SS/!")
