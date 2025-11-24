#!/usr/bin env python3
""""
Program to perform bitwise operations"""


# Input: two integers
a, b = map(int, input("Enter two integers: ").split())

# Bitwise AND: compares bits, returns 1 if both are 1
print("AND:", a & b)

# Bitwise OR: compares bits, returns 1 if either is 1
print("OR:", a | b)

# Bitwise XOR: compares bits, returns 1 if bits differ
print("XOR:", a ^ b)

# Left shift: shifts bits of 'a' two places to the left (multiply by 2^2)
print("SHIFT:", a << 2)