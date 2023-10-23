#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        numm = fct(*args)
        return numm
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return None

