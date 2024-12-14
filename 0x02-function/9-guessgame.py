#!/bin/env python3
"""A programme that handles user guesses"""
import random


def display(message):
    """A function that prints a message"""
    print(message)


while True:   
    num = int(input("Guess a number from 0-5: "))
    guess = random.randrange(0,5)
    if num == guess:
        display("Congratulation, you guessed correct.")
        break
    else:
        display("Sorry, you guessed wrongly. Try again")