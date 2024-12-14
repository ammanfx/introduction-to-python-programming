#!/bin/env python3
"""A module for the implementation calculator"""
add = __import__("0-add").add
sub = __import__("1-sub").sub
divide = __import__("2-division").division
multiply = __import__("3-multiplication").multiplication
mod = __import__("4-modulus").modulus



if __name__ == '__main__':
    num1 = float(input("Enter any number of your choice"))
    num2 = float(input("Enter any number of your choice"))

    op = input("Enter operation to perform(+, -, *, /, %): ")
    if op == "+":
        result = num1 + num2
        print(result)
    elif op =="-":
        result = num1 - num2
        print(result)
    elif op =="x":
        result = num1 * num2
        print(result)
    elif op =="/":
        result = num1 / num2
        print(result)
    elif op =="%":
        result = num1 % num2
        print(result)