import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"

# Create Ethereum logo
eth_img = Image.new("RGBA", (360, 100), (0, 0, 0, 0))
draw = ImageDraw.Draw(eth_img)

# Polygon / Diamond coordinates for Ethereum emblem
# Draw diamond emblem
draw.polygon([(40, 15), (70, 50), (40, 65), (10, 50)], fill=(255, 255, 255, 255))
draw.polygon([(40, 68), (70, 52), (40, 85)], fill=(200, 200, 200, 255))
draw.polygon([(40, 68), (10, 52), (40, 85)], fill=(160, 160, 160, 255))

# Draw ETHEREUM text
try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

draw.text((95, 30), "ETHEREUM", fill=(255, 255, 255, 255), font=font)

eth_img.save(os.path.join(out_dir, "ethereum.png"), "PNG")
print("Saved ethereum.png")

# Create Polygon logo
poly_img = Image.new("RGBA", (360, 100), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(poly_img)

# Draw Polygon emblem (purple rounded polygon shape)
draw2.polygon([(40, 20), (65, 35), (65, 65), (40, 80), (15, 65), (15, 35)], fill=(130, 71, 229, 255))
draw2.polygon([(40, 32), (54, 41), (54, 59), (40, 68), (26, 59), (26, 41)], fill=(0, 0, 0, 255))

draw2.text((95, 30), "POLYGON", fill=(255, 255, 255, 255), font=font)
poly_img.save(os.path.join(out_dir, "polygon.png"), "PNG")
print("Saved polygon.png")
