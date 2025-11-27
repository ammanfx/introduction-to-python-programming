#!/usr/bin/ env python3
"""A module that ask a user to enter their score"""


score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print(f"{score} A")
elif score >= 80 and score <= 89:
    print(f"{score} B")
elif score >= 70 and score <= 79:
    print(f"{score} C")
elif score >= 60 and score <= 69:
    print(f"{score} D")
elif score >= 0 and score<= 59:
    print(f"{score} F")
else:
    print(f"{score} invalid score")