#!/bin/env python3
"""A module that access element in a list using index"""
car = ["BMW", "Audi", "Bugatti", "Ferari", "Tesla"]
print(car[0])
print(car[2])
print(car[4])
print(len(car))
car.append("Toyota")
print(len(car))
car.remove("Bugatti")
car.pop()
for item in car:
    print(item)