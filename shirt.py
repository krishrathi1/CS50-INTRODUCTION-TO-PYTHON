import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for exactly two command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Define valid image extensions
    valid_extensions = ('.jpg', '.jpeg', '.png')

    # Check if the input and output file names have valid extensions
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input or output format")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Check if the input file exists
    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    # Open the input image and the shirt image
    try:
        input_image = Image.open(input_path)
        shirt = Image.open("shirt.png")

        # Resize and crop the input image to fit the shirt
        input_image = ImageOps.fit(input_image, shirt.size)

        # Overlay the shirt on the input image
        input_image.paste(shirt, shirt)

        # Save the resulting image to the output path
        input_image.save(output_path)

        print(f"Successfully saved the shirted image as {output_path}")

    except Exception as e:
        sys.exit(f"Error opening images: {e}")

if __name__ == "__main__":
    main()
