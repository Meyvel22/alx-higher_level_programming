#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # multiply_by_2 - returns a new dictionary with all values multiplied by 2

    z_dictionary = {}
    for x in a_dictionary:
        z_dictionary[x] = a_dictionary[x] * 2
    return (z_dictionary)
