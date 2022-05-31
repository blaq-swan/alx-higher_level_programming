#!/usr/bin/python3


def uppercase(str):
    count = 0
    string = ''

    while str[count:]:
        char = ord(str[count])
        if char in range(97, 123):
            string += chr(char - 32)
        else:
            string += chr(char)
        count += 1

    print("{}".format(string))
