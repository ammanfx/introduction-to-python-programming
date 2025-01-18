#!/bin/env python3
"""A module used for implementing finally"""

try: 
    with open("text.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
finally:
    print("Execution completed")