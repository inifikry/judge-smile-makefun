import os

TEXT = "This morning the warung lady remembered my coffee with no sugar, then slid a fried banana across the counter and winked like we'd planned it for years."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
