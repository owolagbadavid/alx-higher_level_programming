#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d} argument".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print("s.")
    elif len(sys.argv) == 2:
        print(":")
    else:
        print("s:")
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
