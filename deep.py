# deep.py

def main():
    # Prompt the user for an answer
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Check if the answer is correct
    if is_correct_answer(answer):
        print("Yes")
    else:
        print("No")

def is_correct_answer(answer):
    # Normalize the answer to lowercase and strip any extra whitespace
    answer = answer.strip().lower()

    # Check if the answer matches any valid responses
    return answer == "42" or answer == "forty-two" or answer == "forty two"

main()
