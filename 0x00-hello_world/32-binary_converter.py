#!/usr/bin env python3
"""Program to convert integer to binary, octal, and hex"""


num = int(input("Enter an integer: "))

print("Binary:", bin(num))   # bin() gives binary representation
print("Octal:", oct(num))   # oct() gives octal representation
print("Hexadecimal:", hex(num))  # hex() gives hexadecimal representation