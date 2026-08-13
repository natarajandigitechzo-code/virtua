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
    # Remove white background
    if r > 235 and g > 235 and b > 235:
        new_data.append((255, 255, 255, 0))
    else:
        # Convert dark text "smec an company" (low R & G) into crisp WHITE for black background!
        if r < 80 and g < 90:
            new_data.append((255, 255, 255, a))
        else:
            new_data.append(item)

img.putdata(new_data)
out_path = os.path.join(trusted_dir, "smec.png")
img.save(out_path, "PNG")
print("Successfully replaced SMEC logo with new blue ribbon infinity emblem logo!")
