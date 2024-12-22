#!/bin/env python3
"""A module implement union sets"""

Car1 = {"bmw", "bugatti", "ferarri", "lamborghini", "audi"}
Car2= {"benz", "toyota", "honda", "nissan"}

all_cars = Car1.union(Car2)

print(all_cars)