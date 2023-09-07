#!/usr/bin/python3
"""Module: 0-add_integer
Supplies the function add_integer
"""


def add_integer(a, b=98):
    """Function: add_integer
    Return the sum of two numbers

    Args:
        a: int
        b: int
    Raises:
        TypeError if a and b not int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
