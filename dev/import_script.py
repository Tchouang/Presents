import happybase
import csv
from datetime import datetime

# Connexion à HBase
connection = happybase.Connection('node176250-env-1839015-etudiant37.sh1.hidora.com:11775, port=11775')
table_name = 'fromagerie_table'  
table = connection.table(table_name)

# Fonction pour vérifier si une chaîne peut être convertie en date valide
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Fonction pour importer les données du fichier CSV dans HBase
def import_csv_to_hbase(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Vérifier la validité de la date
            if not is_valid_date(row['date']):
                # Passer à la prochaine ligne si la date est invalide
                continue
            
            # Remplacer les valeurs NULL par 0 pour les données numériques
            for key, value in row.items():
                if value.strip() == '':
                    row[key] = '0' if key.isdigit() else ''
            # Insérer la ligne dans HBase
            table.put(row['row_key'], row)

# Appel de la fonction pour importer les données du fichier CSV dans HBase
import_csv_to_hbase('dataw_fro03.csv')

# Fermer la connexion à HBase
connection.close()
