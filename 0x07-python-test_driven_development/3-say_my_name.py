#!/usr/bin/python3
"""say my name module"""


def say_my_name(first_name="", last_name=""):
    """print full name
    Arges:
        first_name: first name
        last_name: last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if (first_name == "") and (last_name == ""):
        raise ValueError("missing two arguments")
    print("My name is {:s} {:s}".format(first_name, last_name))
