#!/usr/bin/python3
"""find the peak"""


def find_peak(list_of_integers):
    
    if len(list_of_integers) < 1:
        return
    else:
        for i in range(len(list_of_integers)):
            if (list_of_integers[i] >= list_of_integers[i - 1] and
                    list_of_integers[i] >= list_of_integers[i + 1]):
                return (list_of_integers[i])
