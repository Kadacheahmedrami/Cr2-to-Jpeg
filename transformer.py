import os
import sys
import rawpy
from PIL import Image

def convert_cr2_to_jpeg(input_path, output_path):
    try:
        with rawpy.imread(input_path) as raw:
            rgb_image = raw.postprocess()
        Image.fromarray(rgb_image).save(output_path, format="JPEG")
        print(f"Converted: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Failed to convert {input_path}: {e}")

if __name__ == "__main__":
    input_dir = sys.argv[1] if len(sys.argv) == 2 else os.getcwd()
    if not os.path.isdir(input_dir):
        print(f"Error: Directory '{input_dir}' does not exist.")
        sys.exit(1)
    
    os.makedirs('images', exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".cr2"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(input_dir, "images", os.path.splitext(filename)[0] + ".jpeg")
            convert_cr2_to_jpeg(input_file, output_file)
