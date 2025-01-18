#!/bin/env python3
"""A module implimenting main"""

import csv
with open("employee_data.csv", "r") as file:
    content = csv.reader(file, delimiter=",")
    for index, row in enumerate(content):
        if index == 50:
            break
        print(f"{row[0]} {row[1]} {row[2]} {row[7]}")
