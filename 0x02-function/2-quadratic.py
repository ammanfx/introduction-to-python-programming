#!/usr/bin/python3
"""a module that calculate quadratic equation(using the completing the squre method)"""
import math


def quadratic(a, b, c):
    d = b ** 2 - (4 * a * c)

    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    return x1, x2



if __name__ == "__main__":
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    x1, x2 = quadratic(a, b, c)

    print(f"The solution are {x1} and {x2}")