import happybase
import csv
from datetime import datetime




connection = happybase.Connection('node176250-env-1839015-etudiant37.sh1.hidora.com', 11775)
connection.open()
table_name = 'maTable'  
table = connection.table(table_name)

# Fonction pour vérifier si une chaîne peut être convertie en date valide
def is_valid_datcde(datcde_str):
    try:
        datetime.strptime(datcde_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Fonction pour importer les données de datawfro dans HBase
def import_csv_to_hbase(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Vérifier la validité de la date
            if not is_valid_datcde(row['datcde']):
                continue
            
            # Remplacer les valeurs NULL par 0 pour les autres données hors date
            for key, value in row.items():
                if key != 'datcde' and (value.strip() == '' or value.strip().lower() == 'null'):
                    row[key] = '0' if key.isdigit() else '0'
            table.put(row['row_key'], row)

# Avant l'importation des données
if connection is not None:
    print("Avant l'importation des données - Connexion à HBase établie")
else:
    print("Erreur: La connexion à HBase n'est pas établie")

import_csv_to_hbase('dataw_fro03.csv')

# Après l'importation des données
if connection is not None:
    print("Après l'importation des données - Connexion à HBase établie", connection.is_table_enabled(table_name))
else:
    print("Erreur: La connexion à HBase n'est pas établie",  connection.is_table_enabled(table_name))



connection.close()
