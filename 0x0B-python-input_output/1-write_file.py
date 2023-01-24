#!/usr/bin/python3
"""function to write into a text file"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf8') as f:
        return(f.write(text))
