#!/bin/env python3
"""A module that raise an error"""
age = "Muhammad Abubakar"
if type(age) is not "int":
    raise ValueError("Input is not a number")