import sys
import os

def main():
    # Check if the user provided exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")

    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith('.py'):
        sys.exit("Error: File must end with .py")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: File {filename} does not exist")

    # Count lines of code
    count_lines_of_code(filename)

def count_lines_of_code(filename):
    try:
        with open(filename, 'r') as file:
            loc = 0  # Line of code count

            for line in file:
                # Strip whitespace from the line
                stripped_line = line.lstrip()

                # Check if the line is not blank and not a comment
                if stripped_line and not stripped_line.startswith('#'):
                    loc += 1

            print(loc)  # Output the number of lines of code
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
