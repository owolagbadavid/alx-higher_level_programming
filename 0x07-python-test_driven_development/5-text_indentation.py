#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these
    characters: ., ? and :.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    space = 0
    for i in range(len(text)):
        if text[i] == " " and space == 0:
            continue
        elif text[i] != " " and space == 0:
            space = 1
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            space = 0
