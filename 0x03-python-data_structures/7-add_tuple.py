#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = []
    tupa = list(tuple_a)
    tupb = list(tuple_b)
    for i in range(2):
        if len(tupa) < 2:
            tupa.append(0)
        if len(tupb) < 2:
            tupb.append(0)
        new.append(tupa[i] + tupb[i])
    return tuple(new)
