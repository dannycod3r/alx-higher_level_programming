#!/usr/bin/python3
def print_last_digit(number):
    """print_last_digit - return the last digit of a number
    @number: the given number
    Return: the last digit the given number
    """
    last_num = abs(number) % 10
    print("{:d}".format(last_num), end="")
    return last_num
