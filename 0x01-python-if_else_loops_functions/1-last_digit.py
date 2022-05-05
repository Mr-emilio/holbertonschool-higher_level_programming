#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number >= 0:
    unid = number % 10
elif number < 0:
    unid = ((number * -1) % 10) * -1
if unid > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, unid))
elif unid == 0:
    print("Last digit of {0} is {1} and is 0".format(number, unid))
elif unid < 6 and unid != 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, unid))
