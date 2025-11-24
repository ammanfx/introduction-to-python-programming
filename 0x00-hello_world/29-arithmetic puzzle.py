#!/usr/bin env python3
"""Program to evaluate arithmetic expression safely"""


# Input: expression string
expr = input("Enter expression (e.g., 3 + 5 * 2): ")

# Split by spaces into tokens
tokens = expr.split()

# Convert numbers and apply operators manually
result = int(tokens[0])
i = 1
while i < len(tokens):
    op = tokens[i]
    num = int(tokens[i+1])
    # Handle operator precedence simply (* and / before + and -)
    if op == '+':
        result += num
    elif op == '-':
        result -= num
    elif op == '*':
        result *= num
    elif op == '/':
        result //= num  # integer division
    i += 2

print("Result:", result)