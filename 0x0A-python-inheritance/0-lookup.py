#!/usr/bin/python3
"""Module 0-lookup supplies the function lookup(obj)"""


def lookup(obj):
    """lookup(obj)->list

    function returns the list of available \
    attributes and methods of an object:"""
    return list(dir(obj))
