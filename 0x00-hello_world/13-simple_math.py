#!/bin/env python3
"""A code that ask a user to enter two numbers"""


# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum, difference, product, and quotient
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Handle division carefully to avoid division by zero
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"

# Print the results with clear labels
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)