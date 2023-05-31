#!/usr/bin/python3
"""Module 4-square

Contains definition of class Square
"""


class Square:
    """Defines type Square"""

    def __init__(self, size=0):
        """Initialize the object

        Args:
            size: Size of square
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square

        Return:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Find the area of the square

        Returns:
            size * size
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square in #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
