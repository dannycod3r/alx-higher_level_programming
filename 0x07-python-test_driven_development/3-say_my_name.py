#!/usr/bin/python3
"""Module 3-say_my_name
Supplies the function say_my_name()
Which prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Params:
        first_name: string
        last_name: string

    Raises:
        TypeError: if first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
