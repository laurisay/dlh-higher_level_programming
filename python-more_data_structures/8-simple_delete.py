#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    copy = a_dictionary
    if key in copy:
        del copy[key]
    return copy
    """
    anothe solution with .pop() function 🈂️
    if key in dictionary:
        dictionary.pop(key)
    """
