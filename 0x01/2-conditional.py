#!/usr/bin/python3
# a module that handles grades using conditionals
age = int(input("Enter your age:"))
if age >= 10 and age <= 17:
    print("you are a teenager")
elif age >= 18 and age <= 40:
    print("you are an adult")
elif age > 40:
    print("you are old")
else:
    print("you are young")
    

          