#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # new_in_list - replaces an element in a list at a specific position\
           # without modifying the original list

    copy_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return (copy_list)
    copy_list[idx] = element
    return (copy_list)
