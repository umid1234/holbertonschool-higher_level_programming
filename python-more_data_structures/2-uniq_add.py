#!/usr/bin/python3
def uniq_add(my_list=[]):
    count_sum = 0
    j = 0
    arr = [None] * len(my_list)
    for i in range(len(my_list)):
        if my_list[i] not in arr:
            arr[j] = my_list[i]
            count_sum += my_list[i]
            j += 1
    return count_sum
