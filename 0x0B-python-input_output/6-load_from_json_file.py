#!/usr/bin/python3
"""load from json file"""

from json import load


def load_from_json_file(filename):
    """load_from_json_file choose reading mode"""
    with open(filename, encoding="utf-8", mode="r") as file:
        return load(file)
