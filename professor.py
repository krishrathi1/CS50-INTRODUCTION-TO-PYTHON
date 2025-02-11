import random

def main():
    level = get_level()  # Get the user's level
    score = 0  # Initialize the score

    for _ in range(10):  # Generate 10 problems
        x = generate_integer(level)  # Generate first number
        y = generate_integer(level)  # Generate second number
        correct_answer = x + y  # Calculate the correct answer
        attempts = 0  # Count attempts for this problem

        while attempts < 3:  # Allow up to 3 attempts
            try:
                answer = int(input(f"{x} + {y} = "))  # Prompt for the answer
                if answer == correct_answer:
                    score += 1  # Increment score for correct answer
                    break  # Exit the attempts loop on correct answer
                else:
                    print("EEE")  # Incorrect answer feedback
                    attempts += 1  # Increment the attempts counter
            except ValueError:
                print("EEE")  # Handle non-integer input
                attempts += 1  # Increment the attempts counter

        # If the user fails to answer correctly after 3 attempts
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")  # Show the correct answer

    # Output the user's score
    print(f"Score: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)  # Single digit
    elif level == 2:
        return random.randint(10, 99)  # Two digits
    elif level == 3:
        return random.randint(100, 999)  # Three digits
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
