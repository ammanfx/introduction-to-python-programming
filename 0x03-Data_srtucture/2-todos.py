#!/bin/env python3
"""A module that implement todos"""
todos = []
try:
    while True:
        todo=input("Enter a task/what to buy: ")
        todos.append(todo)
except KeyboardInterrupt:
    print('\n', todos)
