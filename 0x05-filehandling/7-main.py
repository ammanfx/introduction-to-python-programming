#!/bin/env python3
"""A module that takes and read csv file"""

import csv 
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("File not found!")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, "r") as file:
        content = csv.reader(file, delimiter= ",")
        for index, row in enumerate(content):
            if index >= 10 and index <= 25:
                print(f"{row[1]}, {row[2]}, {row[3]}, {row[5]}, {row[7]}")