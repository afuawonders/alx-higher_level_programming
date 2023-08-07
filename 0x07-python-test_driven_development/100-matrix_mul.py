#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplication function."""


def matrix_mul(firstMatrix, secondMatrix):
    """Multiply two matrices.
    Args:
        firstMatrix (list of lists of ints/floats): The first matrix.
        secondMatrix (list of lists of ints/floats): The second matrix.
    Returns:
        A new matrix representing the multiplication of
        firstMatrix by secondMatrix.
    """

    if firstMatrix == [] or firstMatrix == [[]]:
        raise ValueError("firstMatrix should not be empty")
    if secondMatrix == [] or secondMatrix == [[]]:
        raise ValueError("secondMatrix should not be empty")

    if not isinstance(firstMatrix, list):
        raise TypeError("firstMatrix must be a list")
    if not isinstance(secondMatrix, list):
        raise TypeError("secondMatrix should be a list")

    if not all(isinstance(row, list) for row in firstMatrix):
        raise TypeError("firstMatrix should be a list of lists")
    if not all(isinstance(row, list) for row in secondMatrix):
        raise TypeError("secondMatrix should be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in firstMatrix for num in row]):
        raise TypeError("firstMatrix should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in secondMatrix for num in row]):
        raise TypeError("secondMatrix should contain only integers or floats")

    if not all(len(row) == len(firstMatrix[0]) for row in firstMatrix):
        raise TypeError(" row of firstMatrix should be of the same size")
    if not all(len(row) == len(secondMatrix[0]) for row in secondMatrix):
        raise TypeError("row of secondMatrix  should be of the same size")

    if len(firstMatrix[0]) != len(secondMatrix):
        raise ValueError("firstMatrix and secondMatrix can't be multiplied")

    reversed = []
    for r in range(len(secondMatrix[0])):
        additionalRow = []
        for c in range(len(secondMatrix)):
            additionalRow.append(secondMatrix[c][r])
        reversed.append(additionalRow)

    matrix = []
    for row in firstMatrix:
        additionalRow = []
        for col in reversed:
            prod = 0
            for i in range(len(reversed[0])):
                prod += row[i] * col[i]
            additionalRow.append(prod)
        matrix.append(additionalRow)

    return matrix
