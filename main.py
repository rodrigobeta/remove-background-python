# remove image background using python

from rembg import remove
from PIL import Image
import os
import sys

def remove_background(input_path, output_path):
    """
    Remove background from image and save result
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save output image
    """
    try:
        # Verify input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image '{input_path}' not found")

        # Open and process image
        print("Processing image...")
        input_image = Image.open(input_path)
        
        # Remove background
        output_image = remove(input_image)
        
        # Save processed image
        output_image.save(output_path)
        print(f"Image saved successfully as '{output_path}'")
        
        # Display the output image
        output_image.show()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    # Define input and output paths
    input_path = 'input.png'  # Change this to your input image name
    output_path = 'output.png'
    
    # Process the image
    remove_background(input_path, output_path)

if __name__ == "__main__":
    main()

