#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    con = 0
    for n in range(x):
        try:
            print("{:d}".fotmat(my_list[n]), end="")
        except (ValueError, TypeError):
            continue
        else:
            con += 1
        print()
        return (con)
