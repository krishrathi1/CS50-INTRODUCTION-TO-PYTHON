def main():
    names = []

    # Prompt for names until control-d is entered
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass  # Stop input when EOF is encountered

    # Generate the farewell message
    if len(names) == 1:
        farewell_message = f"Adieu, adieu, to {names[0]}"
    else:
        farewell_message = "Adieu, adieu, to "
        # Join names properly
        farewell_message += ", ".join(names[:-1]) + f", and {names[-1]}"

    # Print the farewell message
    print(farewell_message)

if __name__ == "__main__":
    main()
