#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    alis = []
    c = 0
    for i in range(list_length):
        try:
            c = (my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError):
            print("division by 0")
            c = 0
        except (TypeError):
            print("wrong type")
            c = 0
        except (IndexError):
            print("out of range")
            c = 0
        finally:
            alis.append(c)
    return alis
