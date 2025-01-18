#!/bin/env python3
"""A module takes and read csv file"""


import csv
with open("employee_data.csv", "r") as file:
    content = csv.reader(file, delimiter=",")
    for index, row in enumerate(content):
        if index >= 50 and index <= 100:
            print(f"{row[2]}, {row[2]}, {row[3]}, {row[5]}, {row[7]}")