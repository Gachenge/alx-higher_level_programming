#!/usr/bin/python3
"""function to write into a text file"""


def write_file(filename="", text=""):
    """write a text to a file in utf8
    create the file if it doesnt exist, or overwrite
    """
    with open(filename, 'w', encoding='utf8') as f:
        return(f.write(text))
