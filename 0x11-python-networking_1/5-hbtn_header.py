#!/usr/bin/python3
import requests
from sys import argv
"""sends request t url and displays value of x-request-id"""


if __name__ == "__main__":
    request = requests.get(argv[1])
    html = request.headers['X-Request-Id']

    print(html)
