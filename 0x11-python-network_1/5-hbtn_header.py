#!/usr/bin/python3
"""sends request to url and displays
value of x-request-id
"""
import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get(argv[1])
    html = dict(request.headers)
    print(html.get('X-Request-Id'))
