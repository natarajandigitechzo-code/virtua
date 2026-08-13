import os
from PIL import Image

user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets"

# Find the latest user uploaded file
files = [os.path.join(user_uploaded, f) for f in os.listdir(user_uploaded) if f.startswith("media__")]
latest_file = max(files, key=os.path.getmtime)
print(f"Latest user uploaded logo file: {latest_file}")

img = Image.open(latest_file).convert("RGBA")
datas = list(img.getdata())

# Replace white background pixels outside the logo circle with transparent
new_data = []
for item in datas:
    r, g, b, a = item
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    else:
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
print("Successfully replaced standalone logo icon with clean transparent circular icon!")
