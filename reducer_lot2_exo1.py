#!/usr/bin/env python
"""reducer.py"""

import sys
import decimal
import pandas as pd
import datetime

# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, commandes,key_line):
    parts = line.strip().split(';')
    #cpcli client postal code
    dummy_cpcli=int(parts[0][0:2])
    cpcli=int(parts[0])
    #command code
    codcde = parts[1]
    #datcde command datetime
    datcde=parts[2]
    if datcde == "NULL":
        dummy_datcde=0
        datcde=0
    else:
        dummy_datcde = int(parts[2][0:4])
    #franking price
    timbrecde = parts[3]
    #Packages number
    Nbcolis =parts[4]
    #Quantities
    qte = parts[5]
    #Command points
    if parts[6] == 'NULL':
        points_commande = 0
    else:
        points_commande = int(parts[6])

# Dictionnaire
commandes = {}

n=0
# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes,n)
    n=n+1
    
#Triez le dictionnaire en fonction de la clé "points_commande"
sorted_commandes = sorted(
commandes.items(), key=lambda x: x[1]["command_points"], reverse=True
)

# print(f"sorted_commands :  {sorted_commandes}")

#Créez un DataFrame à partir des données
mydata = []
for key_line, values in sorted_commandes:
    #Données à ajouter dans le tableau mydata
    mydata.append([values["postal_code"], values["command_date_time"], values["command_code"],values["franking_price"],values["packages_number"],\
        values["quantities"],values["command_points"]])

# # Donner à mettre dans le dataframe : mydata
df = pd.DataFrame(mydata)

# # Enregistrez le DataFrame dans un fichier Excel
# #excel_file = "/datavolume1/lot2_exo1.xlsx"
excel_file = "lot2_exo1.xlsx"
df.to_excel(excel_file, index=False)
