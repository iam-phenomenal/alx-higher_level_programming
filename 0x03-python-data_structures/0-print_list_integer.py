#!/usr/bin/python3

def print_list_integer(my_list=[]):
    items = range(len(my_list))
    for n in items:
        print("{}".format(my_list[n]))
