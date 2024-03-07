
"""reducer.py"""

import sys
import decimal
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
            #à modifier si nécessaire pour questions suivantes
            "cpcli": cpcli[0:2],
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

#Trie dictionnaire en fonctio de points

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
        "datcde",
        "codcde",
        "cpcli",
        "timbrecde",
        "Nbcolis",
        "qte",
        "points", 
    ]
)

#Filtre pour avoir que les objets qui ont plus de 100 points
df = df[df['points'] > 100]

#Comptage du nombre de ligne du dataframe
n_line=len(df)
print()

#Création du dictionnnaire pour les pourcentages par département
dfcdcp=df.groupby(['cpcli']).size()
percent28= dfcdcp.iloc[0]/n_line
percent50= dfcdcp.iloc[1]/n_line
percent53= dfcdcp.iloc[2]/n_line
percent61= dfcdcp.iloc[3]/n_line
print(percent28+percent50+percent61+percent53+percent61)

#Création du graphique par secteur
plt.figure(figsize=(8, 8))
labels = ['Département 28', 'Département 50', 'Département 53', 'Département 61']
plt.pie([percent28,percent50,percent53,percent61], labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pourcentage de commandes par département pour objet ayant plus de 100 points")



#Sauvegarde en graphique
output_pdf_file = 'resultat_filtré.pdf'
with PdfPages(output_pdf_file) as pdf:
    pdf.savefig()  

print("Le graphique a ete enregistre au format PDF dans le fichier %s" % output_pdf_file)



#Sauvegarde en exel
excel_file = "donnees_point_ii.xlsx"
df_excel = df[['codcde', 'datcde', 'cpcli', 'Nbcolis', 'qte']]
df_excel.to_excel(excel_file, index=False)

print("Les données ont été enregistrées dans le fichier Excel : %s" % excel_file)