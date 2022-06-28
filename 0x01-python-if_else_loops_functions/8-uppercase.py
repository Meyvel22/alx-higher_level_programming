#!/usr/bin/python3
def uppercase(str):
    answer = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            answer += chr(ord(char) - 32)
        else:
            answer += char
    print("{:s}".format(answer))
