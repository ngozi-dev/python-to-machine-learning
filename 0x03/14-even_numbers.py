#!/usr/bin/python3
# a module that Write a function get_even_numbers(numbers) that:

array = [2, 5, 8, 11, 14, 17]



def get_even_numbers(numbers):
    return [num for num in  numbers if num % 2 == 0] 


if __name__ == "__main__" :
    result = get_even_numbers(array)
    print(result)
    
