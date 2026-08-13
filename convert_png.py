import os
from PIL import Image

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

for filename in os.listdir(trusted_dir):
    filepath = os.path.join(trusted_dir, filename)
    if os.path.isfile(filepath):
        try:
            img = Image.open(filepath).convert("RGBA")
            
            # Convert white/near-white pixels to transparent for crisp PNGs
            datas = img.getdata()
            newData = []
            for item in datas:
                # If pixel is near white (R,G,B > 240)
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)

            base, ext = os.path.splitext(filename)
            png_path = os.path.join(trusted_dir, f"{base}.png")
            img.save(png_path, "PNG")
            print(f"Converted {filename} -> {base}.png")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
