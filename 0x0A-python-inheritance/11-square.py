#!/usr/bin/python3
"""we need to import rectangle and make square subclass of it"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square is subclass of rectangle which is sub class of
    basics geometry"""

    def __init__(self, size):
        """initial state of arguments"""
        self.__size = size
        self.integer_validator("size", self.__size)
        Rectangle.__init__(self, self.__size, self.__size)

    def area(self):
        """return the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """return (side of square/side of square)"""
        return f"[Square] {self.__size}/{self.__size}"

