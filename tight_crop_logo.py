import os
from PIL import Image

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets"
logo_path = os.path.join(trusted_dir, "standalone_logo.png")

img = Image.open(logo_path).convert("RGBA")

# Auto-crop to exact non-transparent bounding box with 0px extra padding
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

img.save(logo_path, "PNG")
print("Tight cropped logo icon with 0px margin!")
