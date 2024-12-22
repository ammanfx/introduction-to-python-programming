#!/bin/env python3 
"""A module that implement subset"""

subjects = {"maths", "english", "chemistry", "physics", "ecnomics"}
reg_subjects = {"maths", "english", "physics"}

result = reg_subjects.issubset(subjects)
print(result)
