#!/usr/bin/python3
'''
delete key inside dictionary
'''


def simple_delete(my_dict, key=""):
    new_dict = my_dict

    if key in my_dict:
        new_dict.pop(key, None)
        return new_dict
    else:
        return my_dict
