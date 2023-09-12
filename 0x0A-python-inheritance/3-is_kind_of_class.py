#!/usr/bin/python3
"""Module supplies the function
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an
    instance of, or if the object is an
    instance of a class that inherited from, t
    he specified class ; otherwise False

    Param:
        obj: the object
        a_class: the class
    """
    return isinstance(obj, a_class)
