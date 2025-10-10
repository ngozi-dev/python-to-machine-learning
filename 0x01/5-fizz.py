#!/usr/bin/python3
# a module that displays fizz, buzz or fizzbuzz
num = int(input("Enter any unmber of your choice: "))
if num %  3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print(num)

