#!/usr/bin/python3
# a module that deletes item from a dictionary

person = {
    "name": "ngozi",
    "age": 70,
    "career": "civil servant",
    "city": "kubwa",
    "country": "nigeria"
}

del person["age"]
print(person)

# another method of deleting a key from a dict using pop
person.pop("name")
print(person)

# another method of deleting a key from a dict using .popitem()
# this will delete the last key in the dictionary
person.popitem()
print(person)


# another method of deleting that delets every items in the dictionary
person.clear()
print(person)