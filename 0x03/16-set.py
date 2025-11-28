#!/usr/bin/python3
# a module that handles set creation

a = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}

print(a)
print(type(a))
b = {5, 6, 7, 8}

# set operations
print(a.intersection(b))

print(a.union(b))

print(a.difference(b))

print(b.difference(a))

print(a.isdisjoint(b))

print(a.symmetric_difference(b))

# set methods

a.add(7)
a.add(8)
print(f"after adding 7,8: {a}")

a.remove(2)
print(f"after removing 2: {a}")

a.pop()
print(f"after poping {a}")








