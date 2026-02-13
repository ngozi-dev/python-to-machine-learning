#!/usr/bin/python3
# a module that performs the sum of numbers from 1 to 50 using a loop

for i in range(1, 51):
    total = sum(range(1, i + 1))
    print(f"The sum of numbers from 1 to {i} is {total}. ")
    
