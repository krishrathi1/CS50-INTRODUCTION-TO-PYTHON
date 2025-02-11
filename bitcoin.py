import sys
import requests

def main():
    # Check for the command line argument for number of Bitcoins
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    # Try to convert the argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: Argument must be a number.")
        sys.exit(1)

    # Query the CoinDesk API for the current Bitcoin price
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON response
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]  # Get the price in float

        # Calculate the total cost
        total_cost = bitcoins * price_per_bitcoin

        # Output the current cost in USD to four decimal places
        print(f"The cost of {bitcoins} Bitcoin(s) is: ${total_cost:,.4f}")

    except requests.RequestException:
        print("Error: Unable to retrieve Bitcoin price.")
        sys.exit(1)

if __name__ == "__main__":
    main()
