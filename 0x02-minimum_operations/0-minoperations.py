#!/usr/bin/python3
"""
0. minimum operations
"""


import math


def minOperations(n):
    factor = find_largest_prime_factor(n)
    value = factor + 1 + (n - factor) / factor
    print(value)
    return int(value)


def find_largest_prime_factor(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break

    return factors[-1]
