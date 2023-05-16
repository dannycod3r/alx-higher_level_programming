#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for char in my_string:
        if ord(char) != ord('c') and ord(char) != ord('C'):
            new_str += char
    return new_str
