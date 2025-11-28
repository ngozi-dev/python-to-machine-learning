#!/usr/bin/python3
# a module that creates a dictionary

new_dict = {
    "brand": "toyota",
    "colour": "blue",
    "make": "camry",
    "mirage": 24000,
}
print(type(new_dict))

cars = dict()
print(type(cars))
print(new_dict)

# how to add to a dict
cars.update({"japanes": ["toyota", "honda", "lexus"]})
print(cars)


cars["price"] = 12000000
print(cars)