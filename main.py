import os
print("importing rembg")
import rembg
print("import successful")
from PIL import Image

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def remove_bgs():
    for filename in os.listdir(INPUT_DIR):
        print(filename)
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        try:
            input_img = Image.open(input_path)
        except Exception:
            print(f"failed to open {filename}")
            continue

        try:
            output_img = rembg.remove(input_img, 
                alpha_matting=True, alpha_matting_foreground_threshold=270,alpha_matting_background_threshold=20, alpha_matting_erode_size=11, 
                post_process_mask=True
            )
        except Exception:
            print(f"failed to remove background from {filename} with post processing")
            try:
                output_img = rembg.remove(input_img)
            except Exception:
                print(f"failed to remove background from {filename}")  
                continue

        try:
            output_img.save(output_path, format="PNG")
        except Exception:
            print(f"failed to save {filename}")

if __name__ == "__main__":
    remove_bgs()