#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # print_list_integer - function that prints all integers of a list

    for x in range(len(my_list)):
            print("{:d}".format(my_list[x]))
