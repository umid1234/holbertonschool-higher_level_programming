#!/usr/bin/python3
"""Module-0 eads a text file (UTF8) and prints it to stdout"""
def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, "r") as file:
        content = file.read()
        print(content)