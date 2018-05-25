#!/usr/bin/python3
'''
replace element of list
'''


def replace_in_list(my_list, idx, element):
    ''' return new list '''
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
    return my_list
