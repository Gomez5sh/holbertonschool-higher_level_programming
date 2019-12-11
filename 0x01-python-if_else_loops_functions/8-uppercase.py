#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) > 96 & ord(n) < 123:
            n = chr((ord(n) - 32))

            print("{}".format(n), end='')

    print()
