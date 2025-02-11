def main():
    # Prompt the user for a time in 24-hour format
    time = input("Enter the time in 24-hour format (e.g., 7:30 or 12:00): ").strip()

    # Convert the time to a float representing hours
    hours = convert(time)

    # Determine the meal time based on the hour
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Convert the time to hours as a float
    return hours + minutes / 60

# Run the main function
if __name__ == "__main__":
    main()
