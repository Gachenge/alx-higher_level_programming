#!/usr/bin/python3
def safe_print_integer(value):
    val = False
    try:
        print("{:d}".format(value))
        val = True
    except:
        print("{}".format(value))
    return (val)
