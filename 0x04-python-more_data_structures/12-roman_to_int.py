#!/usr/bin/python3
def roman_to_int(roman_string):
    # roman_to_int - converts a Roman numeral to an integer

    ROMAN = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
             "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
             "D": 500, "CM": 900, "M": 1000}

    answer = 0
    if not isinstance(roman_string, str):
        return (answer)

    r_numeral = ROMAN.keys()
    n = len(roman_string)
    x = 0
    while x < n:
        check1 = roman_string[x:x+2]
        check2 = roman_string[x]
        if check1 in r_numeral:
            answer += ROMAN.get(check1)
            x += 2
        elif check2 in r_numeral:
            answer += ROMAN.get(check2)
            x += 1

    return(answer)
