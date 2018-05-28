#!/usr/bin/python3
"""
print diagonals
"""


def print_diagonal(n):
    """Print diagonals based on n"""
    if n <= 0:
        print('\n')
        return
    i = 0
    j = 0
    count = 1
    while i < n:
        while j < count:
            if j + 1 == count:
                print('\\')
            else:
                print(' ', end='')
            j += 1
        count += 1
        i += 1
        j = 0
    return
