#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    target_keys = []
    for k, v in a_dictionary.items():
        if v == value:
            target_keys.append(k)

    for key in target_keys:
        del a_dictionary[key]

    return a_dictionary


if __name__ == "__main__":
    complex_delete(a_dictionary, value)
