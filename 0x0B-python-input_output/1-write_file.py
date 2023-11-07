#!/usr/bin/python3
"""write only"""


def write_file(filename="", text=""):
    """just write"""
    with open(filename, encoding="utf-8", mode="w") as file:
        return file.write(text)
