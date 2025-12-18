#!/usr/bin/python3
# a module that attempts to open and read a text file
#Create a file called 6-read_file.py
#Write a function that attempts to open and read a text file. 
#Use exception handling to manage situations where 
#the file does not exist. The function should return 
#the file contents if successful, or an appropriate 
#message if the file is missing.
def read_file(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return "File does not exist."
    
            