#!/usr/bin/python3
# a module that creates a square class with private instance attribute age

class Student:
    def __init__(self, age):
        self.__age = age
        if not isinstance (age, (int)):
            raise TypeError(" age must be a number")
        if age <= 0:
            raise ValueError(" age must be > 0 ")
        

if __name__ == "__main__":
    student = Student(age = 30)
    print(student)
    
      