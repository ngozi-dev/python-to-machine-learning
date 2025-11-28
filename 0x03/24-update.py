#!/usr/bin/python3
# a module that updates city and country

person = {
    "name": "chioma",
    "age": 80,
    "country": "usa",
    "city": "washington DC",
    "friends": ["Rash", "Caly", "Onyi", "Ng"]

}

new_country = input("Enter any country of your choice")
new_city = input("Enter any city of your choice")

person["country"] = new_country
person["city"] = new_city

print(person)

# to sperate the values from the keys
for new_country, value in person.items():
    print(f"{new_country} -> {value}")