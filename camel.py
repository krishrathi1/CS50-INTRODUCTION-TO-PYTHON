def main():
    # Prompt the user for a camel case variable name
    camel_case = input("Enter a variable name in camel case: ").strip()

    # Convert to snake case
    snake_case = convert_to_snake_case(camel_case)

    # Output the snake case variable name
    print("Variable name in snake case:", snake_case)

def convert_to_snake_case(camel_case):
    # Initialize an empty string for the snake case result
    snake_case = ""

    # Iterate over each character in the camel case string
    for char in camel_case:
        # If the character is uppercase, add an underscore and convert to lowercase
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    return snake_case

# Run the main function
if __name__ == "__main__":
    main()
