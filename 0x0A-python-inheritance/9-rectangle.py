#!/usr/bin/python3
"""Module rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """class constructor"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Override the area method"""
        return self.__width * self.__height

    def __str__(self):
        """Return an informal representation of Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
