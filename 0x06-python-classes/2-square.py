#!/usr/bin/python3
"""Module 2-square

Module contains definition of class Square
"""


class Square:
    """A class that defines a sqaure"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            __size: Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
