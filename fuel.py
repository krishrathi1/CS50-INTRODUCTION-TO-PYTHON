def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = map(int, fraction.split('/'))

            # Check for ZeroDivisionError
            if y == 0:
                raise ZeroDivisionError

            # Check that x is not greater than y
            if x > y:
                raise ValueError

            # Calculate the fuel level as a percentage
            percentage = (x / y) * 100

            # Determine output based on percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            break  # Exit the loop once valid input is processed

        except (ValueError, ZeroDivisionError):
            # Prompt the user again for invalid inputs
            continue

main()
