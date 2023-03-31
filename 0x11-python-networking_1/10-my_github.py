#!/usr/bin/python3
import requests
from sys import argv
"""login to github using github api"""

if __name__ == "__main__":
    request = requests.get('https://api.github.com/user',
                           auth=(argv[1], argv[2]))
    if request.status_code == 200:
        request_json = request.json()
        print(request_json['id'])
    else:
        print("None")
