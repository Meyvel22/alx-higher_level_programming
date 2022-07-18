#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    # safe_print_integer_err - prints an integer
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
