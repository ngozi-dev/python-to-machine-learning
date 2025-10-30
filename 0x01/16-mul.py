#!/usr/bin/python3
# a module that requests a user to enter number

def mul(a, b):
    return a * b


if __name__ == "__main__":
    num = int(input("Enter any number of your choice: "))
    for i in range(1, 13):
        print("{} x {} = {}".format(num, i, mul(num, i)))
        


