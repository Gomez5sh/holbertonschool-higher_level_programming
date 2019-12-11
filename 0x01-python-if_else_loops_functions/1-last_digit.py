#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    i = number % 10
else:
    i = number % -10

if i > 5:
    print("last digit of {0} is {1} and is greater that 5".format(number, i))
elif i < 6 and i != 0:
    print("last digit of {0} is {1} and is less than 6 and not 0".format(number, i))
elif i == 0:
    print("last digit of {0} is {0} and is 0".format(i))
