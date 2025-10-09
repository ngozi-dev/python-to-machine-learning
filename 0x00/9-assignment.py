#!/usr/bin/python3
# a file that contains all assignment operations

num = int(input("Enter any number of your choice:"))

num += 2
print("addition and assignment: {}, type {}".format(num, type(num)))

num *= 2
print("multiplication and assignment: {}, type {}".format(num, type(num)))

num -= 2
print("subtraction and assignment: {}, type {}".format(num, type(num)))

num /= 2
print("division and assignment: {}, {}".format(num, type(num)))

num **= 2
print("exponential and assignment: {}, {}".format(num, type(num)))

num %= 2
print("modulus and assignment: {}, {}".format(num, type(num)))

num //= 2
print("floordivision and assignment: {}, {}".format(num, type(num)))
5

