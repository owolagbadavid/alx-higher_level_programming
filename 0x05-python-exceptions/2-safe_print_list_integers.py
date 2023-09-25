#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for j in range(x):
            if type(my_list[j]) is int:
                print("{:d}".format(my_list[j]), end="")
                i += 1
        print()
        return i
    except (TypeError, ValueError):
        print()
        return i
