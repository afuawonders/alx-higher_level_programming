#!/usr/bin/python3
def matrix_divided(matrix, denominator):
    error = "matrix should be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(error)
    if not isinstance(matrix, list):
        raise TypeError(error)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(error)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(error)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(error)
    if not isinstance(denominator, int) and not isinstance(denominator, float):
        raise TypeError("denominator must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix should have the same size")
    if denominator == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / denominator, 2) for item in lists]
            for lists in matrix]
