#!/bin/env python3
"""A module that implement the use of calculator using dictionary"""

# Define the calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error! Division by zero."

def exponentiate(a, b):
    return a ** b

# Dictionary mapping operation names to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulus,
    '^': exponentiate
}

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, ^")
    
    operation = input("Enter operation: ")
    if operation in operations:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        result = operations[operation](a, b)
        print(f"The result is: {result}")
    else:
        print("Invalid operation")

# Run the calculator
calculator()
