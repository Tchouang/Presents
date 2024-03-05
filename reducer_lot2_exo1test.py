#!/usr/bin/env python
"""reducer.py"""

import sys
import decimal
import pandas as pd


# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, commandes):
    cpcli, codcde, timbrecde, Nbcolis, qte, points = line.strip().split(";")
    #TODO aggrégation et changement de types

# Dictionnaire
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

#

df = pd.DataFrame("DONNER A METTRE")

# # Enregistrez le DataFrame dans un fichier Excel
# excel_file = "/datavolume1/lot2_exo1.xlsx"
# df.to_excel(excel_file, index=False)
