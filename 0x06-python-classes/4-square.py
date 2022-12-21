#!/usr/bin/python3

"""ADDING GETTERS AND SETTERS TO SQUARE CLASS
"""


class Square:
    """Initializing class
    """

    def __init__(self, size=0):
        """
        Args:
            size: Length of the square(int)
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes area of a square
            Return:
                Area of square [INT]
        """
        return self.__size ** 2
