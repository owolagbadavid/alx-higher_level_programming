#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys


def print_stats(file_size, status_codes):
    """Function that prints the stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
counter = 0
try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        try:
            file_size += int(data[-1])
        except Exception:
            pass
        try:
            status_codes[data[-2]] += 1
        except Exception:
            pass
        if counter % 10 == 0:
            print_stats(file_size, status_codes)
    print_stats(file_size, status_codes)
except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise
