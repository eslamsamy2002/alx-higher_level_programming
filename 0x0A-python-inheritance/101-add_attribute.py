#!/usr/bin/python3
""" MyInt module"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object.

    Returns:
        Nothing
    """
    if hasattr(obj, "__dict__"):
        obj.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")
