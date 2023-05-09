#!/usr/bin/python3

def uppercase(str):
    """uppercase - convert a string to uppercase
    @str: string
    Return: convert all small case to upper case.
    """
    result = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{:s}".format(result))
