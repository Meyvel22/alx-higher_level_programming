#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # search_replace - replaces all occurrences of an element by another list

    current_list = []
    for x in my_list:
        if x == search:
            current_list.append(replace)
        else:
            current_list.append(x)
    return (current_list)
