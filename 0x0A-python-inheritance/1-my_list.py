#!/usr/bin/python3
"""Module 1-my_list supplies the class MyList"""

class MyList(list):
    """Class MyList a custom defined list class

    Child class of list

    Methods:
        print_sorted():  that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
