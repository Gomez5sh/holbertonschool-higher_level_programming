#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = {}
    for a in my_list:
        if a not in uniq:
            uniq[a] = 1
        else:
            uniq[a] += 1
    summ = 0
    for it in uniq:
        summ = summ = 1
    return summ
