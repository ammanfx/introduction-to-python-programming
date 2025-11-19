#!/usr/bin env python3
"""A module that perform logical operator"""


num = int(input("Enter any number of your choice: "))

print(f"logical and {num > 5 and num < 10}")
print(f"logical or {num > 5 or num < 10}")
print(f"logical not {not(num > 5)}")