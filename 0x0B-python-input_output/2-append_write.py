#!/usr/bin/python3
"""Module 2-append_write supplies th function append_write"""


def append_write(filename="", text=""):
    """The function  appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename: the file to be appended
        text: the text to appended"""
    with open(filename, mode='a', encoding='utf-8') as file:
        n_chars_appended = file.write(text)
        return n_chars_appended
