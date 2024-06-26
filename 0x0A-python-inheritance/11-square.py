#!/usr/bin/python3
""" A square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Sqare class """
    def __init__(self, size):
        """ A constructor """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Area function """
        return self.__size * self.__size

    def __str__(self):
        """ Print ans str funciton """
        return "[Square] {}/{}".format(self.__size, self.__size)
