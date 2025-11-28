#!/usr/bin/python3
"""
Module-1  function that returns
True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """This function checks whether the object is an instance of some class"""
    return type(obj) is a_class
