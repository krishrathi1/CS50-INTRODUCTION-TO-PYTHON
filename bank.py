# bank.py

def main():
    # Prompt the user for a greeting
    greeting = input("Greeting: ").strip().lower()

    # Call the bank function to get the amount
    amount = bank(greeting)

    # Print the amount
    print(f"${amount}")

def bank(greeting):
    # Check if the greeting starts with "hello"
    if greeting.startswith("hello"):
        return 0
    # Check if the greeting starts with "h"
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

main()
