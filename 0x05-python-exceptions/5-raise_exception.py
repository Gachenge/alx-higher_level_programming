#!/usr/bin/python3
def raise_exception():
    x = 'Hello'
    if not type(x) is int:
        raise TypeError("Not an integer")
