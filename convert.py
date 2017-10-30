#!/usr/bin/env python


atoi = int


def itoa(integer):
    try:
        if int(integer) == integer:
            return str(integer)
    except TypeError:
        pass
    raise ValueError()
