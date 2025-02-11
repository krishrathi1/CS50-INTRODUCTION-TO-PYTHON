import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # Random font if no arguments
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Specific font if two arguments provided
        font = sys.argv[2]
        if font not in figlet.getFonts():
            print(f"Error: '{font}' is not a valid font.")
            sys.exit(1)
    else:
        # Invalid usage
        print("Usage: python figlet.py [-f | --font] <font>")
        sys.exit(1)

    # Set the font
    figlet.setFont(font=font)

    # Prompt for text input
    text = input("Text: ")

    # Output the text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
