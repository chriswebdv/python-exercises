import random


def get_choices():
    player_choice = input("Enter a choice => rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choices(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player} Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    


    




