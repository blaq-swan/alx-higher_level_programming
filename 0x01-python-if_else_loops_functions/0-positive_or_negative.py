#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def zero_positive_or_negative(n):
    """
    prints a number is positive, negative, or zero
    """
    if n == 0:
        return f"{n:d} is zero"
    elif n > 1:
        return f"{n:d} is positive"
    else:
        return f"{n:d} is negative"


if __name__ == "__main__":
    print(zero_positive_or_negative(number))
