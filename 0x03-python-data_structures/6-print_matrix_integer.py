#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for component in matrix:
        if isinstance(component, list):
            if len(component) == 0:
                print("")
            for element in component:
                if component.index(element) == len(component) - 1:
                    print("{:d}".format(element))
                else:
                    print("{:d} ".format(element), end="")
        else:
            print("{:d}".format(component))
