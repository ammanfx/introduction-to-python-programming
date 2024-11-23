#!/bin/env python3
"""A module for else if in control structure"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 0 and age <= 7:
    print(f"{name} you're a child")
elif age >=8 and age <= 17:
    print(f"{name} you're a teenager")
elif age >=18 and age <= 40:
    print(f"{name} you're an adult")
else:
    print(f"{name} you're old")
