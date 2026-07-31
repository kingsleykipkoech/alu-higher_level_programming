#!/usr/bin/python3
"""Sends a POST request with a letter parameter to search_user API."""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        json_obj = r.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get("id"), json_obj.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
