#!/usr/bin/python3
# a module that accepts string

my_string = "I am a Python Programmer"
for char in my_string:
    print(char)

my_string = "Hello World"
char = my_string[0]
print(char)

#slicing operators
my_string = "Hello World"
substring = my_string[1:5]
print(substring)

#concatinating two or more strings
greeting = "Hello"
name = "Francisca"
sentence = (greeting + " " + name)
print(sentence)

# We can iterate over our string by using for loop
for i in name:
    print(i)

# To check if a character is in my string

if "F" in name:
    print("yes")
else:
    print("no")

# Using strip to close up spaces
greeting =  "  Hello World  "
print(greeting.strip())

# Changing our strings to upper, lower, title case
print(greeting.upper())
print(greeting.lower())
print(greeting.title())

# To check if a particular string starts with a particular character
print(my_string.startswith("Hello"))
print(my_string.endswith("Hello"))

# To find the index of a character
print(my_string.find("H"))

#To count the number of a particular character of a string
print(my_string.count("l"))

# To replace character or substring in our string by using replace
print(my_string.replace("World", "Universe"))





