#!/usr/bin/python3
"""
print diagonals
"""


def print_diagonal(n):
    """Print diagonals based on n"""
    if n <= 0:
        print()
    else:
        for i in range(n):
            print(i * ' ' + '\\')
        print()
