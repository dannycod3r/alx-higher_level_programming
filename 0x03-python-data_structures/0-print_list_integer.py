#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))


if __name__ == "__main__":
    print_list_integer(my_list=[])