# Prompt the user for a string of text
text = input("Input: ")

# Define a string with all vowels
vowels = "AEIOUaeiou"

# Initialize an empty string to store the result
result = ""

# Iterate over each character in the input text
for c in text:
    # Check if the character is not a vowel
    if c not in vowels:
        # Add it to the result string if it is not a vowel
        result += c

# Output the resulting string with vowels removed
print("Output:", result)
