#!/usr/bin/python3
"""
Module 0-add_integer

Methods: add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be integer")
    return int(a) + int(b)
