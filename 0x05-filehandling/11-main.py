#!/bin/env python3
"""A module that search for student details"""
import json
import os
import sys


if not os.path.exists('students.json'):
    raise FileNotFoundError

def find_students_with_hobby(hob, students):
    """
    Function to find students with a specific hobby
    """
    result = [student for student in students for hobby in student['hobbies'] if hobby == hob]
    return result


def print_student_details(students):
    """
    Function to print student details
    """
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Hobby: {student['hobbies']}")

hobby = input('Search student information using their hobby: ')
if not hobby:
    print('No input specified')
    sys.exit(1)
else:
    with open('students.json', 'r') as file:
        data = json.load(file)
        students = find_students_with_hobby(hobby, data)
        print_student_details(students)

