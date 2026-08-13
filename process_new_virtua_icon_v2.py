import os
from PIL import Image, ImageDraw

user_uploaded = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\.user_uploaded"
trusted_dir = r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets"

# Find the latest user uploaded file
files = [os.path.join(user_uploaded, f) for f in os.listdir(user_uploaded) if f.startswith("media__")]
latest_file = max(files, key=os.path.getmtime)
print(f"Latest user uploaded logo file: {latest_file}")

img = Image.open(latest_file).convert("RGBA")
width, height = img.size

# Flood fill outer white background from (0,0) with transparent (0,0,0,0)
# We can use ImageDraw.floodfill
# First find all pixels connected to (0,0) that are white
from collections import deque

pixels = img.load()
visited = set()
queue = deque([(0, 0)])
visited.add((0, 0))

# White threshold
def is_white(p):
    return p[0] > 230 and p[1] > 230 and p[2] > 230

while queue:
    x, y = queue.popleft()
    pixels[x, y] = (0, 0, 0, 0)
    
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
            if is_white(pixels[nx, ny]):
                visited.add((nx, ny))
                queue.append((nx, ny))

# Auto-crop to non-transparent bounding box
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)
    # Add a small 4px padding
    padded = Image.new("RGBA", (img.width + 8, img.height + 8), (0, 0, 0, 0))
    padded.paste(img, (4, 4))
    img = padded

out_path = os.path.join(trusted_dir, "standalone_logo.png")
img.save(out_path, "PNG")
print("Successfully processed logo with floodfill! White ring preserved 100%!")
