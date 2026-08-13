import os
from PIL import Image, ImageDraw, ImageFont

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

# Create Woodside Energy Logo (Red W curve + Woodside Energy text)
woodside_img = Image.new("RGBA", (300, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(woodside_img)
# Draw Woodside Red & Blue icon motif
draw.polygon([(10, 70), (30, 20), (50, 70), (70, 20), (90, 70)], fill="#ED1B2F")
draw.text((105, 30), "Woodside", fill="#002F6C", font_size=32)
draw.text((105, 65), "ENERGY", fill="#666666", font_size=16)
woodside_img.save(os.path.join(trusted_dir, "woodside.png"))

# Create Curtin University Logo (Gold/Black Crest + Curtin University text)
curtin_img = Image.new("RGBA", (340, 100), (255, 255, 255, 0))
draw_c = ImageDraw.Draw(curtin_img)
draw_c.rectangle([(10, 15), (75, 80)], fill="#E5A823")
draw_c.text((22, 28), "C", fill="#000000", font_size=46)
draw_c.text((90, 25), "Curtin", fill="#FFFFFF", font_size=34)
draw_c.text((90, 62), "University", fill="#E5A823", font_size=20)
curtin_img.save(os.path.join(trusted_dir, "curtin.png"))

print("Created Woodside Energy and Curtin University logos in original brand colors.")
