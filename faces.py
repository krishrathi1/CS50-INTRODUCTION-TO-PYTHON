# faces.py

# Define the convert function
def convert(text):
    # Replace emoticons with their corresponding emoji
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

# Define the main function
def main():
    # Prompt the user for input
    user_input = input("Enter a sentence with emoticons: ")
    # Call the convert function and print the result
    print(convert(user_input))

# Call the main function
if __name__ == "__main__":
    main()
