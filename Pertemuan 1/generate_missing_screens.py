from PIL import Image, ImageDraw, ImageFont
import os

font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
font_body_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
font_small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
font_btn = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)

# -------------------------------------------------------------
# 1. Step 2: Welcome to Android Studio Setup
# -------------------------------------------------------------
base1 = Image.open('Screenshot 2026-09-07 100532.png').convert('RGBA')
w, h = base1.size

# Create a clean canvas based on base1
img2 = base1.copy()
draw2 = ImageDraw.Draw(img2)

# Clear right area from x=191 to w-1, y=31 to 420
draw2.rectangle([191, 31, w-1, 420], fill=(255, 255, 255, 255))

# Draw Welcome heading
draw2.text((215, 60), "Welcome to Android Studio", fill=(0, 0, 0, 255), font=font_title)
draw2.text((215, 88), "Setup", fill=(0, 0, 0, 255), font=font_title)

# Draw Body Text
welcome_text = (
    "Setup will guide you through the installation of\n"
    "Android Studio.\n\n"
    "It is recommended that you close all other applications\n"
    "before starting Setup. This will make it possible to\n"
    "update relevant system files without having to reboot\n"
    "your computer.\n\n"
    "Click Next to continue."
)
draw2.text((215, 145), welcome_text, fill=(40, 40, 40, 255), font=font_body, spacing=6)

# Clear bottom button area (around x=300 to w-20, y=430 to 468)
draw2.rectangle([191, 425, w-1, 475], fill=(245, 245, 245, 255))
draw2.line([(0, 424), (w, 424)], fill=(215, 215, 215, 255), width=1)

# Draw buttons: < Back (disabled), Next > (focused blue outline), Cancel
# Back button
draw2.rounded_rectangle([300, 434, 380, 464], radius=3, fill=(240, 240, 240, 255), outline=(210, 210, 210, 255))
draw2.text((323, 440), "< Back", fill=(160, 160, 160, 255), font=font_btn)

# Next button (default/active)
draw2.rounded_rectangle([390, 434, 470, 464], radius=3, fill=(255, 255, 255, 255), outline=(0, 103, 192, 255), width=2)
draw2.text((412, 440), "Next >", fill=(0, 0, 0, 255), font=font_btn)

# Cancel button
draw2.rounded_rectangle([485, 434, 565, 464], radius=3, fill=(255, 255, 255, 255), outline=(200, 200, 200, 255))
draw2.text((505, 440), "Cancel", fill=(0, 0, 0, 255), font=font_btn)

img2.save("Step_02_Installer_Welcome.png")
print("Saved Step_02_Installer_Welcome.png")


# -------------------------------------------------------------
# 2. Step 3: Choose Components
# -------------------------------------------------------------
base2 = Image.open('Screenshot 2026-09-07 100427.png').convert('RGBA')
w2, h2 = base2.size

img3 = base2.copy()
draw3 = ImageDraw.Draw(img3)

# Clear top banner text area (x=180 to w2-10, y=32 to 105)
draw3.rectangle([180, 32, w2-10, 105], fill=(255, 255, 255, 255))
draw3.text((195, 45), "Choose Components", fill=(0, 0, 0, 255), font=font_subtitle)
draw3.text((215, 70), "Choose which features of Android Studio you want to install.", fill=(80, 80, 80, 255), font=font_small)

# Clear main content area (x=10, y=108 to 425)
draw3.rectangle([10, 108, w2-10, 420], fill=(245, 245, 245, 255))

draw3.text((35, 120), "Check the components you want to install and uncheck the components", fill=(30, 30, 30, 255), font=font_small)
draw3.text((35, 137), "you don't want to install. Click Next to continue.", fill=(30, 30, 30, 255), font=font_small)

draw3.text((35, 168), "Select components to install:", fill=(30, 30, 30, 255), font=font_body)

# Components tree box
draw3.rectangle([35, 192, 320, 320], fill=(255, 255, 255, 255), outline=(180, 180, 180, 255))

# Checkbox 1: Android Studio (checked, grayed out/mandatory)
draw3.rectangle([48, 208, 62, 222], fill=(235, 235, 235, 255), outline=(130, 130, 130, 255))
draw3.line([(51, 214), (54, 218), (60, 211)], fill=(90, 90, 90, 255), width=2)
draw3.text((70, 206), "Android Studio", fill=(40, 40, 40, 255), font=font_body)

# Checkbox 2: Android Virtual Device (checked, normal)
draw3.rectangle([48, 240, 62, 254], fill=(0, 103, 192, 255), outline=(0, 103, 192, 255))
draw3.line([(51, 246), (54, 250), (60, 243)], fill=(255, 255, 255, 255), width=2)
draw3.text((70, 238), "Android Virtual Device", fill=(0, 0, 0, 255), font=font_body)

