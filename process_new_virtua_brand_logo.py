import os
from PIL import Image, ImageChops

user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets"

# Find the latest user uploaded file
files = [os.path.join(user_uploaded, f) for f in os.listdir(user_uploaded) if f.startswith("media__")]
latest_file = max(files, key=os.path.getmtime)
print(f"Latest user uploaded logo file: {latest_file}")

img = Image.open(latest_file).convert("RGBA")
datas = list(img.getdata())

# Replace white background pixels with transparent
new_data = []
for item in datas:
    r, g, b, a = item
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    else:
        # If text outline or thin arcs are light grey (R,G,B around 180-220), convert to crisp PURE WHITE for dark background
        if 150 < r < 230 and 150 < g < 230 and 150 < b < 230:
            new_data.append((255, 255, 255, a))
        else:
            # Keep gold/yellow Virtua text and lightning mark vibrant!
            new_data.append(item)

img.putdata(new_data)

# Auto-crop to content bounding box
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)
    # Add a small 10px padding
    padded = Image.new("RGBA", (img.width + 20, img.height + 20), (255, 255, 255, 0))
    padded.paste(img, (10, 10))
    img = padded

out_path = os.path.join(trusted_dir, "standalone_logo.png")
img.save(out_path, "PNG")
print("Successfully replaced Virtua brand logo with clean transparent full logo!")
