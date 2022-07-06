#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # print_sorted_dictionary - prints a dictionary by ordered keys

    sorted_list = sorted(a_dictionary.keys())
    for x in sorted_list:
        print("{}: {}".format(x, a_dictionary[x]))
