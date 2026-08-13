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
    # Remove white & transparent checkerboard grey background pixels (R>200, G>200, B>200)
    if r > 200 and g > 200 and b > 200:
        new_data.append((255, 255, 255, 0))
    else:
        # Convert dark blue text "NSW GOVERNMENT Health" (low R, high B/G) into crisp WHITE for black background!
        if r < 80 and b > 80:
            new_data.append((255, 255, 255, a))
        else:
            # Keep red waratah flower petals vibrant!
            new_data.append(item)

img.putdata(new_data)
out_path = os.path.join(trusted_dir, "nsw_health.png")
img.save(out_path, "PNG")
print("Successfully replaced NSW Health logo with red Waratah flower emblem logo!")
