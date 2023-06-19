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

    # Getters and Setters for height attribute
    #########################################
    @property
    def height(self):
        """Return the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value: height of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if <= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getters and setter for x attribute
    ####################################
    @property
    def x(self):
        """Return the x coord of the rectangle

        Args:
            value: x coord of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if < 0"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coord of the rectangle

        Args:
            value: x coord of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if < 0"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getters and setter for y attribute
    ####################################
    @property
    def y(self):
        """Return the y coord of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coord of the rectangle

        Args:
            value: y coord of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if < 0"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
