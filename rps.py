import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True
while playagain:
    print("")
    playerChoice = input("Enter... \n1 for Rock \n2 for Paper \n3 for Scissors \n\n")

    player = int(playerChoice)
    if player < 1 or player > 3:
        print("Invalid choice. Please select a number between 1 and 3.")
        continue

    computerChoice = random.randint(1, 3)

    print(f"\nYou chose: {RPS(player).name}. Computer chose: {RPS(computerChoice).name}.")

    if player == computerChoice:
        print("It's a tie!")
    elif (player == 1 and computerChoice == 3) or \
        (player == 2 and computerChoice == 1) or \
        (player == 3 and computerChoice == 2):
        print("You win!")
    else:
        print("Computer wins!")
    playagain = input("Play again? (y/n): ")
    if playagain.lower() == "y":
        continue
    else:
        print("\nThanks for playing! You rock!")