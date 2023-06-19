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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
