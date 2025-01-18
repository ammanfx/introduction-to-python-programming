#!/bin/env python3
"""A module used for modifying student record in json"""

import json
import os

def modify_student(file, name, grades):
    if not os.path.exists(file):
        raise FileNotFoundError
    with open(file, "r" ) as f:
        data = json.load(f)

        for student in data:
            if student['name'].lower() == name.lower():
                student['grades'] = grades
                retval = save_file(file, data)
                if retval:
                    print("Save successfully")
            else:
                return 'Student Not found'


def save_file(file_path, data):
    if not os.path.exists(file_path):
        raise FileNotFoundError
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    return True


modify_student("students.json", "Muhammad Abubakar", [45, 55, 67])

