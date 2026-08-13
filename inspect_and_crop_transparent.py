import os
from PIL import Image

trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets"
logo_path = os.path.join(trusted_dir, "standalone_logo.png")

img = Image.open(logo_path).convert("RGBA")
width, height = img.size

min_x, min_y, max_x, max_y = width, height, 0, 0

pixels = img.load()
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # Look for the circle pixels (which are either dark black interior, yellow mark, or white ring)
        if a > 20 and not (r > 245 and g > 245 and b > 245):
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Original size: {width}x{height}")
print(f"Extracted logo content bounds: x: [{min_x}, {max_x}], y: [{min_y}, {max_y}]")

if max_x > min_x and max_y > min_y:
    img_cropped = img.crop((min_x, min_y, max_x + 1, max_y + 1))
    print(f"New cropped size: {img_cropped.size}")
    img_cropped.save(logo_path, "PNG")
    print("Successfully cropped to EXACT tight circle graphic edge!")
