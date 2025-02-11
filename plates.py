def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if plate starts with at least two letters
    if not s[:2].isalpha():
        return False

    # Check for invalid characters and number positioning
    for i in range(len(s)):
        if not s[i].isalnum():  # No periods, spaces, or punctuation marks
            return False
        if s[i].isdigit():
            # Numbers must not be in the middle; they must be at the end
            if i < len(s) - 1 and s[i+1].isalpha():
                return False
            # The first number cannot be '0'
            if s[i] == '0' and (i == 2 or (i > 2 and s[i-1].isdigit() == False)):
                return False

    return True

main()
