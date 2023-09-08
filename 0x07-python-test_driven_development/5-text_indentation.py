#!/usr/bin/python3
"""Module provides function text_indentation"""


def text_indentation(text):
    """prints a text with 2 new
    lines after each of these characters: ., ? and :

    Param:
        text: string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()\
        .replace(".", ".\n\n")\
        .replace("?", "?\n\n")\
        .replace(":", ":\n\n")

    print(text)
