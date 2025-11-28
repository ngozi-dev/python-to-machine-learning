#!/usr/bin/python3
# a module that Takes a list of names

matrix = ["Alice", "Bob", "Charlie", "David"]
user_input = input("Enter any name of your choice:")

if user_input.capitalizes() in matrix:
    index = matrix.index(user_input)
    print(index)
else:
    print("Nane not fund")
