#!/usr/bin/python3
"""if the error code is greater than or equal to 400
display error code or the text
"""
from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
