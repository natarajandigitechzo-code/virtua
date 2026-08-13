import os
from PIL import Image

out_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\blockchains"

for filename in os.listdir(out_dir):
    if filename.endswith(".png"):
        fpath = os.path.join(out_dir, filename)
        img = Image.open(fpath)
        w, h = img.size
        if h > w * 1.3:
            print(f"Rotating vertical image {filename} ({w}x{h})...")
            # Rotate 270 degrees counterclockwise (or 90 degrees clockwise) so text reads horizontally left-to-right!
            img = img.rotate(270, expand=True)
            # Crop non-transparent
            bbox = img.getbbox()
            if bbox:
                img = img.crop(bbox)
                padded = Image.new("RGBA", (img.width + 20, img.height + 20), (0, 0, 0, 0))
                padded.paste(img, (10, 10))
                img = padded
            img.save(fpath, "PNG")
            print(f"Saved rotated {filename}: {img.size}")

print("Orientation check complete!")
