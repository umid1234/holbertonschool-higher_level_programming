#!/usr/bin/python3
"""Basic serialization and deserialization using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
