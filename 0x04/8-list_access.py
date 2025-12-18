#!/usr/bin/python3
# a module that takes a list and an index, 
# then returns the element at that index. 
# Use exception handling to catch IndexError and 
# return a message indicating that the index is out of range.
# Write a function that takes a list and an index, 
# then returns the element at that index. 
# Use exception handling to catch IndexError and 
# return a message indicating that the index is out of range.

def get_element_at(lst, idx):

    try:
        return lst[idx]
    except IndexError:
        return f"Index {idx} is out of range for a list of length {len(lst)}."