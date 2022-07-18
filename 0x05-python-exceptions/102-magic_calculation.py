#!/usr/bin/python3
def magic_calculation(a, b):
    # magic_calculation - function that workd exactly like a bytecode

    ans = 0
    for y in range(1, 3):
        try:
            if y > a:
                raise Exception('Too far')
            ans += a ** b / y
        except Exception:
            ans = b + a
            break
    return (ans)
