#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    A function that replace all occurrences of an element by another in a list
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
