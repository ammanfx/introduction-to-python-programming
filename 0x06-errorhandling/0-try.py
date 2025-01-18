#!/bin/env python3
"""A module for trying error"""

try:
    result = 10/0
except ZeroDivisionError:
    print("Error")
