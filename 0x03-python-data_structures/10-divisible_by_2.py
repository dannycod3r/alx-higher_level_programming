#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_my_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            bool_my_list[count] = True
        else:
            bool_my_list[count] = False
    return(bool_my_list)


if __name__ == "__main__":
    divisible_by_2(my_list=[])
