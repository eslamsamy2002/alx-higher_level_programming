#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """print a square of #
    Args:
        size: The int size of the square's side.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return ""
    print((("#" * size + "\n") * size), end="")
