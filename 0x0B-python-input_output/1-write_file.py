#!/usr/bin/python3
"""just read"""


def read_file(filename=""):
    """read only"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
