#!/usr/bin/python3
"""A module that apply discount price"""

def apply_discount(price, discount_percent):
    # Calculate the discount amount
    discount_amount = price * (discount_percent / 100)
    
    # Calculate the final price
    final_price = price - discount_amount
    
    # Check if discount is greater than 50%
    if discount_percent > 50:
        print("High discount applied!")
    
    return final_price