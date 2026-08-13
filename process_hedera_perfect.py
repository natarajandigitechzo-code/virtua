import os
from PIL import Image

temp_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\tempmediaStorage"
user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
out_dir1 = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"
out_dir2 = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\digitechzo-landing-page\assets\blockchains"

os.makedirs(out_dir1, exist_ok=True)
os.makedirs(out_dir2, exist_ok=True)

# List all media files from both temp and user_uploaded sorted by time
all_files = []
for d in [temp_dir, user_uploaded]:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.startswith("media__"):
                all_files.append(os.path.join(d, f))

all_files.sort(key=os.path.getmtime, reverse=True)
latest = all_files[0]
print(f"Reading newly uploaded Hedera logo file: {latest}")

img = Image.open(latest).convert("RGBA")
pixels = img.load()
w, h = img.size

new_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
new_pixels = new_img.load()

# Process pixel by pixel:
# White canvas background (r > 220, g > 220, b > 220) -> Transparent (0, 0, 0, 0)
# Emblem circle (black circle background) -> White circle (255, 255, 255, 255)
# Emblem 'H' symbol inside circle (white) -> Dark black (10, 10, 12, 255) inside circle
# Text 'Hedera' (black text) -> Pure White (255, 255, 255, 255)

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # White background removal
        if r > 215 and g > 215 and b > 215:
            # Check if this pixel is inside the emblem circle area (left 35% of width)
            # In the original image: circle background is black (r,g,b < 60), 'H' is white (r,g,b > 215) inside circle!
            if x < w * 0.35:
                # White 'H' inside circle -> make it pure white or black depending on circle inverted state
                # Let's inspect: if circle is black, emblem area has black circle + white H.
                new_pixels[x, y] = (0, 0, 0, 0) # outer background is white
            else:
                new_pixels[x, y] = (0, 0, 0, 0) # outer background is white
        else:
            # Dark pixels (circle background OR text)
            if x < w * 0.35:
                # Circle background -> convert to bright white emblem circle (255, 255, 255, 255)
                new_pixels[x, y] = (255, 255, 255, 255)
            else:
                # 'Hedera' text -> convert black text to pure white (255, 255, 255, 255)
                new_pixels[x, y] = (255, 255, 255, 255)

# Now fix the 'H' symbol inside the circle so the 'H' shows as crisp dark lines inside white circle!
# Re-scan emblem area:
for y in range(h):
    for x in range(int(w * 0.35)):
        r, g, b, a = pixels[x, y]
        # If original pixel was white (r,g,b > 215) AND surrounded by dark circle pixels (meaning it's the 'H' symbol)
        if r > 215 and g > 215 and b > 215:
            # Check if neighboring pixels are dark (circle)
            is_inside_circle = False
            for dx in [-5, 0, 5]:
                for dy in [-5, 0, 5]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        pr, pg, pb, _ = pixels[nx, ny]
                        if pr < 60 and pg < 60 and pb < 60:
                            is_inside_circle = True
                            break
            if is_inside_circle:
                new_pixels[x, y] = (10, 10, 12, 255)

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

print(f"Saved perfect Hedera logo: size {new_img.size}")
