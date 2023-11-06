#!/usr/bin/python3
""" Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class is a subclass has same properties in
    basics geometry class"""

    def __init__(self, width, height):
        """initial state of arguments"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """return width/height"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
