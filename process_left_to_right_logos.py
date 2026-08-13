import os
from PIL import Image

temp_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\tempmediaStorage"
user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
out_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"

os.makedirs(out_dir, exist_ok=True)

# List all media files from both temp and user_uploaded sorted by time
all_files = []
for d in [temp_dir, user_uploaded]:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.startswith("media__"):
                all_files.append(os.path.join(d, f))

all_files.sort(key=os.path.getmtime, reverse=True)
latest_4 = all_files[:4]
print("Found latest 4 uploaded blockchain logo files:")
for f in latest_4:
    print(f)

def clean_white_bg(img_path, filename):
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    new_pixels = new_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # White background removal
            if r > 230 and g > 230 and b > 230:
                new_pixels[x, y] = (0, 0, 0, 0)
            else:
                # If dark text/symbol (like Stellar black text or circle), convert to pure white for dark UI
                if r < 50 and g < 50 and b < 50:
                    new_pixels[x, y] = (255, 255, 255, a)
                else:
                    new_pixels[x, y] = (r, g, b, a)
                    
    bbox = new_img.getbbox()
    if bbox:
        new_img = new_img.crop(bbox)
        padded = Image.new("RGBA", (new_img.width + 24, new_img.height + 24), (0, 0, 0, 0))
        padded.paste(new_img, (12, 12))
        new_img = padded
        
    save_path = os.path.join(out_dir, filename)
    new_img.save(save_path, "PNG")
    print(f"Saved {filename}: {new_img.size}")

for i, f in enumerate(latest_4):
    clean_white_bg(f, f"new_blockchain_{i+1}.png")

