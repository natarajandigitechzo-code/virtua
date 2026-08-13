import os
from PIL import Image

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

for filename in os.listdir(trusted_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        filepath = os.path.join(trusted_dir, filename)
        try:
            img = Image.open(filepath).convert("RGBA")
            
            # Find non-white non-transparent bounding box
            # Convert pixels near white to transparent first
            datas = img.getdata()
            newData = []
            for item in datas:
                # near white or transparent
                if (item[0] > 245 and item[1] > 245 and item[2] > 245) or item[3] < 10:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            
            bbox = img.getbbox()
            if bbox:
                # Crop tightly around letters and graphics
                cropped = img.crop(bbox)
                
                # Add a small 10px clean margin around letters
                margin = 10
                new_img = Image.new("RGBA", (cropped.width + margin*2, cropped.height + margin*2), (255, 255, 255, 255))
                new_img.paste(cropped, (margin, margin), cropped)
                
                base, _ = os.path.splitext(filename)
                save_path = os.path.join(trusted_dir, f"{base}.png")
                new_img.save(save_path, "PNG")
                print(f"Successfully cropped & enlarged letters/graphics for: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
