#!/usr/bin/python3
"""Module 10-square supplies the class Square"""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """

        """
        super().integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """Return an informal representation of Rectangle"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """Override area method"""
        return self.__size ** 2
