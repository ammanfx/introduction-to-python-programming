#!/bin/env python3 
"""A module used for calculating sum of two numbers"""


# Store two numbers
num1 = 45
num2 = 55

# Calculate the sum
total = num1 + num2

# Print using string formatting
print("The sum of {} and {} is {}".format(num1, num2, total))

# Optional: Aligning text output in a table-like format
print("\nAligned Output:")
print("{:<15} {:<15} {:<15}".format("Number 1", "Number 2", "Sum"))
print("{:<15} {:<15} {:<15}".format(num1, num2, total))