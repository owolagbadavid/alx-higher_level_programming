#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list_of_integers
    lent = len(li)
    if lent == 0:
        return
    m = lent // 2
    if (m == lent - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >=
                                                  li[m - 1]):
        return li[m]
    if m != lent - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
