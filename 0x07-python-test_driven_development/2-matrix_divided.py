#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    for row in range(len(matrix)):
        if row <= len(matrix) - 2 and len(matrix[row]) != len(matrix[row + 1]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix[row])):
            if type(matrix[row][i]) not in (int, float):
                raise TypeError(error)

    return list(map(lambda row: list(map(lambda x: round((x / div), 2), row)),
                matrix))
