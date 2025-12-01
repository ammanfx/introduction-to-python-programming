#!/usr/bin/python3
"""a module that checks if a number is even or odd"""

def analyze_number(num):
    """
    Analyze whether a number is even or odd,
    and check if it's divisible by 5.
    
    Parameters:
    num (int): The number to analyze.
    
    Returns:
    str: "Even number" or "Odd number"
    """
    # Check divisibility by 5
    if num % 5 == 0:
        print("Special number: divisible by 5")
    
    # Check even or odd
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"