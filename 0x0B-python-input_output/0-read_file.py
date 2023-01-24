#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    """read the contents of a file and print them out"""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end='')
