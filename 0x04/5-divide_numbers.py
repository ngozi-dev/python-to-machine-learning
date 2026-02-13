#!/usr/bin/python3
# a module that takes two numbers and returns their division
def divide (num1, num2):

    try:
        result = num1/num2
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero. Please provide a non-zero divisor. ")
    except TypeError:
        print("Invalid input. Please provide numbers for both numerator and divisor. ")

if __name__ == "__main__":
    result = divide(6,2)
    print(result)

