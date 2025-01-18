#!/bin/env python3

import csv

with open("lesson.csv", "w") as file:
    content = csv.writer(file, delimiter=",")
    content.writerow(["1", "muhammad Abubakar", "computer sciemce", "csc122"])