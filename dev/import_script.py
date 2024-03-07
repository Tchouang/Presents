import happybase
import csv
from datetime import datetime
import logging
import uuid

# Configuration du journal
logging.basicConfig(level=logging.INFO)


connection = happybase.Connection('node176250-env-1839015-etudiant37.sh1.hidora.com', 11775) #VM 37 à changer par user
connection.open()
table_name = 'fromagerie'  #à changer si besoin
table = connection.table(table_name)

# Fonction pour vérifier si une chaîne peut être convertie en date valide
def is_valid_datcde(datcde_str):
    try:
        datetime.strptime(datcde_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

# Fonction pour importer les données de datawfro dans HBase
def import_csv_to_hbase(csv_file):
    try:
        print('avant ouverture fichier')
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)
            print('ouverture fichier')
            for row in reader:
                # Générer une clé de ligne unique
                row_key = str(uuid.uuid4())
                # Vérifier la validité de la date
                if not is_valid_datcde(row['datcde']):
                    logging.warning("Date invalide dans la ligne: %s", row)
                    continue
                print('print du row')
                # Remplacer les valeurs NULL par 0 pour les autres données hors date
                for key, value in row.items():
                    if key != 'datcde' and (value.strip() == '' or value.strip().lower() == 'null'):
                        row[key] = '0' if key.isdigit() else '0'
                print('avant le put')
                table.put(str(row_key).encode(), {
                    b'cf:codcli': str(row['codcli']).encode(),
                    b'cf:genrecli': str(row['genrecli']).encode(),
                    b'nomcli': str(row['nomcli']).encode(),
                    b'cf:prenomcli': str(row['prenomcli']).encode(),
                    b'cpcli': str(row['cpcli']).encode(),
                    b'villecli': str(row['villecli']).encode(),
                    b'nomcli': str(row['nomcli']).encode(),
                    b'codcde': str(row['codcde']).encode(),
                    b'datcde': str(row['datcde']).encode(),
                    b'timbrecli': str(row['timbrecli']).encode(),
                    b'timbrecde': str(row['timbrecde']).encode(),
                    b'Nbcolis': str(row['Nbcolis']).encode(),
                    b'cheqcli': str(row['cheqcli']).encode(),
                    b'barchive': str(row['barchive']).encode(),
                    b'bstock': str(row['bstock']).encode(),
                    b'codobj': str(row['codobj']).encode(),
                    b'qte': str(row['qte']).encode(),
                    b'Colis': str(row['Colis']).encode(),
                    b'libobj': str(row['libobj']).encode(),
                    b'Tailleobj': str(row['Tailleobj']).encode(),
                    b'Poidsobj': str(row['Poidsobj']).encode(),
                    b'points': str(row['points']).encode(),
                    b'indispobj': str(row['indispobj']).encode(),
                    b'libcondit': str(row['libcondit']).encode(),
                    b'prixcond': str(row['prixcond']).encode(),
                    b'puobj': str(row['puobj']).encode(),
                })
                
                
    except Exception as e:
        logging.error("Erreur lors de l'importation des données: %s", str(e))

# Avant l'importation des données
if connection is not None:
    logging.info("Avant l'importation des données - Connexion à HBase établie")
else:
    logging.error("Erreur: La connexion à HBase n'est pas établie")

import_csv_to_hbase('dataw_fro03_mini_100.csv')

# Après l'importation des données
if connection is not None:
    logging.info("Après l'importation des données - Connexion à HBase établie")
else:
    logging.error("Erreur: La connexion à HBase n'est pas établie")

# Fermeture de la connexion
connection.close()
