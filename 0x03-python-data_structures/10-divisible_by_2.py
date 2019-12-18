#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    save = []
    for n in my_list:
        if n % 2 == 0:
            n = True
            save.append(n)
        else:
            n = False
            save.append(n)

            return save
