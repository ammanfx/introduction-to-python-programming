#!/bin/env python3
"""A module that handle file renaming"""
import os
import json

def rename(old_filename, new_file_name):
    """
    A function that rename a file 
    Arge:
        old_filename: existing file name to be replace 
        new_file_name: name of file to be replacde 
    """
    try:
        if not os.path.isfile(old_filename):
            raise FileNotFoundError("file to be renamed not found")
        with open(old_filename, "r") as file:
            content = json.load(file)
            with open(f'{new_file_name}.json' "w") as new_file:
                try:
                    json.dump(new_file_name, content)
                except Exception as e:
                    print('Error: not able to rename file!')
                    return False
                finally:
                    new_file.close()
            file.close()
        os.remove(f'{old_filename}.json')
    except Exception as e:
        print(f"Error: {e}")
        return False