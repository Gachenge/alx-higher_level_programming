#!/usr/bin/python3

def read_file(filename=""):
    """read the contents of a file"""
    with open("my_file_0.txt") as f:
        for i in f:
            print(i)
