#!/bin/env python3
"""A module that checks if the letter entered is an upper case"""
def isupper(c):
    """A function that return true or false if a character is upper"""
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False
    
print(isupper("E"))