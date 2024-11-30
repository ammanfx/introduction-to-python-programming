#!/bin/env python3
"""A programme that handles user guesses"""
import random


while True:   
    num = int(input("Guess a number from 0-2: "))
    guess = random.randrange(0,2)
    if num == guess:
        print("Congratulation, you guessed correct.")
        break
    else:
        print("Sorry, you guessed wrongly. Try again")
        
