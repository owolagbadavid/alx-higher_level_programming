#!/usr/bin/python3
import sys


def print_stats():
    print('File size: {:d}'.format(file_size))

    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{}: {:d}'.format(key, value))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

counter = 0
file_size = 0

try:
    for line in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            print_stats()

        data = line.split()

        try:
            status = int(data[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except:
            pass

        try:
            file_size += int(data[-1])
        except:
            pass

        counter += 1

    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise