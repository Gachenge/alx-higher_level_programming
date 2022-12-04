#!/usr/bin/python3
def no_c(my_string):
    st1 = ''
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        st1 = st1 + my_string[i]
    return (st1)
