#Python rock paper scissor game made by Debroop(pythonRPS.py) 
#roll number 235/UCS/049
import random

# Python rock paper scissor game made by Debroop (pythonRPS.py)
# Roll number 235/UCS/049

import random

def rock_paper_scissor():
    choices = ["rock", "paper", "scissor"]

    print("Welcome to Rock, Paper, Scissor!")
    print("Press 'Q' to exit the game.\n")

    wins = 0
    losses = 0
    ties = 0

    while True:
        user_choice = input("Enter rock, paper, or scissor: ").lower()

        if user_choice == "q":
            print("\nThank you for playing!")
            print(f"Final Score → Wins: {wins}, Losses: {losses}, Ties: {ties}")
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!\n")
            ties += 1
        elif (user_choice == "rock" and computer_choice == "scissor") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissor" and computer_choice == "paper"):
            print("You win!\n")
            wins += 1
        else:
            print("You lose!\n")
            losses += 1

rock_paper_scissor()
