import os
from PIL import Image, ImageDraw, ImageFont

user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
out_dir1 = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"
out_dir2 = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\digitechzo-landing-page\assets\blockchains"

# Latest file
all_files = [os.path.join(user_uploaded, f) for f in os.listdir(user_uploaded) if f.startswith("media__")]
all_files.sort(key=os.path.getmtime, reverse=True)
latest_hedera = all_files[0]
print(f"Reading {latest_hedera}")

img = Image.open(latest_hedera).convert("RGBA")
pixels = img.load()
w, h = img.size

# We want the circle to be bright (pure white circle with black 'H' inside) and the text 'Hedera' to be pure white #FFFFFF!
new_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
new_pixels = new_img.load()

# Let's inspect pixel values in emblem vs text
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if a < 10 or (r > 230 and g > 230 and b > 230):
            # Background -> transparent
            new_pixels[x, y] = (0, 0, 0, 0)
        else:
            # Check if this pixel is inside the emblem circle area (left 30% of width)
            if x < w * 0.32:
                # Black circle background -> make it pure white (255, 255, 255)
                # White 'H' inside -> make it pure black (10, 10, 10) for maximum contrast!
                if r < 80 and g < 80 and b < 80:
                    new_pixels[x, y] = (255, 255, 255, 255)
                else:
                    new_pixels[x, y] = (10, 10, 12, 255)
            else:
                # Text area: convert black "Hedera" text to pure white
                if r < 80 and g < 80 and b < 80:
                    new_pixels[x, y] = (255, 255, 255, 255)
                else:
                    new_pixels[x, y] = (r, g, b, a)

bbox = new_img.getbbox()
if bbox:
    new_img = new_img.crop(bbox)
    padded = Image.new("RGBA", (new_img.width + 24, new_img.height + 24), (0, 0, 0, 0))
    padded.paste(new_img, (12, 12))
    new_img = padded

p1 = os.path.join(out_dir1, "hedera.png")
p2 = os.path.join(out_dir2, "hedera.png")

new_img.save(p1, "PNG")
new_img.save(p2, "PNG")

print(f"Saved ultra clear Hedera logo: size {new_img.size}")
