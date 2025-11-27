#!/usr/bin/ env python3
"""A module that ask a user to enter their score"""


score = int(input("Enter your score: "))

if score >= 70 and score <= 100:
    print(f"{score} A")
elif score >= 60 and score <= 69:
    print(f"{score} B")
elif score >= 50 and score <= 59:
    print(f"{score} C")
elif score >= 45 and score <= 49:
    print(f"{score} D")
elif score >= 40 and score <= 44:
    print(f"{score} E")
elif score >= 0 and score<= 30:
    print(f"{score} F")
else:
    print(f"{score} invalid score")