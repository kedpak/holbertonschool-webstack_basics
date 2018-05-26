#!/usr/bin/python3
'''
print dictionary in sorted order
'''


def print_sorted_dictionary(my_dict):
    '''
    print in order
    '''
    for key, value in sorted(my_dict.items()):
        print("{}: {}".format(key, value))
