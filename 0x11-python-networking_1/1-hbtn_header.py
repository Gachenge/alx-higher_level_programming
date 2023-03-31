#!/usr/bin/python3
""""access url headers, the x-request-id value fro the key"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        html = response.headers['X-Request-Id']

    print(html)
