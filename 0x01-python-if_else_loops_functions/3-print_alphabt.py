#!/usr/bin/python3
for k in range(97, 123):
    if (chr(k) == 'q' or chr(k) == 'e'):
        continue
    print("{}".format(chr(k)), end="")
