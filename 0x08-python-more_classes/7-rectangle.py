#!/usr/bin/python3
"""Module 7-rectangle

Supplies the class Rectangle
"""


class Rectangle:
    """Defines the template for a rectangle

    Attributes:
        number_of_instances: keeps count of number of rectangle created

    Methods:
        height: return height or set the height of rectangle
        width: return width or set the width of rectangle
        area: return the area of the rectangle
        perimeter: return the perimeter of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __str__(self):
        """informal representation of object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for i in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """a formal representation of object"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """Destructor - print Bye rectangle... if object in deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __init__(self, width=0, height=0):
        """Initialize the rectangle

        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width to the given value

        Args:
            value(int): the new value

        Raises:
            TypeError: if width is not integer
            ValueError: if width is negative number
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

        Raises:
            TypeError: if height is not integer
            ValueError: if height is negative number
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retuns the area of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
