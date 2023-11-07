#!/usr/bin/python3
"""append"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new string after each line"""
    with open(filename, 'r+', encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
