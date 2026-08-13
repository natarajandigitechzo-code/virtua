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
print(f"Reading newly uploaded Avalanche logo file: {latest}")

img = Image.open(latest).convert("RGBA")
pixels = img.load()
w, h = img.size

new_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
new_pixels = new_img.load()

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # Outer white background removal
        if r > 240 and g > 240 and b > 240 and a > 10:
            new_pixels[x, y] = (0, 0, 0, 0)
        else:
            new_pixels[x, y] = (r, g, b, a)

bbox = new_img.getbbox()
if bbox:
    new_img = new_img.crop(bbox)
    padded = Image.new("RGBA", (new_img.width + 20, new_img.height + 20), (0, 0, 0, 0))
    padded.paste(new_img, (10, 10))
    new_img = padded

p1 = os.path.join(out_dir1, "avalanche.png")
p2 = os.path.join(out_dir2, "avalanche.png")

new_img.save(p1, "PNG")
new_img.save(p2, "PNG")

print(f"Saved clean red Avalanche logo to both projects: size {new_img.size}")
