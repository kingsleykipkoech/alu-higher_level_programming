#!/usr/bin/python3
"""Displays the X-Request-Id header of a given URL response using requests."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
