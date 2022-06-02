#!/usr/bin/python3

def calculator():
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    if len(args[1:]) != 3:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)
    if args[2] not in ['+', '-', "*", '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, operator,  b = int(args[1]), args[2], int(args[3])
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    calculator()
