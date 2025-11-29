#!/usr/bin/python3
"""Module that provides a function to serialize an object's attributes."""
def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.

    Args:
        obj: The object to convert.

    Returns:
        dict: The dictionary containing the object's serializable attributes.
    """
    return obj.__dict__
