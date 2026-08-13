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
    # Remove outer white background pixels (R>245, G>245, B>245)
    if r > 245 and g > 245 and b > 245:
        new_data.append((255, 255, 255, 0))
    else:
        # Keep orange arrow, orange dot, and white text crisp and vibrant!
        new_data.append(item)

img.putdata(new_data)
out_path = os.path.join(trusted_dir, "xsights.png")
img.save(out_path, "PNG")
print("Successfully replaced xSights logo with orange chevron arrow + white text logo!")
