#!/usr/bin/python3
# a module that creates a base class and carries out override method

# Base class
class Vehicle:
    def drive(self):
        print("The vehicle is moving.")

# Derived class
class Car(Vehicle):
    # Overriding the drive method
    def drive(self):
        print("The car is driving smoothly on the highway.")

# Demonstrating overriding
if __name__ == "__main__":
    # Object of the base class
    generic_vehicle = Vehicle()
    
    # Object of the derived class
    my_car = Car()

    # Calling the method on the base class object
    generic_vehicle.drive()  # Output: The vehicle is moving.

    # Calling the method on the derived class object
    my_car.drive()          # Output: The car is driving smoothly on the highway.