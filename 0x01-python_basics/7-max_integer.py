#!/usr/bin/python3

'''
return largest integer of list
'''


def max_integer(my_list=[]):
    '''
    return max int
    '''
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i

    return max
