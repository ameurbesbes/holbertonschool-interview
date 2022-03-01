#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    x = 0
    i = 2

    while (i <= n):
        if n % i == 0:
            x = x + i
            n = n / i
        else:
            i += 1

    return x
