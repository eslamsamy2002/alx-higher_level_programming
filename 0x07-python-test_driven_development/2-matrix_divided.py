#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_error)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(matrix_error)
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elements in row:
            if not isinstance(elements, (int, float)):
                raise TypeError(matrix_error)
    new_matrix = []
    for list_of_int in matrix:
        my_row = []
        for number in list_of_int:
            my_row.append(round(number / div, 2))
        new_matrix.append(my_row)
    return new_matrix
