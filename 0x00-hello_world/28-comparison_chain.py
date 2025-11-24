#!/usr/bin env python3
"""Program to check strictly increasing sequence"""


x, y, z = map(int, input("Enter three integers: ").split())

# Strictly increasing means x < y < z
if x < y < z:
    print("Strictly increasing")
else:
    print("Not strictly increasing")