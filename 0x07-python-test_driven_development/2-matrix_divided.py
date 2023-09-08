#!/usr/bin/python3
"""Module: 2-matrix_divided
Supplies the function matrix_divided
"""


def matrix_divided(matrix, div):
    """Function: matrix_divide
    Divides all elements of a matrix

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float)

    Raises:
        TypeError: if matrix is not list of lists of float or int
        TypeError: if matrix row are not the same size
        TypeError: if div not float or int
        ZeroDivisionError: if div is 0
    """
    # check matrix type here
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # list of lists of int, floats
    if not all(isinstance(row, list)
               and all(isinstance(elem, (int, float))
                       for elem in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # check if Each row of the matrix must have the same size
    # length of first row
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check for 0 division
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(elem / div, 2) for elem in row]
        for row in matrix
        ]

    return new_matrix
