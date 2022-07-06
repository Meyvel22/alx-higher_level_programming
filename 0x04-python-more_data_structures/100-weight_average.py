#!/usr/bin/python3
def weight_average(my_list=[]):
    # weight_average - returns the weighted average of all integers tuple

    if not my_list:
        return (0)

    top = 0
    down = 0

    for avg in my_list:
        top += avg[0] * avg[1]
        down += avg[1]

    return (top / down)
