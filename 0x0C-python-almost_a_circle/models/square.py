#!/usr/bin/python3
"""Module contains the class Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class definition for Square

    Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor

        Args:
            size: width/height
            x: x coord
            y: y coord
            id: id of instance
        """
        self.width = size
        self.height = size
        super().__init__(self.width, self.height, x, y, id)

    def __str__(self):
        """An informal representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
