#!/usr/bin/python3
"""Module 3-square

Contains definition of class Square
"""


class Square:
    """Defines type Square"""

    def __init__(self, size=0):
        """Initialize the object

        Args:
            size: Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Find the area of the square
        Returns:
            size * size
        """
        return self.__size ** 2
