#!/usr/bin/python3

for x in range(97, 123):
    if chr(x) not in 'eq':
        print("{}".format(chr(x)), end='')
