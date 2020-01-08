#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        dev = a / b
        return(dev)
    except (ZeroDivisionError):
        dev = None
    finally:
        print("Inside result: {}".format(dev))
