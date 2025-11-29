#!/usr/bin/python3
"""Module that saves a Python object to a file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize.
        filename (str): The file to write the JSON string into.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
