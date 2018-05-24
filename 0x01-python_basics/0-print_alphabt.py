#!/usr/bin/python3
import string

'''
print alaphabet except 1 and e
'''
for i in string.ascii_lowercase:
    if i == 'q' or i == 'e':
        pass
    else:
        print (i, end='')
