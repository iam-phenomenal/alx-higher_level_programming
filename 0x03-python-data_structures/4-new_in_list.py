#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    max_idx = len(my_list)
    new_list = my_list[:]
    if idx < 0:
        return my_list
    elif idx > max_idx - 1:
        return my_list
    else:
        new_list[idx] = element
        return new_list
