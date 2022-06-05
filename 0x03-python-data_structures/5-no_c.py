#!/usr/bin/python3

def no_c(my_string):
    my_list = [i for i in my_string]

    for x in my_list:
        if x in 'cC':
            my_list.remove(x)

    string = ''
    for x in my_list:
        string += x

    return string
