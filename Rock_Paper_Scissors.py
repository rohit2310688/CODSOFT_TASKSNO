# CodSoft Python Internship - Task 4: Rock-Paper-Scissors Game

import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK - PAPER - SCISSORS =====")
print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.\n")

while True:
    # Step 1: Get the user's choice
    user_choice = input("Enter rock, paper or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice! Please try again.\n")
        continue

    # Step 2: Computer makes a random choice
    computer_choice = random.choice(options)

    # Step 3: Show both choices
    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Step 4: Decide the winner
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You win!")
        user_score += 1
    else:
        print("Result: Computer wins!")
        computer_score += 1

    # Step 5: Show the score
    print("Score -> You:", user_score, "| Computer:", computer_score)

    # Step 6: Ask to play again
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("\nFinal Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break
    print()