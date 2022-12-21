#!/usr/bin/python3

"""ADDING GETTERS AND SETTERS TO SQUARE CLASS
"""


class Square:
    """Initializing class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: Length of the square(int)
            position: Position on the square(tuple of 2)
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Computes area of a square
            Return:
                Area of square [INT]
        """
        return self.__size ** 2

    @property
    def size(self):
        """
            Return:
                size: Length of the square(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Args:
                value: Length of the square(int)
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
            Return:
                None
            Output:
                Print square
        """
        if self.__size == 0:
            print("")
            return
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
            return

    @property
    def position(self):
        """
            Return:
                Position: A tuple of 2(int)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Args:
                value: Position on the square (x, y)
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
