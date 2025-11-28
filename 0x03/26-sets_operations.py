#!/usr/bin/python3
# a module that displays students, and their subjects 


# Given sets
python_students = {"Alice", "Bob", "Charlie"}
java_students = {"Charlie", "Diana", "Ethan"}

# 1) Students who study both Python and Java
both = python_students & java_students

# 2) Students who study only Python
only_python = python_students - java_students

# 3) Students who study only Java
only_java = java_students - python_students

# Store results in a dictionary
results = {
    "both": both,
    "only_python": only_python,
    "only_java": only_java
}

# Print the dictionary
print(results)