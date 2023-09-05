#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        alp = i
    else:
        alp = i - 32
    print("{:s}".format(chr(alp)), end="")
