#!/usr/bin/python3
"""Module supplies the function write_file()"""


def write_file(filename="", text=""):
    """The function  writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename: the file to be written
        text: the text to wrtie"""
    with open(filename, mode='w', encoding='utf-8') as file:
        n_chars = file.write(text)
        return n_chars
