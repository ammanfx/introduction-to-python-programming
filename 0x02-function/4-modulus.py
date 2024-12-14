#!/bin/env python3
"""A module that perfoms modulis"""



def modulus(num1, num2):
    """
A function that mod two numbers
param:
    num1 - takes any number
    num2 - takes any number
return the result of both operands

    """
    return num1 % num2


if __name__ == '__main__':
    result = modulus(10, 3)
    print(result)