#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number div.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide matrix elements by.

    Returns:
        A new matrix containing the rounded quotient elements.

    Raises:
        TypeError: If matrix is invalid, rows differ in size, or div not a number.
        ZeroDivisionError: If div is 0.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(err_msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
