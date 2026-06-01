#!/usr/bin/python3
"""
Module that creates an append_write function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str, optional): The file to append to. Defaults to "".
        text (str, optional): The text to append. Defaults to "".
    
    Returns:
        int: Number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
