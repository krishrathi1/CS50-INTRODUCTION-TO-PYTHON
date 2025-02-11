# Uncomment the line below for the library you want to use

# Option 1: Using validator-collection
# from validator_collection import checkers

# Option 2: Using validators
import validators

def main():
    email = input("Email: ")

    # Uncomment the line below based on your choice of library

    # Option 1: If using validator-collection
    # is_valid = checkers.is_email(email)

    # Option 2: If using validators
    is_valid = validators.email(email)

    if is_valid:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
