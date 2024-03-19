#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in my_list:
        if(i == my_list[-1]):
            print("{:d}".format(i))
        else:
            print("{:d}".format(i), end="\n")
    return
