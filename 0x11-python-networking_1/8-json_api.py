#!/usr/bin/python3
"""takes a letter and sends a post request
with the letter as parameter"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    request = requests.post(argv[1], data={'q': q})
    try:
        post_request = request.json()
        if post_request:
            print("[{}] {}".format(post_request['id'], post_request['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
