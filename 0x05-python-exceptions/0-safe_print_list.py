#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    try:
        for n in range(x):
            print(my_list[n], end="")
    except:
        n -= 1
    finally:
        print()
        return (n + 1)
