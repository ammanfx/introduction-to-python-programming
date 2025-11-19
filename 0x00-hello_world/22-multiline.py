#!/bin/env python3 
"""A module used for printing formatted receipt"""


# Store item details
item = "Book"
quantity = 3
total = 45.00

# Print formatted receipt using triple-quoted string
receipt = f"""Receipt:
Item: {item}
Quantity: {quantity}
Total: ${total:.2f}
"""

print(receipt)