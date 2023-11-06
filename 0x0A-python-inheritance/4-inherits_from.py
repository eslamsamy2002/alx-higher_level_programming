#!/usr/bin/python3
"""is instance?"""


def inherits_from(obj, a_class):
    """check the instance"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
