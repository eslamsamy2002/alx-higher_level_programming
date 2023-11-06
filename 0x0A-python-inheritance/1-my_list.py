#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """a child class"""

    def print_sorted(self):
        """print the list in an ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
