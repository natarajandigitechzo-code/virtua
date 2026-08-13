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
print(f"Latest uploaded Hedera logo file: {latest}")

img = Image.open(latest).convert("RGBA")
pixels = img.load()
w, h = img.size

new_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
new_pixels = new_img.load()

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # White background removal
        if r > 220 and g > 220 and b > 220:
            new_pixels[x, y] = (0, 0, 0, 0)
        else:
            # If dark text ("Hedera" text to the right of emblem), convert to pure white #FFFFFF for dark UI
            # Keep emblem circle dark/white intact
            if x > w * 0.3 and r < 60 and g < 60 and b < 60:
                new_pixels[x, y] = (255, 255, 255, a)
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

print(f"Saved clean Hedera logo to both projects: size {new_img.size}")
