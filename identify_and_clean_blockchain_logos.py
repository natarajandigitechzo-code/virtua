import os
from PIL import Image

temp_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\tempmediaStorage"
user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
out_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"

os.makedirs(out_dir, exist_ok=True)

# Find specific files by size/characteristics
all_files = []
for d in [temp_dir, user_uploaded]:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.startswith("media__"):
                all_files.append(os.path.join(d, f))

def clean_white_bg(img, invert_black=True):
    img = img.convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    new_pixels = new_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # White background removal
            if r > 225 and g > 225 and b > 225:
                new_pixels[x, y] = (0, 0, 0, 0)
            else:
                if invert_black and r < 50 and g < 50 and b < 50:
                    # Invert black text/symbols to white for dark background
                    new_pixels[x, y] = (255, 255, 255, a)
                else:
                    new_pixels[x, y] = (r, g, b, a)
                    
    bbox = new_img.getbbox()
    if bbox:
        new_img = new_img.crop(bbox)
        padded = Image.new("RGBA", (new_img.width + 24, new_img.height + 24), (0, 0, 0, 0))
        padded.paste(new_img, (12, 12))
        new_img = padded
    return new_img

# Process each uploaded image by matching their content
for fpath in all_files:
    try:
        im = Image.open(fpath)
        w, h = im.size
        # BNB Chain image (media__1785502953727.png or similar, ~500x400)
        # Let's inspect images by aspect ratio or size
        print(f"File {os.path.basename(fpath)} size: {w}x{h}")
        
        cleaned = clean_white_bg(im)
        # Save based on file signature
        if w == 500 and h == 375:
            cleaned.save(os.path.join(out_dir, "bnb.png"), "PNG")
            print("Saved bnb.png")
        elif w == 400 and h == 400:
            cleaned.save(os.path.join(out_dir, "avalanche.png"), "PNG")
            print("Saved avalanche.png")
        elif w == 300 and h == 300:
            cleaned.save(os.path.join(out_dir, "solana.png"), "PNG")
            print("Saved solana.png")
        elif w == 340 and h == 340:
            cleaned.save(os.path.join(out_dir, "xrp.png"), "PNG")
            print("Saved xrp.png")
        elif w == 1000 or w == 1200 or (w == 1000 and h == 563) or "1785502999978" in fpath or "1785502953770" in fpath:
            # Base logo
            if "1785502999978" in fpath:
                cleaned.save(os.path.join(out_dir, "base.png"), "PNG")
                print("Saved base.png")
    except Exception as e:
        print(f"Error reading {fpath}: {e}")

# Fallback: create high-res SVG/PNG vectors for Ethereum, Polygon, Avalanche, BNB, Solana, XRP, Base
print("Processing complete!")
