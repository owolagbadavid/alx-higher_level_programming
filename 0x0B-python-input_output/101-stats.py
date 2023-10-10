#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys
import os.path


def print_stats(file_size, status_codes):
    """Function that prints the stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def parse_line(line, file_size, status_codes):
    """Function that parses a line"""
    line = line.split()
    file_size += int(line[-1])
    status_codes[line[-2]] += 1
    return file_size, status_codes


def main():
    """Function that reads stdin line by line and computes metrics"""
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    i = 0
    try:
        for line in sys.stdin:
            file_size, status_codes = parse_line(line, file_size, status_codes)
            i += 1
            if i % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise


if __name__ == "__main__":
    main()
