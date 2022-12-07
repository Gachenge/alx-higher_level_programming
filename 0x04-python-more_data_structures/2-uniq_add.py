#!/usr/bin/python3
def uniq_add(my_list=[]):
    unq = []
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] not in unq:
            unq.append(my_list[i])
    for i in range(len(unq)):
        sum += unq[i]
    return sum
