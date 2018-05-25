#!/usr/bin/python3

'''
print number of arguments
'''
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print ("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) > 1:
        print ("{} arguments:".format(len(sys.argv) - 1))
        for i in range(len(sys.argv)):
            if i > 0:
                print ("{}: {}".format(i, sys.argv[i]))
