#!/usr/bin/python3
"""append mode"""


def append_write(filename="", text=""):
    """append: write with saving old data"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
