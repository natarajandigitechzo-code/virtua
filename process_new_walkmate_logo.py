import os
from PIL import Image

user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

# Find the latest user uploaded file
files = [os.path.join(user_uploaded, f) for f in os.listdir(user_uploaded) if f.startswith("media__")]
latest_file = max(files, key=os.path.getmtime)
print(f"Latest user uploaded logo file: {latest_file}")

img = Image.open(latest_file).convert("RGBA")
datas = list(img.getdata())

new_data = []
for item in datas:
    r, g, b, a = item
    # Remove outer white background pixels (R>240, G>240, B>240)
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    else:
        # Keep green badge, white text, and red footprint dots vibrant!
        new_data.append(item)

img.putdata(new_data)
out_path = os.path.join(trusted_dir, "walkmate.png")
img.save(out_path, "PNG")
print("Successfully replaced Walkmate logo with red footprint + green badge logo!")
