#!/usr/bin env python3
""""Program to generate truth table for two boolean variables"""


# We use True and False combinations
values = [True, False]

print("A\tB\tAND\tOR\tNOT A\tNOT B")
for A in values:
    for B in values:
        # Logical operators: and, or, not
        print(f"{A}\t{B}\t{A and B}\t{A or B}\t{not A}\t{not B}")