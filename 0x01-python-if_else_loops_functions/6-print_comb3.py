#!/usr/bin/python3

for x in range(10):
    for y in range(x + 1, 10):
        if x != y:
            z = f"{x}{y}"
            if z != '89':
                print("{}".format(z), end=", ")
            else:
                print(z)
