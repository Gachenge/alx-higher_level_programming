#!/usr/bin/python3
"""list 10 commits from the most recent to the oldest
repository rails by user rails
"""
import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get("https://api.github.com/repos/{}/{}/commits".
                           format(argv[1], argv[2]))
    if (request.status_code == 200):
        request_json = request.json()[:10]
        for commit in request_json:
            name = commit['commit']['author']['name']
            print("{}: {}".format(commit.get('sha'), name))
