#!/usr/bin/python3
import requests
"""script that fetches from url must use requests package"""

if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t - type: {}".format(type(request.text)))
    print("\t - content: {}".format(request.text))
