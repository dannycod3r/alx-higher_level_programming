#!/usr/bin/python3
"""Module: 2-rectangle.py
Supplies the class: Rectangle
Which: defines a rectangle
"""


class Rectangle:
    """Class: Rectangle
    Purpose: Defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """Constructor for objects"""
        self.width = width
        self.height = height


    # getters
    @property
    def width(self):
        """Return the width of the Rectangle"""
        return self.__width

    @property
    def height(self):
        """Return the height of the Rectangle"""
        return self.__height

    # setters
    @width.setter
    def width(self, value):
        """Set the width of the Rectangle

        Param:
            value: width of the Rectangle

        Raises:
            TypeError: if width not integer
            ValueError: if width less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle

        Param:
            value: height of the Rectangle

        Raises:
            TypeError: if height not integer
            ValueError: if height less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Instant methods
    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
