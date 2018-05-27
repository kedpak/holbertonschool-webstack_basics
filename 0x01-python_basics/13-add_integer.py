#!/usr/bin/python3
'''
Add integers
'''


def add_integer(a, b):
    '''return int or float or raise TypeError
    '''
    try:
        a = int(a)
        b = int(b)
        return (a + b)
    except:
        if type(a) != int:
            raise TypeError('a must be an integer')
        else:
            raise TypeError('b must be an integer')
