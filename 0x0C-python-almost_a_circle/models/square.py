#!/usr/bin/python3
"""Module supplies the class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class serves as blueprint for squares

    Parent class: models.Rectangle

    Methods:
        area - return the area of the rectangle
        update - update the attributes of a rectangle instance
        to_dictionary - return dictionary form of object
        display - display rectangle using '#' sign
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size - size of square(width, height)
            x - x coordinate
            y - y coordinate
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Informal representation of rectangle
        """
        # [Square] (<id>) <x>/<y> - <size>
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    # Getter
    @property
    def size(self):
        """Return size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square
        """
        obj_args = [
            'id', 'size', 'x', 'y'
            ]
        if args:
            for i in range(len(args)):
                setattr(self, obj_args[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the string representation of the square
        instance
        """
        # {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
