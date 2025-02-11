print("Amount Due:")
amt_due = 50
coin_added = 0

# Correct the capitalization of 'True' in the while loop and use proper indentation.
while True:
    inserted_coin = int(input("Insert Coin: "))

    # Check if the inserted coin is valid
    if inserted_coin in [25, 10, 5]:
        amt_due -= inserted_coin
        coin_added += inserted_coin

        # Check if enough coins have been added to cover the cost
        if coin_added >= 50:
            print(f"Change Owed: {coin_added - 50}")
            break
        else:
            print(f"Amount Due: {amt_due}")
    else:
        # Inform the user when an invalid coin is entered
        print(f"Invalid coin. Amount Due: {amt_due}")
