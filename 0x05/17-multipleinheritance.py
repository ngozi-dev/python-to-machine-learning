#!/usr/bin/python3
# a module that creates two classes

class Flyer:
    def fly(self):
        print("The duck takes to the sky!")

class Swimmer:
    def swim(self):
        print("The duck paddles through the water.")

# Duck inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack quack!")

# Demonstration
if __name__ == "__main__":
    # Create an instance of Duck
    donald = Duck()

    # Call methods from both parent classes
    donald.fly()   # Inherited from Flyer
    donald.swim()  # Inherited from Swimmer
    donald.quack() # Defined in Duck