#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # square_matrix_simple - computes the square value of all integer of matrix

    current_matrix = matrix.copy()
    for x in range(len(matrix)):
        current_matrix[x] = list(map(lambda x: x**2, matrix[x]))

    return (current_matrix)
