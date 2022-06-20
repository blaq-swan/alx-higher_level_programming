#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    item = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            item += 1
        except IndexError:
            pass
    print()
    return item
