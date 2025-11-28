#!/usr/bin/python3
# a module that displays items the key and value in a dictionary

person = {
    "name": "ngozi",
    "age": 70,
    "country": "nigeria",
    "friends": ["chioma", "onyi", "aka", "chucks"],
    "city": "saburi"
}


print(person.items())

for name, value in person.items():
    print(f"{name} -> {value}")
