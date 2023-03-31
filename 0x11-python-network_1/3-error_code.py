#!/usr/bin/python3
"""script that sends a request and displays
the body of the response
"""
from urllib.error import HTTPError
from sys import argv
from urllib import request

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))

    except Exception as e:
        print("Error code: {}".format(e.code))
