#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
mod = abs(number) % 10

if mod < 6  and mod > 0:
    print(f"Last digit of {number:d} is {mod:d} and "
          f"is less than 6 and not 0")
elif mod > 5:
    print(f"Last digit of {number:d} is {mod:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {mod:d} and is 0")
