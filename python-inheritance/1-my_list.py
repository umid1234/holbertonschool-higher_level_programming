#!/usr/bin/python3
"""
Docstring for MyList which will print the sorted list
"""


class MyList(list):
    """
    MyList class that inherits from list class
    """
    
    def print_sorted(self):
        """Docstring for print_sorted """
        print(sorted(self))
