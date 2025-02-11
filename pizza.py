import csv
import os
import sys
from tabulate import tabulate

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")

    filename = sys.argv[1]

    # Check if the filename ends with .csv
    if not filename.endswith('.csv'):
        sys.exit("Error: File must end with .csv")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: File {filename} does not exist")

    # Read the CSV file and prepare data for tabulation
    data = read_csv(filename)

    # Print the formatted table
    print(tabulate(data, headers="firstrow", tablefmt="grid"))

def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        # Convert the CSV reader object to a list
        data = list(reader)
    return data

if __name__ == "__main__":
    main()
