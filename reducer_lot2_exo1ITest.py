#!/usr/bin/env python
"""reducer.py"""

import sys
import decimal
import pandas as pd
import matplotlib.pyplot as plt

# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire mydata
def process_line(line, commandes):
    cpcli, datcde, codcde, timbrecde, Nbcolis, qte, points = line.strip().split(";")
    if Nbcolis == "NULL": Nbcolis=0
    else: Nbcolis=int(Nbcolis)  
    if qte == "NULL": qte=0
    else: qte=int(qte)         
    if points =="NULL": points=0 
    else:points=int(points)   
    if codcde not in commandes:
        commandes[codcde] = {
            "datcde": datcde,
            "codcde" : codcde,
            "cpcli": cpcli,
            "timbrecde": timbrecde,
            "Nbcolis": Nbcolis,
            "qte": qte,
            "points": points,
        }
    else:
        # Si le code de commande existe déjà, mettre à jour les informations d'agrégation
        commandes[codcde]["Nbcolis"] += (Nbcolis)
        commandes[codcde]["qte"] += (qte)
        commandes[codcde]["points"] += (points)


# Dictionnaire
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

#Trie dictionnaire en fonction de points
sorted_commande = sorted (
    commandes.items(),key=lambda x: x[1]["points"], reverse=True
)

#Création Dataframe
mydata = []
for codcde, value in sorted_commande:
    mydata.append(
        [
            codcde,
            value["datcde"],
            value["cpcli"],
            value["timbrecde"],
            value["Nbcolis"],
            value["qte"],
            value["points"],
        ]
    )

df = pd.DataFrame(
    mydata,
    columns=[
        "codcde",
        "datcde",
        "cpcli",
        "timbrecde",
        "Nbcolis",
        "qte",
        "points", 
    ]
)

# Calculer le pourcentage de commandes par département
dept_counts = df['cpcli'].value_counts(normalize=True) * 100

# Créer un graphe en secteurs (pie chart)
plt.figure(figsize=(8, 8))
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
plt.title('Pourcentage de commandes par département')

# Enregistrer le graphe dans un fichier PDF dans le dossier de partage /datavolume1
pdf_file = "pourcentage_commandes_par_departement.pdf"
plt.savefig(pdf_file)

# Afficher le graphe si besoin
plt.show()

#Création du graphique par secteur
plt.figure(figsize=(8, 8))
plt.pie(values, labels=dfcdcp, autopct='%1.1f%%', startangle=140)