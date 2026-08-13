import os
from PIL import Image

out_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"
os.makedirs(out_dir, exist_ok=True)

# Explicit file mapping from recent uploaded images:
# BNB Chain: media__1785502953727.png
# Avalanche: media__1785496629782.png
# Solana: media__1785502953730.png
# XRP: media__1785502953770.jpg
# Base: media__1785502999978.png

files_map = {
    "bnb.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785502953727.png",
    "avalanche.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785496629782.png",
    "solana.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785502953730.png",
    "xrp.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785502953770.jpg",
    "base.png": r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded\media__1785502999978.png",
}

for name, fpath in files_map.items():
    if not os.path.exists(fpath):
        # try temp directory
        alt = os.path.join(r"C:\Users\NATARAJAN\.gemini\antigravity\brain\tempmediaStorage", os.path.basename(fpath))
        if os.path.exists(alt):
            fpath = alt

    img = Image.open(fpath).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    new_pixels = new_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Strip pure white / near-white background
            if r > 230 and g > 230 and b > 230:
                new_pixels[x, y] = (0, 0, 0, 0)
            else:
                # If dark text/emblem (like black Avalanche/Base text), make pure white for dark UI
                if r < 45 and g < 45 and b < 45:
                    new_pixels[x, y] = (255, 255, 255, a)
                else:
                    new_pixels[x, y] = (r, g, b, a)
                    
    bbox = new_img.getbbox()
    if bbox:
        new_img = new_img.crop(bbox)
        # Pad 10px
        padded = Image.new("RGBA", (new_img.width + 20, new_img.height + 20), (0, 0, 0, 0))
        padded.paste(new_img, (10, 10))
        new_img = padded
        
    save_p = os.path.join(out_dir, name)
    new_img.save(save_p, "PNG")
    print(f"Saved clean {name}: size {new_img.size}")

print("All 5 blockchain logos successfully processed and saved!")
