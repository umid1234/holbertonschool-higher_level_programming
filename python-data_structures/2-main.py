#!/usr/bin/python3
import sys
replace_in_list = __import__("2-replace_in_list").replace_in_list
my_list = [1, 2, 3, 4, 5]
argv = sys.argv
idx = int(argv[1])
new_element = int(argv[2])
new_list = replace_in_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
