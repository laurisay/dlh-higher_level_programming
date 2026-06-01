#!/usr/bin/python3
"""
Module that provides XML serialization and deserialization functions
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML and save to a file

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The filename to save the XML data to
    Returns:
        None
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Iterate through dictionary items and add as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create XML tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Read XML data from a file and return a deserialized Python dictionary

    Args:
        filename (str): The filename to read the XML data from
    Returns:
        dict: The deserialized Python dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except Exception:
        return None
