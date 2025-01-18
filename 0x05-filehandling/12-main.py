#!/bin/env python3
"""A module that filter students score"""

# Sample data for students
students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 22, "score": 68},
    {"name": "Charlie", "age": 21, "score": 72},
    {"name": "David", "age": 23, "score": 90},
    {"name": "Eve", "age": 20, "score": 65}
]

def filter_students_by_score(students, threshold=70):
    """
    Function to filter students who scored 70 and above
    """
    result = [student for student in students if student["score"] >= threshold]
    return result

def print_student_details(students):
    """
    Function to print student details
    """
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Score: {student['score']}")

# Example usage
threshold_score = 70
students_above_threshold = filter_students_by_score(students, threshold_score)
print(f"Students who scored {threshold_score} and above:")
print_student_details(students_above_threshold)
