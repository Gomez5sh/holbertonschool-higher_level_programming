#!/usr/bin/env python3
def no_c(my_string):
    replace = list(my_string)
    [replace.remove(n) for n in replace if n == 'C' or n == 'c']
    return ("".join(replace))
