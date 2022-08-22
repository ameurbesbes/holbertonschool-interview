#!/usr/bin/python3
"""
n queen solver
"""
from sys import argv


def queens(n, i=0, a=[], b=[], c=[]):
    """
    find every possible solution
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def find_solution(n):
    """ solve every possible solution that
    generated by queens function
    """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


if len(argv) < 2 or len(argv) > 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
n = int(argv[1])
if n < 4:
    print("N must be at least 4")
    exit(1)
else:
    find_solution(n)
