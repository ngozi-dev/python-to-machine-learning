#!/usr/bin/python3
# a module that handles opening a file 

file = open("students.txt", encoding = "utf-8")

print(file.read())
file.close()