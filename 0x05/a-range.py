#!/usr/bin/python3
# a module that reads range

count = 0

for i in range (1, 10):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"We have {count} even numbers")
    