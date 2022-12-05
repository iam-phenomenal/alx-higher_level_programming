#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    out_list = []
    for i in my_list:
        if i % 2 == 0:
            out_list.append(True)
        else:
            out_list.append(False)
    return out_list
