#!/bin/env python3
"""A module for calculator"""
num1 = float(input("Enter any number of your choice: "))
num2 = float(input("Enter any number of your choice: "))
op = input ("Enter the operation to perform (+, -, x, /): ")
if op == "+":
    result = num1+num2 
    print(result)
elif op =="-":
    result = num1-num2
    print(result)
elif op =="x":
    result = num1*num2
    print(result)
elif op =="/":
    result = num1/num2
    print(result)
elif op =="%":
    result = num1%num2
    print(result)
