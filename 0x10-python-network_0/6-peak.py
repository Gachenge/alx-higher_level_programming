#!/usr/bin/python3
"""find the peak"""


def find_peak(list_of_integers):
    """find peak in an unsorted integers."""
    size = len(list_of_integers)
    mid = size // 2
    end = size
    
    if size == 0:
        return None
    
    while True:
        end = end // 2
        if (mid < size - 1 and list_of_integers[mid] <
                list_of_integers[mid + 1]):
            if end // 2 == 0:
                end = 2
            mid = mid + (end // 2)
        elif end > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if end // 2 == 0:
                end = 2
            mid = mid - (end // 2)g
        else:
            return list_of_integers[mid]
