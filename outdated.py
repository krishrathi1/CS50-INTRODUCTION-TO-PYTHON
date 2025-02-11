def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        # Prompt the user for a date
        date_input = input("Date: ").strip()

        # Try to parse the date in MM/DD/YYYY format
        try:
            month, day, year = map(int, date_input.split("/"))
            if 1 <= month <= 12 and 1 <= day <= 31 and year >= 1:
                print(format_date(year, month, day))
                break
        except ValueError:
            pass

        # Try to parse the date in "Month Day, Year" format
        parts = date_input.split()
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            month_str = parts[0]
            day = int(parts[1])
            year = int(parts[2])

            if month_str in months and 1 <= day <= 31 and year >= 1:
                month = months.index(month_str) + 1
                print(format_date(year, month, day))
                break

        print("Invalid date format. Please try again.")

def format_date(year, month, day):
    return f"{year}-{month:02}-{day:02}"

if __name__ == "__main__":
    main()
