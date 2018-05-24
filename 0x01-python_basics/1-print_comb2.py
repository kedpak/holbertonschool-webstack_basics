#!/usr/bin/python3

'''
Print numbers from 0 to 99
'''


def print_comb2():
    ''' print numbers '''

    for i in range(100):
        if i == 99:
            print ("%02d" % (i,))
        else:
            print ("%02d" % (i,), end=', ')
        i += 1


print_comb2()
