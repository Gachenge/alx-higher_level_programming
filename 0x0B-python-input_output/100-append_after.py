#!/usr/bin/python3
"""function to insert text in text after"""

def append_after(filename="", search_string="", new_string=""):
    """search text and after a string, insert new strin
    won't manage file permissions or non existent file
    """
    content = ''
    with open(filename) as f:
         for line in f:
             content += line
             if search_string in line:
                 content += new_string
    with open(filename, 'w') as f:
        f.write(content)
