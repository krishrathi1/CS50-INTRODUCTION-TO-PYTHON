def main():
    grocery_list = {}

    while True:
        try:
            # Prompt the user for an item
            item = input().strip().lower()

            # Increment the item count in the grocery list
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            # Break the loop when control-D is pressed
            break

    # Sort the items alphabetically and print the results
    for item in sorted(grocery_list.keys()):
        count = grocery_list[item]
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
