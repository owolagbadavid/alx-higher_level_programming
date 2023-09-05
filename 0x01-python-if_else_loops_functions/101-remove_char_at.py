#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    count = 0
    for i in str:
        if count != n:
            str_copy += i
        count = count + 1
    return str_copy
