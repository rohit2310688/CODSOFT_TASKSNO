# CodSoft Python Internship - Task 4: Rock-Paper-Scissors Game

# CodSoft Python Internship - Task 3: Password Generator

import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    # Step 1: Ask the user for the password length
    try:
        length = int(input("Enter password length (minimum 4): "))
    except ValueError:
        print("Invalid input! Please enter a whole number.\n")
        continue

    if length < 4:
        print("Password must be at least 4 characters long.\n")
        continue

    # Step 2: Ask the user for the complexity level
    print("\nChoose complexity:")
    print("1. Low    (letters only)")
    print("2. Medium (letters + digits)")
    print("3. High   (letters + digits + symbols)")
    level = input("Enter your choice (1-3): ")

    # Step 3: Decide which characters can be used
    if level == "1":
        characters = string.ascii_letters
    elif level == "2":
        characters = string.ascii_letters + string.digits
    elif level == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice! Please choose between 1 and 3.\n")
        continue

    # Step 4: Pick random characters to build the password
    password = ""
    for i in range(length):
        password = password + random.choice(characters)

    # Step 5: Display the password
    print("\nGenerated password:", password)

    # Step 6: Ask if the user wants another password
    again = input("\nGenerate another password? (y/n): ")
    if again.lower() != "y":
        print("Thank you! Stay safe online.")
        break
    print()
    