import os
from PIL import Image

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

for filename in os.listdir(trusted_dir):
    if filename.endswith(".png"):
        filepath = os.path.join(trusted_dir, filename)
        try:
            img = Image.open(filepath).convert("RGBA")
            datas = list(img.getdata())
            
            new_data = []
            for item in datas:
                r, g, b, a = item
                if a > 30:
                    # If pixel is dark/black text (low RGB), convert to crisp WHITE!
                    if r < 110 and g < 110 and b < 110:
                        new_data.append((255, 255, 255, a))
                    else:
                        new_data.append(item)
                else:
                    new_data.append((0, 0, 0, 0))
            
            img.putdata(new_data)
            img.save(filepath, "PNG")
            print(f"Converted black text to white for: {filename}")
        except Exception as e:
            print(f"Error {filename}: {e}")
