#!/usr/bin/python3
# a module that handles the comparison of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("{:.2f} is the biggest number".format(num1))
elif num2 > num1:
    print("{:.2f} is the biggest number".format(num2))
else:
    print("Both numbers are equal")
    
        