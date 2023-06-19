#!/usr/bin/python3
"""Module contains class Rcetangle"""
from .base import Base


class Rectangle(Base):
    """Blueprint for rectangles

    Attributes:
         width: width\n
        height: height\n
             x: x\n
             y: y\n

    Methods:
        area(): return the area of rectangle
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

    #
    def __str__(self):
        """Return an informal representation of a rectangle instance"""
        return f"[Rectangle] \
({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

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

    # Get the area of a rectangle
    #############################
    def area(self):
        """Return the area of a reactangle"""
        return self.width * self.height

    # Print the rectangl with #
    ###########################
    def display(self):
        """Print the rectangle with respect to x and y"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """update the details of an existing rectangle

        Update in the format: Rectangle(id, width, height, x, y)

        Args:
            *args: variable length argument"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
