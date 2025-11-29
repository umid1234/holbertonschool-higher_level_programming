#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries to/from XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.
    """
    root = ET.Element("data")

    # Add each dictionary item as a child element
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML content from a file into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        # XML stores everything as text → remain consistent with example
        result[child.tag] = child.text

    return result
