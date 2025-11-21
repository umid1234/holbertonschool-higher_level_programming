#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = [0] * len(my_list)
    for i in range(len(my_list)):
        if my_list[i] == search:
            arr[i] = replace
        else:
            arr[i] = my_list[i]
    return arr
