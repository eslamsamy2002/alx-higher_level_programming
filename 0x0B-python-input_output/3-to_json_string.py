#!/usr/bin/python3
"""json string module"""

from json import dumps


def to_json_string(my_obj):
    """convert to json obj"""

    return dumps(my_obj)
