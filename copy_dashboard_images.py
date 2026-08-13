import os
import shutil

img1 = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\rwa_dashboard_portfolio_1785587695640.jpg"
img2 = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\rwa_dashboard_minting_1785587710913.jpg"
img3 = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\rwa_dashboard_orderbook_1785587725139.jpg"
img4 = r"C:\Users\NATARAJAN\.gemini\antigravity\brain\9c03ef69-3098-49ed-bcb3-4ce65487e708\rwa_dashboard_analytics_1785587740532.jpg"

targets = [
    r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\rwa-landing-page\assets\dashboard",
    r"C:\Users\NATARAJAN\.gemini\antigravity\scratch\digitechzo-landing-page\assets\dashboard"
]

for t in targets:
    os.makedirs(t, exist_ok=True)
    shutil.copy(img1, os.path.join(t, "portfolio.jpg"))
    shutil.copy(img2, os.path.join(t, "minting.jpg"))
    shutil.copy(img3, os.path.join(t, "orderbook.jpg"))
    shutil.copy(img4, os.path.join(t, "analytics.jpg"))

print("Copied all 4 dashboard mockup images to asset directories successfully!")
