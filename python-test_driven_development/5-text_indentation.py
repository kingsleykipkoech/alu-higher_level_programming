#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: String text to indent.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
