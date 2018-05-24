#!/usr/bin/python3

'''
check if character is lower case
'''


def islower(c):
    '''return true if lower'''
    for i in c:
        if ord(i) < 123 and ord(i) > 96:
            return True
        if ord(i) > 64 and ord(i) < 91:
            return False
