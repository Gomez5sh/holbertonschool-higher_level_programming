#!/usr/bin/python3
def print_last_digit(number):
        f = (number % 10) if number > 0 else (-number) % 10

        print("{:d}".format(f), end='')
        return f
