#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if len(my_list) == 0:
        return (None)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
