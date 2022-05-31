#!/usr/bin/python3
import random
n = random.randint(-10, 10)
y = ['is positive', 'is negative', 'is zero']

print(f'{n} {y[0]}' if n > 0 else (f'{n} {y[1]}' if n < 0 else f'{n} {y[2]}'))
