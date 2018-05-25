#!/usr/bin/python3
'''
remove c and C from string
'''


def no_c(str):
    '''remove character'''
    newChar = ''
    if str.find('c') != -1 or str.find('C') != -1:
        for i in str:
            if i != 'c' and i != 'C':
                newChar += i
    return newChar
