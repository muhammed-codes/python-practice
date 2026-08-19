import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("")
        playerChoice = input("Enter... \n1 for Rock \n2 for Paper \n3 for Scissors \n\n")

        if playerChoice not in ["1", "2", "3"]:
            print("Invalid choice. Please select a number between 1 and 3.")
            play_rps()

        player = int(playerChoice)
        if player < 1 or player > 3:
            print("Invalid choice. Please select a number between 1 and 3.")
            play_rps()

        computerChoice = random.randint(1, 3)

        print(f"\nYou chose: {RPS(player).name}. Computer chose: {RPS(computerChoice).name}.")

        def decide_winner(player, computerChoice):
            nonlocal player_wins
            nonlocal computer_wins

            if player == computerChoice:
                return"It's a tie!"
            elif (player == 1 and computerChoice == 3) or \
                (player == 2 and computerChoice == 1) or \
                (player == 3 and computerChoice == 2):
                player_wins += 1
                return"You win!"
            else:
                computer_wins += 1
                return"Computer wins!"

        game_result = decide_winner(player, computerChoice)

        nonlocal game_count
        game_count += 1
        if game_count > 1:
            print(f"You've played {game_count} times, you won {player_wins} and computer won {computer_wins}")
        else:
            print(f"You've played {game_count} time and {game_result}")

        def continue_playing ():
            playagain = input("\nPlay again? (y/n): ")
            if playagain.lower() == "y":
                play_rps()
            elif playagain.lower() == "n":
                print("\nThanks for playing! You rock!")
                sys.exit("Bye")
            else:
                print("\nYou chose wrong option, choose again.")
                continue_playing()

        continue_playing()
    return play_rps

play = rps()
play()