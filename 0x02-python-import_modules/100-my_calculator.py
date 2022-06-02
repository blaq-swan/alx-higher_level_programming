#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def calculator():
    operators = ['+', '-', '*', '/']

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(0)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        result = ''

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            result = div(a, b)

        print("{} {} {} = {}".format(a, operator, b, result))
        sys.exit(0)


if __name__ == '__main':
    calculator()
