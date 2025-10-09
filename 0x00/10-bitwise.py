#!/usr/bin/python3
# a file that contains type bitwise in python
num = int(input("Enter any number of your choice"))
print("left shift: {}".format(num << 3))
print("right shift: {}".format(num >> 3))
print("bitwise AND: {}".format(num & 3))
print("bitwise or: {}".format(num | 3))
print("bitwise XOR: {}".format(num ^ 3))
print("bitwise NOT: {}".format(~num))

