#!/usr/bin/python3
"""Square module"""


class Square:
    """Class for defining a square"""
    def __init__(self, size=0):
        """This is the init function."""
        self.size = size

    @property
    def size(self):
        """Getter function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
