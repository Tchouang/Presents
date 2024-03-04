#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
import pandas as pd


dict = {4: "postal_code", 6: "command_code", 7: "command_date_time", 9: "franking_price", 10: "packages_number", 15: "quantities", 20: "points"}
print(pd.DataFrame(list(dict.items()), columns=["Code", "Items"]))

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

    
    key_line = (cpcli, codcde, datcde, timbrecde, Nbcolis, qte, points)

    # Traiter la ligne
    process_line(row, commandes, key_line, seen_keys)

# Imprimer les commandes sélectionnées sans doublons
for key, value in commandes.items():
    print('%s;%s;%s;%s;%s;%s;%s' % (value["postal_code"], value["command_code"], value["command_date_time"],
                                     value["franking_price"], value["packages_number"], value["quantities"], value["command_points"]))
