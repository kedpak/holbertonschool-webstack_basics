#!/usr/bin/python3
'''
divide two integers
'''


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
        return result
