#!/usr/bin/python3
# a module that creates a tuple

# list of fruits using tuples
fruits = ("cherry", "mango", "watermellon", "apple", "cucumba")
# to print the type of data structure
print(type(fruits))
# to print the number of elements in the tuple
print(len(fruits))
#to print the first item on the tuple
print(fruits[0])
# to get the last item on the tuple
print(fruits[-1])
# to add other fruits
fruits += ("carrot", "pawpaw")
print(f"after appending new fruits: {fruits}")
# to convert tuple to list
New_fruits = list(fruits)
print(type(New_fruits))
print(New_fruits)
# to create a new tuple
profile = ("ngozi", "franciscaezeaku@gmail.com", "password123")

# to unpack tuple
name, email, password = profile
print(name)
print(email)
print(password)

# to repeat
print(profile * 3)

# how to search for an item in a tuple
for fruit in fruits:
    if fruit == "cherry":
        print("fruit fund")

# to find the index of an in a tuple
ids = 0
for fruit in fruits:
    if fruit == "cherry":
        print(ids)
    ids += 1


