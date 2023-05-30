#!/usr/bin/python3
"""Module 1-square

Module contains definition of class Square
"""


class Square:
    """A class that defines a square"""

    def __init__(self, size):
        """Initialize a new square set size to private

        Args:
            size: Size of the square
        """
        self.__size = size
