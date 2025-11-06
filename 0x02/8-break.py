#!/usr/bin/python3
# a module that impliment break

count = 1
while count <= 20:
    if count % 10 == 0:
        break
    print(count, end=", ")
    count += 1
