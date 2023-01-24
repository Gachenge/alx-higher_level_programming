#!/usr/bin/python3
"""script that adds all arguments to a python list"""

import sys
import json

if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv

try:
    item = load_from_json_file('add_item.json')
except FileNotFoundError:
    item =[]
    item.extend(args[1:])
    save_to_json_file(item, 'add_item.json')
