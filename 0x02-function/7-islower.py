#!/bin/env python3
"""A module that checks if the letter you entered is a lower case"""
def islower(c):
    """A function that return true or false if the character is in lower case"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True 
    else:
        return False


print(islower("a"))