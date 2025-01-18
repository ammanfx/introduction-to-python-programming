#!/bin/env python3
"""A module that read csv"""
import csv

with open("lesson.csv", "r") as file:
    content = csv.reader(file, delimiter= ",")
    for row in content:
        print(" ".join(row))