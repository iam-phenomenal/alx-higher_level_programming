#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    idx = 0
    out_str = ""
    while idx < str_len:
        if my_string[idx] == "c" or my_string[idx] == "C":
            out_str += ""
        else:
            out_str += my_string[idx]
        idx += 1
    return out_str
