#!/usr/bin/python3
"""square class"""


class Square:
    """defines square"""

    def __init__(self, size=0, position=(0, 0)):
        """init
        Args:
            size: length
            position: ...
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter"""
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(num, int) and num >= 0 for num in value):
                self.__position = value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """square"""
        return self.size**2

    def my_print(self):
        """print a line"""
        if self.size == 0:
            print()
            return
        """print a square of # in position"""
        print(
            ("\n" * self.position[1])
            + ((" " * self.position[0]) + ("#" * self.size + "\n")) * self.size,
            end="",
        )

    def __str__(self):
        """same thing in my_print string of a square of # in position"""
        if self.size == 0:
            return ""
        else:
            my_string = ("\n" * self.position[1]) + (
                (" " * self.position[0]) + ("#" * self.size + "\n")
            ) * (self.size)

            return my_string.rstrip("\n")
