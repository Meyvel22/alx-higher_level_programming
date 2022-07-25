#!/usr/bin/python3
"""
   2-matrix_divide: matrix_divide()
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mess_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(mess_type)

    length = 0
    mess_size = "Each row of the matrix must have the same size"

    for elemn in matrix:
        if not elemn or not isinstance(elemn, list):
            raise TypeError(mess_type)

        if length != 0 and len(elemn) != length:
            raise TypeError(mess_size)

        for num in elemn:
            if not type(num) in (int, float):
                raise TypeError(mess_type)

        length = len(elemn)

    z = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (z)
