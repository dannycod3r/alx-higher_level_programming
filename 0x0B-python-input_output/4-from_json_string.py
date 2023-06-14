#!/usr/bin/python3
"""Module supplies the function"""
import json


def from_json_string(my_str):
    """the function  returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: json string"""
    my_obj = json.loads(my_str)
    return my_obj
