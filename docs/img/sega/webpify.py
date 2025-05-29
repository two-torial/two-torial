import os
from PIL import Image

def recursive_convert(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".png"):
                png_path = os.path.join(root, file)
                webp_path = os.path.splitext(png_path)[0] + ".webp"

                try:
                    with Image.open(png_path) as img:
                        img.save(webp_path, "WEBP", lossless=True)
                    os.remove(png_path)
                    print(f"Converted and removed: {png_path}")
                except Exception as e:
                    print(f"Failed to convert {png_path}: {e}")

if __name__ == "__main__":
    recursive_convert(".")