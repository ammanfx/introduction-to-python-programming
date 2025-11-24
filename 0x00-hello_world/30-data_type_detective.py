#!/usr/bin env python3
"""Program to detect input type"""


data = input("Enter something: ")

# Try converting to int
try:
    val = int(data)
    print("You entered an integer")
except ValueError:
    # Try converting to float
    try:
        val = float(data)
        print("You entered a float")
    except ValueError:
        # If neither, it's a string
        print("You entered a string")