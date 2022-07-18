#!/usr/bin/python3
def safe_function(fct, *args):
    # safe_function - function that executes a function safely

    import sys
    try:
        ans = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        ans = None

    return (ans)
