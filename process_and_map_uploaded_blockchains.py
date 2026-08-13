import os
from PIL import Image

out_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"
os.makedirs(out_dir, exist_ok=True)

files_map = {
    "stellar.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785574261602.png",
    "arbitrum.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785574275300.png",
    "solana.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785574348872.png",
    "xrp.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785574365009.jpg",
}

def make_clean_transparent_dark_theme(img_path, filename):
    img = Image.open(img_path).convert("RGBA")
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
                # If dark text/symbol (like Stellar black text or Arbitrum dark navy background element), convert to white or keep emblem colors
                # For dark text (r,g,b < 50), invert to pure white #FFFFFF for dark obsidian background
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
    print(f"Processed {filename}: size {new_img.size}")

for name, fpath in files_map.items():
    if os.path.exists(fpath):
        make_clean_transparent_dark_theme(fpath, name)

print("All uploaded blockchain logos processed successfully!")
