#!/bin/env python3
"""A module that implement the use of copy_list"""
updatelist=__import__("3-update").update_list
phones = ["iphone", "samsung", "tecno", "nokia", "itel"]
phones_copy=phones.copy()
copy_phones=phones[:]

updatelist(copy_phones, 3, "redmi")

print(phones_copy)

