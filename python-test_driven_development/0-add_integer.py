#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Adds two integers or floats after casting floats to ints.

    Args:
        a: First integer or float.
        b: Second integer or float, defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
