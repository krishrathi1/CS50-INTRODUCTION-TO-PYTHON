import emoji

def main():
    # Prompt the user for input
    user_input = input("Enter a message: ")

    # Convert the input to its emojized version
    emojized_message = emoji.emojize(user_input, language='alias')

    # Output the emojized message
    print(emojized_message)

if __name__ == "__main__":
    main()
