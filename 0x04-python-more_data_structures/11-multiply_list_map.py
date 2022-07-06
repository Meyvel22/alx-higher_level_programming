#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # multiply_list_map - returns a list with all values multplied by a number

    return (list(map(lambda x: x * number, my_list)))
