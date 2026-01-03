#!/usr/bin/python3
# a module that creates a class Person with public instance attribute name

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name # public instance attribute first_name
        self.last_name = last_name # public instance attribute last_name

    def full_name(self): # public method that returns the full name
        return f"{self.first_name} {self.last_name}"
    

if __name__ == "__main__":
    person = Person("Ngozi", "Ezeaku")
    print(person.full_name())   