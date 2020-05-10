"""
This module contains varous helper functions.
"""


def merge_bytes(*args):
    """Returns a single list of int from given int and list of int.

    :param int,list[int] args: Values to merge
    :rtype: list[int]

    >>> from rivalcfg.helpers import merge_bytes
    >>> merge_bytes(1, 2, 3)
    [1, 2, 3]
    >>> merge_bytes([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> merge_bytes(1, [2, 3], 4)
    [1, 2, 3, 4]
    """
    result = []
    for arg in args:
        if type(arg) in [list, tuple]:
            result.extend(arg)
        else:
            result.append(arg)
    return result