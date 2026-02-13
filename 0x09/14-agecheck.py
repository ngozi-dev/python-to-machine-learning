#!/usr/bin/python3
# a module that checks if a user is a minor or an adult

def main():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult. ")
    elif age <= 17:
        print("you are a minor. ")
    else:
        print("Invalid input. Please enter a valid age. ")

  