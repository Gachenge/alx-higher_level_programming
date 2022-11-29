#!/usr/bin/python3
def uppercase(str):
    s = ""
    for i in str:
        if "a" <= i <= "z":
            s += chr(ord(i) - 32)
        else:
            s += i
    print("{}".format(s))
