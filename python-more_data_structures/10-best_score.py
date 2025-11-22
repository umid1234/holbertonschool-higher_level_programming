#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # If the dictionary is empty, return None
        return None
    best_key = None
    max_val = float('-inf')  # Initialize to negative infinity for comparison
    for key, value in a_dictionary.items():
        if value > max_val:
            max_val = value
            best_key = key
    return best_key
