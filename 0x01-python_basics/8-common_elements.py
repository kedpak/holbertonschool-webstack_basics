#!/usr/bin/python3
'''
find common element of two sets
'''


def common_elements(set_1, set_2):
    '''
    return common element
    '''
    common = []

    for i in set_1:
        for j in set_2:
            if j == i:
                common.append(j)
    return common
