#/bin/env python3
"""A module that impliment dictionary in calculator"""
from add import add
from sub import sub
from division import division
from multiplication import multiplication 


num1 = float(input("Enter any number of your choice: "))
num2 = float(input("Enter any number of your choice: "))
op = input ("Enter the operation to perform (+, -, x, /,): ")
result = 0

kwargs = {
    "op":[{'+':add},{'-':sub},{'*':division},{'/':multiplication}]
}

for operator in kwargs.get("op"):
    for key, value in operator.items():
        if key == op:
            result = value(num1, num2)

print(result)