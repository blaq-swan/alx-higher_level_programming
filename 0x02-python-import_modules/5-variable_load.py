#!/usr/bin/python3


def print_imported_variable():
    import variable_load_5

    return variable_load_5.a


if __name__ == "__main__":
    print(print_imported_variable())
