#!/bin/env python3
"""A module that handles file update"""
import json
import os

def update(filename, title, body):
    """
    a function that handle file update 
    Args:
        Filename: name of the file
        Title: new title for the update
        body: the new body of the update
    """
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError("File to update not found")
        with open(filename, "a") as file:
            content = json.load(file)
            content['title'] = title
            content['body'] = body
            json.dump(file, content, indent=4)
            return True
    except Exception as e:
        print(f'Error: {e}')
        return False
    