#!/usr/bin/python3
for k in range(0, 100):
    if k == 99:
        print("{}".format(k), end="\n")
        break
    print("{:02}".format(k), end=", ")
