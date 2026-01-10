#!/usr/bin/python3
# a module that creates a base class Animal with a method sound()

# 1. Base Class
class Animal:
    def sound(self):
        print("Generic animal sound")

# 2. Derived Class (Dog)
class Dog(Animal):
    def sound(self): # Override the method
        print("Woof! Woof!")

# 3. Derived Class (Cat)
class Cat(Animal):
    def sound(self): # Override the method
        print("Meow!")

# 4. Demonstrate Polymorphism
def animal_sound_demo(animal):
    """Function that takes any Animal object and calls its sound method."""
    print(f"Calling sound on a {type(animal).__name__}:")
    animal.sound()

# Create objects
my_dog = Dog()
my_cat = Cat()
generic_animal = Animal()

print("--- Calling directly ---")
my_dog.sound()
my_cat.sound()
generic_animal.sound()

print("\n--- Calling via polymorphic function ---")
animal_sound_demo(my_dog) # Dog's sound runs
animal_sound_demo(my_cat) # Cat's sound runs
animal_sound_demo(generic_animal) # Animal's sound runs

print("\n--- Using a list/array for dynamic calls ---")
animals = [Dog(), Cat(), Animal(), Dog()]
for animal in animals:
    animal_sound_demo(animal)