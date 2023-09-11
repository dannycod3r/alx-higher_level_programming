#!/usr/bin/python3
"""Module supplies the function ``lookup``
"""


def lookup(obj):
    """Function returns the list of available
    attributes and methods of an object

    Param:
        obj: objects
    """
    return dir(obj)
