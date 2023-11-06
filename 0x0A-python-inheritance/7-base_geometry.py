#!/usr/bin/python3
"""Basic geometry class"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """check if the area not found?"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise exception if the name not integer and >zero"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
