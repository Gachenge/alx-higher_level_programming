#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        """print the list in ascending order"""
        print(sorted(self))
