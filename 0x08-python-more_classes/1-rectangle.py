#!/usr/bin/python3
"""Module 1-rectangle

Supplies the class Rectangle
"""


class Rectangle:
    """Defines the template for a rectangle

    Methods:
        height: return height or set the height of rectangle
        width: return width or set the width of rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize the rectangle

        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width to the given value

        Args:
            value(int): the new value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height to the given value

        Args:
            value(int): the new value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
