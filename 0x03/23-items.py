#!/usr/bin/python3
# a module that displays items the key and value in a dictionary

person = {
    "name": "ngozi",
    "age": 70,
    "country": "nigeria",
    "friends": ["chioma", "onyi", "aka", "chucks"],
    "city": "saburi"
}

# to print the key with its values together
print(person.items())

# to sperate the values from the keys
for name, value in person.items():
    print(f"{name} -> {value}")
