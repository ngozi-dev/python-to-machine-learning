#!/usr/bin/python3
# a module that creates a class Student with a private attribute --age

class Student:
    def __init__(self, age):
        self.age = age # invoke the age setter method

    @property # getter method for age
    def age(self):
        """retrives the age attribute"""
        return self.__age
    
    @age.setter
    def age(self, value):
        """sets the size attribute with validation"""
        if not isinstance(value, (int)):
            raise TypeError("age must be a number")
        if value < 0:
            raise ValueError("age must be >=0")
        self.__age = value


if __name__ == "__main__":
    student = Student(30)
    print(student.age)
    


