#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 > idx < (len(my_list) - 1):
        return (my_list)
    new_list = my_list[:idx] + [element] + my_list[idx + 1:]
    return (new_list)
