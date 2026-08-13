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

# Sort by modification time reverse
all_files.sort(key=os.path.getmtime, reverse=True)
latest_5 = all_files[:5]
print("Found latest 5 uploaded blockchain logo files:")
for f in latest_5:
    print(f)

# Function to make white background transparent and make black text white for dark background
def process_logo(img_path, filename):
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    new_pixels = new_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # White background removal
            if r > 235 and g > 235 and b > 235:
                new_pixels[x, y] = (0, 0, 0, 0)
            else:
                # If pixel is dark/black (text like AVALANCHE or BASE text), convert to white for dark background
                if r < 40 and g < 40 and b < 40:
                    new_pixels[x, y] = (255, 255, 255, a)
                else:
                    new_pixels[x, y] = (r, g, b, a)
    
    # Auto-crop to content
    bbox = new_img.getbbox()
    if bbox:
        new_img = new_img.crop(bbox)
        # Pad with 10px
        padded = Image.new("RGBA", (new_img.width + 20, new_img.height + 20), (0, 0, 0, 0))
        padded.paste(new_img, (10, 10))
        new_img = padded
        
    save_path = os.path.join(out_dir, filename)
    new_img.save(save_path, "PNG")
    print(f"Saved {filename}: {new_img.size}")

# Match latest 5 files to filenames
# Order of upload in prompt: Base, XRP, Solana, Avalanche, BNB Chain
# Let's inspect each file to identify or process in order
for i, f in enumerate(latest_5):
    process_logo(f, f"blockchain_{i+1}.png")

