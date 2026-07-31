#!/usr/bin/python3
def magic_string():
    magic_string.strs = getattr(magic_string, 'strs', []) + ["BestSchool"]
    return ", ".join(magic_string.strs)
