#!/usr/bin/python3
"""Module 2-is_same_class

Supplies the function is_same_class
"""


def is_same_class(obj, a_class):
    """is_same_class(obj, a_class) -> bool

    Args:
        obj: object
        a_class: the class

    Returns:
        True if the object is exactly an instance of
        the specified class else False
    """
    return type(obj) is a_class
