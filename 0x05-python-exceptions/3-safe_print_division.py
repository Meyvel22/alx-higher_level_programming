#!/usr/bin/python3
def safe_print_division(a, b):
    # safe_print_division - divides 2 integers and prints the result

    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
