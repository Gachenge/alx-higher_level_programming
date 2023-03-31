#!/usr/bin/python3
"""takes email as parameter and posts it then print response"""
from sys import argv
import requests


if __name__ == "__main__":
    request = requests.post(argv[1], data={'email': argv[2]})

    print(request.text)
