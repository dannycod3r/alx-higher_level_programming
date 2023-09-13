#!/usr/bin/python3
"""Module supplies the function to_json_string"""
import json


def to_json_string(my_obj):
    """the function returns the JSON representation of
    an object (string)

    Args:
        my_obj: string"""
    my_json = json.dumps(my_obj)
    return my_json
