#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

def process_line(line, commandes, key_line, seen_keys):
    # Partie de traitement des lignes

    # Vérifier si la clé de la commande a déjà été vue
    if key_line not in seen_keys:
        # Ajouter la clé à l'ensemble des clés vues
        seen_keys.add(key_line)
        
        # Ajouter la commande au dictionnaire de commandes
        commandes[key_line] = {
            "postal_code": cpcli,
            "command_date_time": datcde,
            "command_code": codcde,
            "franking_price": timbrecde,
            "packages_number": Nbcolis,
            "quantities": qte,
            "command_points": points_commande
        }

# Créer un ensemble pour stocker les clés des commandes déjà rencontrées
seen_keys = set()

# Créer un dictionnaire pour stocker les commandes sélectionnées
commandes = {}

# Créer un lecteur CSV pour gérer les données
csv_reader = csv.reader(sys.stdin)

# Ignorer la première ligne (en-tête)
next(csv_reader, None)

# Parcourir les lignes du CSV
for row in csv_reader:
    # Extraire les champs du CSV
    cpcli, codcde, datcde, timbrecde, Nbcolis, qte, points = (
        row[4],
        row[6],
        row[7],
        row[9],
        row[10],
        row[15],
        row[20],
    )

    # Convertir les données si nécessaire (comme indiqué dans votre code original)

    # Créer la clé de la ligne
    key_line = (cpcli, codcde, datcde, timbrecde, Nbcolis, qte, points)

    # Traiter la ligne
    process_line(row, commandes, key_line, seen_keys)

# Imprimer les commandes sélectionnées sans doublons
for key, value in commandes.items():
    print('%s;%s;%s;%s;%s;%s;%s' % (value["postal_code"], value["command_code"], value["command_date_time"],
                                     value["franking_price"], value["packages_number"], value["quantities"], value["command_points"]))
