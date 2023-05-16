#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    size = len(my_list) - 1
    while size >= 0:
        print("{:d}".format(my_list[size]))
        size -= 1


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
