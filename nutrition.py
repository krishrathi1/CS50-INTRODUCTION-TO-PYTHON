def main():
    # Create a dictionary with fruits and their calorie counts (all keys in lowercase)
    fruits = {
        "apple": 130,
        "banana": 110,
        "avocado": 50,
        "sweet cherries": 100,
        "cantaloupe": 50,
        "grapefruit": 60,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "tangerine": 50,
        "watermelon": 80
    }

    # Prompt the user for a fruit (case-insensitively)
    fruit = input("Fruit: ").strip().lower()

    # Check if the fruit is in the dictionary and print its calorie count
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")

main()
