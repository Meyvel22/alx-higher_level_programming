#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #print_reversed_list_integer - prints all integers of a list in reverse

    if my_list:
        for x in reversed(my_list):
            print("{:d}".format(x))
