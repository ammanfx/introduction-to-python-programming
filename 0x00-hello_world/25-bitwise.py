#!/usr/bin env python3
"""A module perform bitwise opration"""


num = int(input("Enter any number of your choise"))

print(f"bitwise shift left {num << 1}")
print(f"bitwise shift right {num >> 1}")
print(f"bitwise and {num & 1}")
print(f"bitwise or {num ^ 1}")