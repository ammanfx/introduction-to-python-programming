#!/usr/bin/python3
"""a module that calculate the arae of a triangle"""


def triangle(base, height):
    return 0.5 * base * height



if __name__ == "__main__":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))

    result = triangle(base,height)
    print(f"The area of the triangle is {result}")