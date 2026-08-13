import os
from PIL import Image, ImageEnhance

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\trusted"

for filename in os.listdir(trusted_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        filepath = os.path.join(trusted_dir, filename)
        try:
            img = Image.open(filepath).convert("RGBA")
            
            # Enhance sharpness & contrast for crisp enterprise rendering
            enhancer = ImageEnhance.Sharpness(img)
            img_sharp = enhancer.enhance(1.8)
            
            # Save high quality PNG
            base, _ = os.path.splitext(filename)
            out_path = os.path.join(trusted_dir, f"{base}.png")
            img_sharp.save(out_path, "PNG", optimize=True)
            print(f"Enhanced quality for: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
