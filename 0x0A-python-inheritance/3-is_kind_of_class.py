#!/usr/bin/python3
"""Module 3-is_kind_of_class
supplies a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """check if an obj is an instance of or
    if the object is an instance of a class
    that inherited from, the specified class
    Return:
        True if affirmative else False
    """
    if isinstance(obj, a_class):
        return True
    return False
