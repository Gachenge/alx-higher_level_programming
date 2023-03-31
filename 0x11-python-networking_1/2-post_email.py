#!/usr/bin/python3
"""sends post email and displays the
body of the response
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen


if __name__ == "__main__":
    data = urlencode({'email': argv[2]}).encode('utf-8')
    req = Request(argv[1], data)

    with urlopen(req) as response:
        html = response.read()

    print(html.decode('utf-8'))
