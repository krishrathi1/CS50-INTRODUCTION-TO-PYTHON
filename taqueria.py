def main():
    # Define the menu as a dictionary
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            # Prompt user for an item, treating the input case-insensitively
            item = input("Item: ").strip().title()

            # Check if the item exists in the menu
            if item in menu:
                total_cost += menu[item]
                print(f"Total: ${total_cost:.2f}")

        except EOFError:
            # If control-D is pressed, break the loop and end the program
            print("\n")
            break

main()
