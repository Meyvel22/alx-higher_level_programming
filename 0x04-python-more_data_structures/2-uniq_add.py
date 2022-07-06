#!/usr/bin/python3
def uniq_add(my_list=[]):
    # uniq_add - adds all unique integers in a list(only once for each integer)

    uniq_list = set(my_list)
    digit = 0
    for x in uniq_list:
        digit += x

    return (digit)
