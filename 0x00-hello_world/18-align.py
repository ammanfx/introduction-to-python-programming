#!/bin/env python3 
"""A module used for storing student name and score"""


# Define items and their prices
items = [("Apple", 2.00), ("Banana", 1.50), ("Orange", 3.25)]

# Print table header
print("{:<10} {:>6}".format("Item", "Price"))

# Print a separator line
print("-" * 16)

# Print each item and its price
for item, price in items:
    print("{:<10} ${:>5.2f}".format(item, price))