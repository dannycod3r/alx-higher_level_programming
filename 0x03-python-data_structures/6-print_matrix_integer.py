#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(element) for element in row))


if __name__ == "__main__":
    print_matrix_integer(matrix[[]])
