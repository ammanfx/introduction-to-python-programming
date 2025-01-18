#!/bin/env python3
"""A module implimenting json to print script"""

import json
import os
import sys

def generate_unique_id(file_path):
    if not os.path.exists(file_path):
        return 1
    with open(file_path, 'r') as f:
        data = json.load(f)
        return max(student['id'] for student in data) + 1

def add_student(file_path, name, age, grades, hobbies):
    student = {
        'id': generate_unique_id(file_path),
        'name': name,
        'age': age,
        'grades': grades,
        'hobbies': hobbies
    }
    
    if not os.path.exists(file_path):
        data = []
    else:
        with open(file_path, 'r') as f:
            data = json.load(f)

    data.append(student)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage:
file_path = 'students.json'

students = []

while True:
    try:
        name = input("Enter name of student: ")
        age = int(input("Enter age of student: "))
        grades = input("Enter student grades (45, 25, 60): ")
        hobbies = input("Enter student hobbies (e.g Reading, Cycling): ")

        if grades:
            print(grades)
            new_grades = grades.split(",")
            grades = [int(grade.strip(" ")) for grade in new_grades]

        if hobbies:
            new_hobbies = hobbies.split(",")
            hobbies = [(hobbie.strip(" ")) for hobbie in new_hobbies]
        
        students.append({
            'name': name,
            'age': age,
            'grades': grades,
            'hobbies': hobbies
        })
    except KeyboardInterrupt:
        print("\n Processing for storage")
        for student in students:
            add_student(file_path, student['name'], student['age'], student['grades'], student['hobbies'])
        print(f"Student added successfully!")
        sys.exit(0)
