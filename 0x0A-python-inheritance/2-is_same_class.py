#!/usr/bin/python3
"""class for check the equality of obj and class"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the specified
    class and return true otherwise false"""
    return type(obj) == a_class
