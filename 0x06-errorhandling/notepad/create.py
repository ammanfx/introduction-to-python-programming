#!/bin/env python3
"""A module that handle file creation"""
import json
import os

def create(filename, title, body):
    """
    a function that handle file creation and input file and body
    Args:
        filename: name of the file to create 
        title: title of the document
        body: information to be contained file
    """
    try:
        if os.path.exists(f"{filename}.json"):
            raise FileExistsError("Cannot create file, filname already exist")
        with open(f"{filename}.json", "w" ) as file:
            content = {"title": title, "body": body}
            json.dump(file, content)
            return True
    except Exception as e:
        print(f"An error occured: {e}")
        return False