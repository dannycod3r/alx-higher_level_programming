#!/usr/bin/python3
"""Module 4-square

Contains definition of class Square
"""


class Square:
    """Defines type Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the object

        Args:
            size: Size of square
            position: Tuple of the form (x, y)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