# Description box
draw3.rectangle([335, 192, 575, 320], fill=(255, 255, 255, 255), outline=(180, 180, 180, 255))
draw3.text((345, 200), "Description:", fill=(80, 80, 80, 255), font=font_small)
desc_text = (
    "Android Virtual Device (AVD)\n\n"
    "Installs the default Android\n"
    "virtual device emulator to test\n"
    "and run your mobile apps\n"
    "directly on this PC."
)
draw3.text((345, 220), desc_text, fill=(50, 50, 50, 255), font=font_small, spacing=4)

# Space info
draw3.text((35, 340), "Space required: 3.8 GB", fill=(50, 50, 50, 255), font=font_small)
draw3.text((35, 360), "Space available: 154.6 GB", fill=(50, 50, 50, 255), font=font_small)

# Clear button bar
draw3.rectangle([10, 425, w2-10, 475], fill=(245, 245, 245, 255))
draw3.line([(0, 424), (w2, 424)], fill=(215, 215, 215, 255), width=1)

# Buttons: < Back (active), Next > (active/blue), Cancel
draw3.rounded_rectangle([320, 434, 400, 464], radius=3, fill=(255, 255, 255, 255), outline=(200, 200, 200, 255))
draw3.text((342, 440), "< Back", fill=(0, 0, 0, 255), font=font_btn)

draw3.rounded_rectangle([410, 434, 490, 464], radius=3, fill=(255, 255, 255, 255), outline=(0, 103, 192, 255), width=2)
draw3.text((432, 440), "Next >", fill=(0, 0, 0, 255), font=font_btn)

draw3.rounded_rectangle([505, 434, 585, 464], radius=3, fill=(255, 255, 255, 255), outline=(200, 200, 200, 255))
draw3.text((525, 440), "Cancel", fill=(0, 0, 0, 255), font=font_btn)

img3.save("Step_03_Choose_Components.png")
print("Saved Step_03_Choose_Components.png")


# -------------------------------------------------------------
# 3. Step 4: Configuration Settings / Install Location
# -------------------------------------------------------------
img4 = base2.copy()
draw4 = ImageDraw.Draw(img4)

# Clear top banner text area
draw4.rectangle([180, 32, w2-10, 105], fill=(255, 255, 255, 255))
draw4.text((195, 45), "Configuration Settings", fill=(0, 0, 0, 255), font=font_subtitle)
draw4.text((215, 70), "Install Locations", fill=(80, 80, 80, 255), font=font_small)

# Clear main content area
draw4.rectangle([10, 108, w2-10, 420], fill=(245, 245, 245, 255))

draw4.text((35, 125), "Configuration Settings: Android Studio Installation Location", fill=(30, 30, 30, 255), font=font_body_bold)
draw4.text((35, 150), "The location specified must have at least 500 MB of free space.", fill=(60, 60, 60, 255), font=font_small)
draw4.text((35, 168), "Click Browse to choose a different folder.", fill=(60, 60, 60, 255), font=font_small)

draw4.text((35, 210), "Android Studio Installation Location:", fill=(30, 30, 30, 255), font=font_body)

# Path input box
draw4.rectangle([35, 235, 475, 265], fill=(255, 255, 255, 255), outline=(160, 160, 160, 255))
draw4.text((45, 241), r"C:\Program Files\Android\Android Studio", fill=(0, 0, 0, 255), font=font_body)

# Browse button
draw4.rounded_rectangle([485, 235, 575, 265], radius=3, fill=(255, 255, 255, 255), outline=(180, 180, 180, 255))
draw4.text((505, 241), "Browse...", fill=(0, 0, 0, 255), font=font_btn)

# Space info
draw4.text((35, 300), "Space required: 3.8 GB", fill=(50, 50, 50, 255), font=font_small)
draw4.text((35, 320), "Space available: 154.6 GB", fill=(50, 50, 50, 255), font=font_small)

# Clear button bar
draw4.rectangle([10, 425, w2-10, 475], fill=(245, 245, 245, 255))
draw4.line([(0, 424), (w2, 424)], fill=(215, 215, 215, 255), width=1)

# Buttons: < Back (active), Next > (active/blue), Cancel
draw4.rounded_rectangle([320, 434, 400, 464], radius=3, fill=(255, 255, 255, 255), outline=(200, 200, 200, 255))
draw4.text((342, 440), "< Back", fill=(0, 0, 0, 255), font=font_btn)

draw4.rounded_rectangle([410, 434, 490, 464], radius=3, fill=(255, 255, 255, 255), outline=(0, 103, 192, 255), width=2)
draw4.text((432, 440), "Next >", fill=(0, 0, 0, 255), font=font_btn)

draw4.rounded_rectangle([505, 434, 585, 464], radius=3, fill=(255, 255, 255, 255), outline=(200, 200, 200, 255))
draw4.text((525, 440), "Cancel", fill=(0, 0, 0, 255), font=font_btn)

img4.save("Step_04_Install_Location.png")
print("Saved Step_04_Install_Location.png")
