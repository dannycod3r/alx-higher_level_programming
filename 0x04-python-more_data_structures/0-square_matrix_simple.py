#!/usr/bin/python3
def create_matrix_same_size(row_size, col_size):
    new_matrix = []
    for i in range(row_size):
        row = [0] * col_size
        new_matrix.append(row)

    return new_matrix


def square_matrix_simple(matrix=[]):
    row_size = len(matrix)
    col_size = len(matrix[0])

    new_mat = create_matrix_same_size(row_size, col_size)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            new_mat[r][c] = matrix[r][c] ** 2

    return new_mat


if __name__ == "__main__":
    square_matrix_simple(matrix=[])
