#!/usr/bin/python3
"""Function that inserts a line of text to a file, after each line containing
a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file, after each line
    containing a specific string"""


    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
        f.seek(0)
        f.writelines(lines)
