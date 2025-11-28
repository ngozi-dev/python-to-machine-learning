#!/usr/bin/python3
# a module that creates a 3 x 3 matrix 
# 12-matrix.py


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print(row)


def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for ele in row:
            total += ele
    return total


if __name__ == "__main__" :
    result = sum_matrix(matrix)
    print(result)
