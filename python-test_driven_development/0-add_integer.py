#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function that adds two integers.
Floats are cast to integers before addition.
"""


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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a != a or a == float('inf') or
                                 a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b != b or b == float('inf') or
                                 b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    return int(a) + int(b)
