#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [x for x in my_list]
    for i in range (len(new_list)):
        if i == idx:
            new_list[i] = element
    return (new_list)
