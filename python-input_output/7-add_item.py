#!/usr/bin/python3
"""Script that adds arguments to a list and saves them to a JSON file."""
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])  # Add all command-line arguments
save_to_json_file(my_list, filename)
