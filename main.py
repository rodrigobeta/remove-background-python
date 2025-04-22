from rembg import remove
from PIL import Image
import os
import sys

def remove_background(input_path: str, output_path: str) -> None:
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image '{input_path}' not found")

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        output_image.show()

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    input_path = 'input.png'
    output_path = 'output.png'
    remove_background(input_path, output_path)

if __name__ == "__main__":
    main()