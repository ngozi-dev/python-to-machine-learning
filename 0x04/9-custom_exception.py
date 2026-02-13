#!/usr/bin/python3
# a module that defines custom exception class.
# Define your own custom exception class. 
# Then write a function that raises this exception 
# when a specific condition is not met (for example, 
# when a number is negative). Handle the exception gracefully 
# and return a message confirming that the custom exception 
# was triggered.

def test_check_positive(value):
    
    try:
        if value < 0:
            raise ValueError("Value is negative, use a positive number")
            print(value)
    except Exception as e:
        print(f"Custom exception triggered: {e}")

if __name__ == "__main__":
    test_check_positive(-1)        


