#!/usr/bin/python3
"""
Module that defines a Student class
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    Defaults to None.
        Returns:
            dict: Dictionary containing the specified attributes of the Student
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
