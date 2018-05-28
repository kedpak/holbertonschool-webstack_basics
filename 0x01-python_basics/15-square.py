#!/usr/bin/python3
'''
print square
'''


class Square:
    def __init__(self, size=0):
        '''constructor'''
        self.size = size

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''return area'''
        return self.__size * self.__size

    def my_print(self):
        '''print squares'''
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print('')
