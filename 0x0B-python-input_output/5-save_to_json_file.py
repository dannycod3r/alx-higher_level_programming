#!/usr/bin/python3
"""Module supplies the fuction save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """the function  writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object/python data structure
        filename: the file to be written"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
