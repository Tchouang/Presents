#!/usr/bin/env python
"""reducer.py"""

import sys
import decimal
import pandas as pd


# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, commandes):
    cpcli, datcde, codcde, timbrecde, Nbcolis, qte, points = line.strip().split(";")
    if codcde not in commandes:
        commandes[codcde] = {
            "cpcli": cpcli,
            "datcde": datcde,
            "timbrecde": timbrecde,
            "Nbcolis": Nbcolis,
            "qte": qte,
            "points": points
        }
    else:
        # Si le code de commande existe déjà, mettre à jour les informations d'agrégation
        commandes[codcde]["Nbcolis"] += int(Nbcolis)
        commandes[codcde]["qte"] += int(qte)
        commandes[codcde]["points"] += int(points)


# Dictionnaire
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

#Trie dictionnaire en fonctio de points

sorted_commande = sorted (
    commandes.items(),key=lambda x: x[1]["points"], reverse=True
)

#Création Dataframe

mydata = []
for codcde, value in sorted_commande[:100]:
    mydata.append(
        [
            codcde,
            value["cpcli"],
            value["datcde"],
            value["timbrecde"],
            value["Nbcolis"],
            value["qte"],
            value["cpcli"],
            value["points"],
        ]
    )


df = pd.DataFrame(
    mydata,
    columns=[
        "cpcli",
        "datcde",
        "codcde",
        "timbrecde",
        "Nbcolis",
        "qte",
        "points", 
    ]
)

#Enregistrez le DataFrame dans un fichier Excel
excel_file = "/datavolume1/lot2_exo1.xlsx"
df.to_excel(excel_file, index=False)
