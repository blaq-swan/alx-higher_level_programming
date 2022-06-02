#!/usr/bin/python3


def print_hidden_names():
    import hidden_4 as hidden

    for name in dir(hidden):
        if not name.startswith('__'):
            print(name)


if __name__ == "__main__":
    print_hidden_names()
