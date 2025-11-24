#!/usr/bin env python3
"""A module that perform calculation"""


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %): ")

# Perform operation based on operator
if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
elif op == '%':
    if b != 0:
        print("Result:", a % b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")