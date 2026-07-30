#!/usr/bin/python3
"""Defines a function that converts a class instance to JSON dictionary."""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure."""
    return obj.__dict__
