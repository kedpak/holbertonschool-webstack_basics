#!/usr/bin/python3
'''
print alaphabet except q and e
'''

def printAlpha():
    '''print alphabet'''
    c = 97
    i = 0
    while i < 26:
        if c == 101 or c == 113:
            pass
        else:
            print(chr(c), end='')
        c += 1
        i += 1

printAlpha()
