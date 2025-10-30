#!/usr/bin/python3 
# a module that performs simple calculations


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def pow(a, b):
    return a ** b


if __name__ == "__main__":
    opt = int(input("Enter operation (1. add, 2. sub, 3. mul, 4. div, 5. mod, 6. pow): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    match opt:
        case 1:
            print(f"Result: {add(num1, num2)}")
        case 2:
            print(f"Result: {sub(num1, num2)}")
        case 3:
            print(f"Result: {num1 * num2}")
        case 4:
            print(f"Result: {div(num1, num2)}")
        case 5:
            print(f"Result: {mod(num1, num2)}")
        case 6:
            print(f"Result: {pow(num1, num2)}")
        case _:
            print("Invalid operation")
