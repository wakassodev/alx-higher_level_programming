#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if ((idx < 0) or (idx > len(my_list) - 1)):
        return my_list
    mutation = [index for index in my_list]
    mutation[idx] = element
    return mutation
