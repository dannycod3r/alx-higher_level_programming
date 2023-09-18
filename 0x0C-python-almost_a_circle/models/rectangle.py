#!/usr/bin/python3
"""Module supplies the class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle blueprint for all rectangle

    Inherits: Base class

    Attributes:
        width - width of rectangle
        height - height of rectangle
        x - x coordinate
        y - y coordinate
        id - override super id

    Methods:
        area - return the area of the rectangle
        update - update the attributes of a rectangle instance
        to_dictionary - return dictionary form of object
        display - display rectangle using '#' sign
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width - width of rectangle
            height - height of rectangle
            x - x coordinate
            y - y coordinate
            id - id override parent id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Informal representation of rectangle
        """
        # [Rectangle] (<id>) <x>/<y> - <width>/<height>
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    # Getters
    @property
    def width(self):
        """Return the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Return the height of the rectangle
        """
        return self.__height

    @property
    def x(self):
        """Return the x coordinate of rectangle
        """
        return self.__x

    @property
    def y(self):
        """Return the y coordinate of rectangle
        """
        return self.__y

    # Setters
    @width.setter
    def width(self, value):
        """Validate and set width

        Args:
            value - width of rectangle

        Raises:
            TypeError - if width not int
            ValueError - if width is <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Validate and set width

        Args:
            value - height of rectangle

        Raises:
            TypeError - if height not int
            ValueError - if height is <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Validate and set width

        Args:
            value - x of rectangle

        Raises:
            TypeError - if x not int
            ValueError - if x is < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Validate and set width

        Args:
            value - y of rectangle

        Raises:
            TypeError - if y not int
            ValueError - if y is < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' sign
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)
        print()

    def update(self, *args, **kwargs):
        """Modify the object based on the provided arguments

        Args:
            args - non-keyword argument
            kwargs - keyword argument

        Note:
            args and kwargs must be in the arranged as
            id, width, height, x, y
        """
        obj_args = [
            'id', 'width', 'height', 'x', 'y'
            ]
        if args:
            for i in range(len(args)):
                setattr(self, obj_args[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of object

        {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        """

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
