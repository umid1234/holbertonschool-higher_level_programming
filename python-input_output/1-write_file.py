#!/usr/bin/python3
"""Module-1 function that writes a string to a text file"""


def write_file(filename="", text=""):
    """fucntion that writes"""
    with open(filename, "w") as file:
        file.write(text)