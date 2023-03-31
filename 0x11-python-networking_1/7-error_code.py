#!/usr/bin/python3
from sys import argv
import requests
"""if the error code is greater than or equal to 400"""


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
