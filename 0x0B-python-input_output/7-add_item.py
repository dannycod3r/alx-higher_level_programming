#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then save them to a file"""
from sys import argv


def add_item():
    """function add_item adds commanline arguments to list"""
    filename = "add_item.json"
    save_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_json_file = __import__('6-load_from_json_file').load_from_json_file

    args_list = []
    args_list += argv[1:]

    save_json_file(args_list, filename)
    load_json_file(filename)


if __name__ == "__main__":
    add_item()
