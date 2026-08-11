import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerChoice = input("Enter... \n1 for Rock \n2 for Paper \n3 for Scissors \n\n")

player = int(playerChoice)
if player < 1 or player > 3:
    sys.exit("Invalid choice. Please select a number between 1 and 3.")

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