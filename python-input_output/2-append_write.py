#!/usr/bin/python3
"""Module containing a function that appends text to a file."""


def append_write(filename="", text=""):
    """
    Append a string to the end of a UTF-8 text file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
