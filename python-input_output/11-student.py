#!/usr/bin/python3
"""
Module that create a Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """Init method

        Args:
            first_name (str): Student First name
            last_name (str): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Represent a instance in dict form

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    Defaults to None.
        Returns:
            dict: instance in dict form represented
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
