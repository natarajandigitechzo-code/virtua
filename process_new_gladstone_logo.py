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
    # Remove black background (make transparent)
    if r < 30 and g < 30 and b < 30:
        new_data.append((0, 0, 0, 0))
    else:
        # Keep the blue GPC ship emblem and Gladstone Ports text vibrant!
        new_data.append(item)

img.putdata(new_data)
out_path = os.path.join(trusted_dir, "gladstone_ports.png")
img.save(out_path, "PNG")
print("Successfully replaced Gladstone Ports Corporation logo!")
