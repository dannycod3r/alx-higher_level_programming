#!/usr/bin/python3
"""Module 0-read_file supplies the function
read_file"""


def read_file(filename=""):
    """the function reads a text file (UTF8) and
    prints it to stdout

    Args:
        filename: the filename containing content"""
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content)
