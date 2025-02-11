import random

def main():
    # Prompt the user for a positive integer level
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

    # Randomly generate an integer between 1 and level (inclusive)
    secret_number = random.randint(1, level)

    # Initialize the guessing process
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Please enter a positive integer.")
            continue

        # Compare guess to the secret number
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop if the guess is correct

if __name__ == "__main__":
    main()
