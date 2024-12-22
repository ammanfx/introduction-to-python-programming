#!/bin/env python3
"""A module that implement interception in set"""

phone1 = {"iphone", "samsung", "redmi", "oppo"}
phone2 = {"tecno", "infinix", "iphone", "redmi"}

all_phones = phone1.intersection(phone2)
print(all_phones)