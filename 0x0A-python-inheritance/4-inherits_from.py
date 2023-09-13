#!/usr/bin/python3
"""Module supplies the function
inherits_from()
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    if issubclass(obj.__class__, a_class):
        if isinstance(obj, a_class):
            return True

    return False
