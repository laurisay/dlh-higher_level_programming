#!/usr/bin/python3
"""
Module that creates a write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename (str, optional): The file to write to. Defaults to "".
        text (str, optional): The text to write. Defaults to "".
    Returns:
        int: Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
