#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # complex_delete - deletes keys with specific value in a dictionary

    key_list = list(a_dictionary.keys())
    for dict_value in key_list:
        if value == a_dictionary.get(dict_value):
            del a_dictionary[dict_value]

    return (a_dictionary)
