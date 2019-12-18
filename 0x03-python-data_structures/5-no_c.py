#!/usr/bin/env python3
def no_c(my_string):
    replace = ""
    charr = "Cc"
    count = 0

    for i in my_string:
        if i not in charr:
            replace = replace + my_string[count]
        count = count + 1

    return replace
