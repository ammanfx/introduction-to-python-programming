#!/usr/bin env python3
"""Program to apply bitmask"""


num = int(input("Enter number: "))
mask = int(input("Enter bitmask (in decimal): "), 10)  # input mask as decimal

# Bitwise AND with mask
result = num & mask
print("Result:", result)