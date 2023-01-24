#!/usr/bin/python3

def read_file(filename=""):
    """read the contents of a file"""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end ='')
