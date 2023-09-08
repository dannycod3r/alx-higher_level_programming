#!/usr/bin/python3
"""Module supplies the function print_square()"""


def print_square(size):
    """prints a square with the character #

    Param:
        size: length of square

    Raises:
        TypeError: if size not int
        ValueError: if size < 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    # if isinstance(size, float) and size < 0:
    #     raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)

    for i in range(size):
        print("#" * size)
