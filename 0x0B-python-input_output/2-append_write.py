#!/usr/bin/python3
"""function to append a string to the end of a file"""


def append_write(filename="", text=""):
    """append a text to a file.
    create the file if necessary
    """
    with open(filename, 'a', encoding='utf8') as f:
        return (f.write(text))
