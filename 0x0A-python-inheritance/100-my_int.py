#!/usr/bin/python3
""" MyInt"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, other):
        """reverse true state"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """reverse true state"""
        return int.__eq__(self, other)
