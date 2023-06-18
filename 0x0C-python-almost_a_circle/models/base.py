#!/usr/bin/python3
"""Module contains the class Base"""


class Base:
    """Base class for all shapes

    Attributes:
        __nb_object: number of objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id: id of new instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
