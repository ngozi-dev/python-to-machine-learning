#!/usr/bin/python3
# a module that accepts a string and converts it to an integer
# Write a function that accepts a string and converts it to an integer. 
# Use a try/except block to catch ValueError 
# when the string cannot be converted, 
# and return a clear message explaining the issue.

try:
    print(int("s"))
except ValueError:
    print("Cannot convert to an integer. Please provide a string that represents an integer (e.g., '42', '-7').")

