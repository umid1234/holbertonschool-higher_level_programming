#!/usr/bin/python3
import sys
element_at = __import__("1-element_at").element_at
my_list = [1, 2, 3, 4, 5]
argv = sys.argv[1]
idx = int(argv)
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
