#!/usr/bin/python3
"""a module th calculate the area of rectangle"""


def rectangle(lenth, breath):
    return lenth * breath



if __name__ == "__main__":
    lenth = int(input("Enter the lenth of the rectangle: "))
    breath = int(input("Enter the breath of the rectangle: "))

    result = rectangle(lenth, breath)
    print(f"The area of the rectangle is {result}")