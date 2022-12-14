#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_ints = set(my_list)
    return sum(list(unique_ints))
