#!/usr/bin/python3

def no_c(my_string):
    for x in my_string:
        if x in "Cc":
            my_string = my_string.split(x)
            my_string = "".join(my_string)
    return my_string
