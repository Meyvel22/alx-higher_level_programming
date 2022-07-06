#!/usr/bin/python3
def roman_to_int(roman_string):
    # roman_to_int - function that converts a Roman numeral to an integer

    if type(roman_string) is not str or roman_string is None:
        return (0)
    full = 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for idx in range(len(roman_string)):
        x = rom_num.get(roman_string[idx])
        if (idx < len(roman_string[idx]) - 1):
            xx = rom_num.get(roman_string[idx + 1])
            if xx > x:
                full -= x
            else:
                full += x
        else:
            full += x
    return (full)
