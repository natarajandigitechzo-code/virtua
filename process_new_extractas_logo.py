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
    # Remove white background pixels (R>235, G>235, B>235)
    if r > 235 and g > 235 and b > 235:
        new_data.append((255, 255, 255, 0))
    else:
        # Convert blue text "Extractas Bioscience" (high B, low R) into crisp WHITE for black background!
        if r < 50 and b > 120:
            new_data.append((255, 255, 255, a))
        else:
            # Keep teal circular cell emblem vibrant!
            new_data.append(item)

img.putdata(new_data)
out_path = os.path.join(trusted_dir, "extractas.png")
img.save(out_path, "PNG")
print("Successfully replaced Extractas Bioscience logo with teal cell emblem logo!")
