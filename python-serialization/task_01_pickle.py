#!/usr/bin/python3
"""
Pickling module that provides a CustomObject class with serialization
and deserialization capabilities using the pickle module
"""
import pickle


class CustomObject:
    """Custom class that can be serialized and deserialized using pickle"""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance

        Args:
            name (str): Name of the person
            age (int): Age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes in a formatted way"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file

        Args:
            filename (str): The filename to save the serialized object to
        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file

        Args:
            filename (str): The filename to load the serialized object from
        Returns:
            CustomObject: An instance of CustomObject or None if error
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
