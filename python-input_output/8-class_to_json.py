#!/usr/bin/python3
"""Module that provides a function to serialize an object's attributes."""


def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.
    """
    return obj.__dict__
