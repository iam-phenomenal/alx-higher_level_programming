#!/usr/bin/python3

"""This module focuses on ALX task 3 [Python Classes]
"""


class Square:
    """Creating a class to check for input TypeError
    and ValueError
    """

    def __init__(self, size=0):
        """
        Args:
            size: Size of the square(int)
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Computes area of a square
            Return:
                Area of square [INT]
        """
        return self.__size ** 2
