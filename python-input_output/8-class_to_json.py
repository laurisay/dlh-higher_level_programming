#!/usr/bin/python3
"""
Module that creates a class_to_json function
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a Class
    Returns:
        dict: Dictionary description of the object
    """
    return obj.__dict__
