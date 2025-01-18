#!/bin/env python3
"""A module for main"""

from determine import determine_winner
from userchoice import get_user_choice
from computerchoice import get_computer_choice


def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()
