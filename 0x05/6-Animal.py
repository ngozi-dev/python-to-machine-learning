#!/usr/bin/python3
# a module that creates a class with public instance attribute name 

class Animal:
    def __init__(self,name):
        self.name = name # public instance attribute name
       


if __name__ == "__main__":
    animal = Animal("Lion")
    print(animal.name)
