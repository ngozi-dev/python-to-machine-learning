#!/usr/bin/python3
# a module that creates a matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_2 = [[1, 2], [4, 5]]

matrix_3 = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    print(row)
    

for row in matrix:
    for el in row:
        print(el, end=", ")
    print()


