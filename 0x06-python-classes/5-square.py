#!/usr/bin/python3
"""square class"""


class Square:
    """defines square"""

    def __init__(self, size=0):
        """init
        Args:
            size: length
        """

        self.__size = size

    @property
    def size(self):
        """property for the length

        raises:
            type error: if size not integer
            value error: if size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    def area(self):
        """area"""
        return self.__size ** 2
    def my_print(self):
        """print"""
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
