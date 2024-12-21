#!/bin/env python3
"""A module that count integer"""

"""
for number in range (0, 101):
    PRINT(num, end=" ")
"""



for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0: 
        print("fizzbuzz", end=" ")
    elif num % 5 == 0:
        print("buzz", end=" ")
    elif num % 3 == 0:
         print("fizz", end=" ")
    else:
        print(num, end=" ")