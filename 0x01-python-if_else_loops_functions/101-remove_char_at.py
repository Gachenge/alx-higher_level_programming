#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        st1 = str
    else:
        st1 = str[:n] + str[n + 1:]
    return st1
