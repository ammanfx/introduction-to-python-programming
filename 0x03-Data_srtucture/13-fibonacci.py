#!/bin/env python3
"""Function to print Fibonacci numbers from 1 to 100"""


def print_fibonacci():
    a, b = 0, 1
    while b <= 100:
        if b > 0:
            print(b, end=" ")
        a, b = b, a + b

print_fibonacci()
