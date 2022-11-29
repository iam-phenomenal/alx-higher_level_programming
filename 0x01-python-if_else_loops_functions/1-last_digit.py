#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
remaider = number % 10
print("Last digit of {} is {}".format(number, remaider))
