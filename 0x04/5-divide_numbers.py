#!/usr/bin/python3
# a module that takes two numbers and returns their division

try:
    result = 7/0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero. Please provide a non-zero divisor. ")
except TypeError:
    print("Invalid input. Please provide numbers for both numerator and divisor. ")
