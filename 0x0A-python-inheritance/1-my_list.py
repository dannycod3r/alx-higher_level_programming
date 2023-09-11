#!/usr/bin/python3
"""Module supplies the class MyList
"""


class MyList(list):
    """Class Mylist

    Methods:
        print_sorted()
    """

    def print_sorted(self):
        """that prints the list, but
        sorted (ascending sort)
        """
        # pass
        new_list = self[:]
        new_list.sort()
        print(new_list)
