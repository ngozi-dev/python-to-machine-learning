#!/usr/bin/python3
# a module that handles error
try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("cannot perform division by zero") 