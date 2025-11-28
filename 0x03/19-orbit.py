#!/usr/bin/python3
# a module that unpack a tuple

user = ("John", 25, "Nigeria")
print(type(user))

# (1) to unpack the tuple
name, age, country = user
print(name)
print(age)
print(country)

print(f"{name} is {age} years old from {country}: ")

# (3) Given two sets of integers, perform and print the result of union, intersection, difference, and symmetric difference.

num1 = {1, 2, 3}
num2 = {4, 5, 6}
print(num1.union(num2))

print(num1.intersection(num2))

print(num1.difference(num2))

print(num1.symmetric_difference(num2))

# (4) Create a list of 10 elements. Print: First 3 elements, Last 3 elements, Every second element

# list of 10 elements (you can customize elements as needed)
lst = list(range(1, 11))  # [1, 2, 3, ..., 10]

# First 3 elements
first_three = lst[:3]

# Last 3 elements
last_three = lst[-3:]

# Every second element (indices 0, 2, 4, ...)
every_second = lst[::2]

print("First 3 elements:", first_three)
print("Last 3 elements:", last_three)
print("Every second element:", every_second)


# (5) Accept a list of integers with duplicates. Remove duplicates using a set and return the sorted list.

num = [1, 2, 3, 3, 3, 4, 5, 5]
num = set(num)
print(type(num))
print(num)


# (7) Ask the user for a number and check if it exists in a predefined set {3, 6, 9, 12}. Print "Found" or "Not Found".

set = {3, 6, 9, 12}
user_num = int(input("Enter a number:"))
for user_num in set:
    if user_num == 3:
        print(user_num)
    else:
        print(user_num)


# (8) Given a nested list [[1, 2], [3, 4], [5, 6]], print the second element of the third sublist.

list = [[1, 2], [3, 4], [5, 6]]
print(list(-2))


# (10) Take a string input from the user and convert it into a set of unique characters. Print the set and its length.

user_input = input("My name is Ngozi")
print(user_input)
print(len(user_input))