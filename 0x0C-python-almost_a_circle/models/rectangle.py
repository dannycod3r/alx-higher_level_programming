#!/usr/bin/python3
"""Module contains class Rcetangle"""
from models.base import Base


class Rectangle(Base):
    """Blueprint for rectangles

    Attributes:
         __width: width\n
        __height: height\n
             __x: x\n
             __y: y\n

    Methods:
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
             width: width\n
            height: height\n
                 x: x coord\n
                 y: y coord"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getters and Setters for width attribute
    #########################################
    @property
    def width(self):
        """Return the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value: width of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if <= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
