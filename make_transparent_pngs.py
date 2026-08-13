import os
from PIL import Image

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

for filename in os.listdir(trusted_dir):
    filepath = os.path.join(trusted_dir, filename)
    if os.path.isfile(filepath) and (filename.endswith(".png") or filename.endswith(".jpg")):
        try:
            img = Image.open(filepath).convert("RGBA")
            datas = img.getdata()
            
            new_data = []
            for item in datas:
                # If pixel is near-white (R>220, G>220, B>220), make it transparent alpha=0
                if item[0] > 220 and item[1] > 220 and item[2] > 220:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            
            img.putdata(new_data)
            
            base, _ = os.path.splitext(filename)
            out_path = os.path.join(trusted_dir, f"{base}.png")
            img.save(out_path, "PNG")
            print(f"Converted & cleaned: {filename} -> {base}.png")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
