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
        print(lst[idx])
    except IndexError:
        print(f"Index {idx} is out of range for a list of length {len(lst)}.")

if __name__ == "__main__":
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    get_element_at(num, 10)