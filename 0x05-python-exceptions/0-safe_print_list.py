#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # safe_print_list - function that prints x elements of a list.

    tally = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            tally += 1
        except IndexError:
            break
    print("")
    return (tally)
