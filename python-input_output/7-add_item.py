#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""
import sys
import json

# Importer les fonctions depuis les fichiers précédents
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Essayer de charger la liste existante
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # Si le fichier n'existe pas, créer une liste vide
    my_list = []

# Ajouter tous les arguments de la ligne de commande (sauf le nom du script)
for arg in sys.argv[1:]:
    my_list.append(arg)

# Sauvegarder la liste mise à jour dans le fichier
save_to_json_file(my_list, filename)
