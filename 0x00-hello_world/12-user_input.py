#!/usr/bin/env python3 
"""A module that ask a user to enter name and age"""


# Ask the user for their name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# Create the message using string formatting and concatenation
message = "HELLO " + name.upper() + ", YOU ARE " + age + " YEARS OLD."

# Print the message
print(message)