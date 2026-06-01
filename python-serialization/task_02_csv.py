#!/usr/bin/python3
"""
Module that converts CSV data to JSON format
"""
import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON format and save to data.json

    Args:
        filename (str): The name of the CSV file to read
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        data_list = []
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)
        
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
