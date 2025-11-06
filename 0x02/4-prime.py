#!/usr/bin/python3
# a module that impliment prime numbers using for loop

for i in range(2, 101):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
        