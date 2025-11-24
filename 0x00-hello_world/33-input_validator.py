#!/usr/bin env python3
"""Program to validate input between 1 and 100"""


while True:
    num = int(input("Enter a number between 1 and 100: "))
    if 1 <= num <= 100:
        print("Valid input:", num)
        break
    else:
        print("Invalid input, try again.")