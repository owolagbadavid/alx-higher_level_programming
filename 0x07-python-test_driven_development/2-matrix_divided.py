#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.
    """
    if type(matrix) is not list:
        raise TypeError(("matrix must be a matrix (list of lists) "
                        "of integers/floats"))
    for row in matrix:
        if type(row) is not list:
            raise TypeError(("matrix must be a matrix (list of lists) "
                            "of integers/floats"))
    for row in matrix:
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(("matrix must be a matrix (list of lists) "
                                "of integers/floats"))
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
