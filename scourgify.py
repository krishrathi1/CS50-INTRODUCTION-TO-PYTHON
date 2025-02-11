import sys
import csv

def main():
    check_command_line_args()
    output = []

    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({
                    'first': split_name[1].strip(),  # Fixed typo and used 'first'
                    'last': split_name[0].strip(),
                    'house': row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"could not read {sys.argv[1]}")

    # Fixed incorrect file mode, variable name, and CSV writing format
    with open(sys.argv[2], "w", newline='') as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in output:
            writer.writerow(row)

def check_command_line_args():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input.csv output.csv")

if __name__ == "__main__":
    main()
