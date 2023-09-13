#!/usr/bin/python3
"""Module supplies empty class BaseGeometry"""


class BaseGeometry:
    """Empty class BaseGeometry

    Methods:
        area: raises exception - area not implemented

    """
    def area(self):
        """area method Not implemented

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value parameter

        Params:
            name (str): name
            value (any)

        Raises:
            TypeError: if value not int
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
